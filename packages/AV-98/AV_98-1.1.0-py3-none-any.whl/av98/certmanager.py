import glob
import logging
import os
import os.path
import shutil
import tempfile
import uuid

try:
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    _HAS_CRYPTOGRAPHY = True
    _BACKEND = default_backend()
except ModuleNotFoundError:
    _HAS_CRYPTOGRAPHY = False

import av98.util as util

ui_out = logging.getLogger("av98_logger")

def certfile_to_fingerprint(certfile):
    print(certfile)
    with open(certfile, "rb") as fp:
        pem_bytes = fp.read()
        cert = x509.load_pem_x509_certificate(pem_bytes, _BACKEND)
        return cert.fingerprint(hashes.SHA256()).hex()

class ClientCertificateManager:

    def __init__(self, config_dir, db_conn):

        self.config_dir = config_dir
        self.certdir = os.path.join(self.config_dir, "client_certs")
        self.db_conn = db_conn
        self.db_cur = db_conn.cursor()
        self.create_db()
        self.legacy_certs = self.find_legacy_certs()
        self.certs_used_this_session = set()
        self.hard_wired = False
        self.hard_cert = None
        self.hard_key = None

    def create_db(self):
        self.db_cur.execute("""CREATE TABLE IF NOT EXISTS client_certs
            (hostname text, port integer, root text, filename text,
            nickname text)""")

    def find_legacy_certs(self):
        """
        Identify certificate files created by earlier versions of AV-98.

        Client certificates created by AV-98 are now tracked via a
        `client_certs` table in the SQLite database which associates
        certificate/key filenames (derived from the cert fingerprint) with a
        particular host, port and root path.  However, in earlier versions of
        the client, certificate management was much more manual.

        This function checks for certificate files in self.certdir which do not
        seem to have a corresponding entry in the SQLite database.  These are
        termed "legacy certificates".  They can still be used, and when they are
        the database is updated appropriately, i.e. they stop being legacy
        certificates after their first use in a modern version of the client.
        """
        if not os.path.exists(self.certdir):
            return []
        legacy = []
        for c in glob.glob(os.path.join(self.certdir, "*.crt")):
            base = os.path.basename(c)[:-4]
            self.db_cur.execute("""SELECT * FROM client_certs WHERE filename=?""", (base,))
            hits = self.db_cur.fetchall()
            if not hits:
                legacy.append(base)
        return legacy

    def record_cert_in_db(self, host, port, root, filename, nickname):
        """
        Associate a certificate file with a particular host, port and path.
        """
        self.db_cur.execute("""INSERT INTO client_certs
            (hostname, port, root, filename, nickname)
            VALUES (?, ?, ?, ?, ?)""",
            (host, port, root, filename, nickname))
        self.db_conn.commit()

    def get_cert_nickname(self, fingerprint):
        self.db_cur.execute("""SELECT nickname FROM client_certs WHERE filename=?""", (fingerprint,))
        return self.db_cur.fetchone()[0]

    def get_cert_scopes(self, fingerprint):
        self.db_cur.execute("""SELECT hostname, port, root FROM client_certs
            WHERE filename=?""", (fingerprint,))
        scopes = self.db_cur.fetchall()
        scopes = ["gemini://{}:{}{}".format(h, p, r) for (h, p, r) in scopes]
        return scopes

    def manage(self):
        """
        Launch an interactive management tool for client certificates.
        """
        while True:
            # List current certificates
            print("AV-98 CLIENT CERTIFICATE MANAGER")
            print("")
            print("Client certificates associated with destinations:")
            print("(* denoes active certificates)")
            print("")

            self.db_cur.execute("""SELECT * FROM client_certs""")
            certs = self.db_cur.fetchall()
            for n, cert in enumerate(certs):
                print("{}. {} {} gemini://{}:{}/{}".format(n+1,
                                                       "*" if cert[3] in self.certs_used_this_session else " ",
                                                       cert[4].ljust(24),
                                                       cert[0], cert[1], cert[2]))
            print("")
            if self.legacy_certs:
                print("Legacy certificates:")
                print("")

                for n, cert in enumerate(self.legacy_certs):
                    print("{}. {}".format(len(certs) +n+1, cert))

            # Prompt for a certificate to manage
            print("Choose a certificate by number, or just press enter to exit cert manager.")
            choice = input("> ").strip()
            if not choice:
                break
            try:
                choice = int(choice)
            except:
                print("What?")
                continue

            # Manage a particular cert
            if 1 <= choice <= len(certs) + len(self.legacy_certs):
                # Display cert info
                if choice <= len(certs):
                    fingerprint = certs[choice - 1][3]
                else:
                    fingerprint = self.legacy_certs[choice - 1 - len(certs)]
                nickname = self.get_cert_nickname(fingerprint)
                scopes = self.get_cert_scopes(fingerprint)
                active = fingerprint in self.certs_used_this_session
                filename = os.path.join(self.certdir, "{}.crt".format(fingerprint))
                with open(filename, "rb") as fp:
                    pem_bytes = fp.read()
                    cert = x509.load_pem_x509_certificate(pem_bytes, _BACKEND)
                    print("Nickname:    {}".format(nickname))
                    print("Scope:       {}".format(scopes[0]))
                    if len(scopes) > 1:
                        for scope in scopes[1:]:
                            print("             {}".format(scopes[0]))
                    print("Expiry:      {}".format(cert.not_valid_after_utc))
                    print("Active:      {}".format("yes" if active else "no"))
                    print("")

                # Prompt for action
                while True:
                    print("1. Delete certificate")
                    if active:
                        print("2. Deactivate certificate")
                    else:
                        print("2. Activate certificate")
                    print("3. Return to certificate manager")
                    choice = input("> ").strip()
                    if choice == "1":
                        # Delete certificate
                        print("CERTIFICATE DELETION IS IRREVERSIBLE!")
                        print("Type 'Delete' to confirm:")
                        choice = input("> ").strip()
                        if choice == "Delete":
                            # Remove from DB
                            print(fingerprint)
                            self.db_cur.execute("""DELETE FROM client_certs
                            WHERE filename=?""", (fingerprint,))
                            self.db_conn.commit()
                            # Remove from disk
                            os.unlink(filename)
                            os.unlink(filename.replace(".crt", ".key"))
                            # Remove from active set
                            if fingerprint in self.certs_used_this_session:
                                self.certs_used_this_session.remove(fingerprint)
                            print("Certificate delete!")
                            break
                        else:
                            print("Aborting.")
                    elif choice == "2":
                        if active:
                            self.certs_used_this_session.remove(fingerprint)
                        else:
                            self.certs_used_this_session.add(fingerprint)
                    elif choice == "3":
                        break
                    else:
                        print("What?")
            else:
                print("No such cert!")

    def associate_client_cert(self, context, gi):
        """
        Decide whether the TLS context for fetching gi should use a client cert.

        Return TRUE or FALSE depending on whether or not a certificate was
        attached to the context so that the prompt can be updated accordingly.

        Note that this method is called before every request for a gi, not only
        when a status code beginning with 6 is encountered.
        """
        # Do we have a hard-wired cert?
        if self.hard_wired:
            context.load_cert_chain(self.hard_cert, self.hard_key)
            return True

        # Do any certs exist for this host/port?
        self.db_cur.execute("""SELECT root, filename, nickname
            FROM client_certs
            WHERE hostname=? AND PORT=?""",
            (gi.host, gi.port))
        host_certs = self.db_cur.fetchall()
        if not host_certs:
            return False

        # Is the current URL path below the root of any of them?
        applicable_certs = [(filename, nickname) for root, filename, nickname in host_certs if gi.path.startswith(root)]
        if not applicable_certs:
            return False

        # If there's only one matching cert, things are easy...
        if len(applicable_certs) == 1:
            filename = applicable_certs[0][0]
            if filename in self.certs_used_this_session or util.ask_yes_no("PRIVACY ALERT: Reactivate previously used client cert for gemini://{}:{}{}?".format(gi.host, gi.port, gi.path)):
                certfile = os.path.join(self.certdir, "{}.crt".format(filename))
                keyfile = os.path.join(self.certdir, "{}.key".format(filename))
                context.load_cert_chain(certfile, keyfile)
                self.certs_used_this_session.add(filename)
                return True

            else:
                print("Remaining unidentified.")

        # ...otherwise, the use must choose
        else:
            print("Reactivate one of the following previously used client certs for gemini://{}:{}{}?".format(gi.host, gi.port, gi.path))
            filename = util.ask_from_numbered_list([c[0] for c in applicable_certs], [c[1] for c in applicable_certs], "None")
            if filename:
                certfile = os.path.join(self.certdir, "{}.crt".format(filename))
                keyfile = os.path.join(self.certdir, "{}.key".format(filename))
                print(certfile)
                print(keyfile)
                context.load_cert_chain(certfile, keyfile)
                self.certs_used_this_session.add(filename)
                return True
            else:
                return False

    def handle_cert_request(self, meta, status, host, port, path):
        """
        Allow the user to interactively respond to a response with a 6x status.
        """
        root = os.path.dirname(path)

        print("SERVER SAYS: ", meta)
        # Present different messages for different 6x statuses, but
        # handle them the same.
        if status in ("64", "65"):
            print("The server rejected your certificate because it is either expired or not yet valid.")
        elif status == "63":
            print("The server did not accept your certificate.")
            print("You may need to e.g. coordinate with the admin to get your certificate fingerprint whitelisted.")
        else:
            print("The site {} is requesting a client certificate.".format(host))
            print("This will allow the site to recognise you across requests.")

        # Give the user choices
        while True:
            print("What do you want to do?")
            print("1. Give up.")
            print("2. Generate a new certificate.")
            print("3. Reuse a previously generated certificate.")
            print("4. Import a certificate from external files.")
            if self.legacy_certs:
                print("5. Load a legacy AV-98 certificate.")
            choice = input("> ").strip()
            if choice == "1":
                print("Giving up.")
                return False
            elif choice == "2":
                if self._generate_client_cert(host, port, root):
                    return True
            elif choice == "3":
                if self._choose_client_cert(host, port, root):
                    return True
            elif choice == "4":
                if self._import_external_cert(host, port, root):
                    return True
            elif choice == "5" and self.legacy_certs:
                if self._choose_legacy_cert(host, port, root):
                    return True
            else:
                print("What?")

    def _choose_client_cert(self, host, port, root):
        """
        Select a previously created TLS client certificate stored in the
        database.
        """
        # Record in DB
        self.db_cur.execute("""SELECT filename, nickname FROM client_certs""")
        certs = self.db_cur.fetchall()
        filename = util.ask_from_numbered_list([c[0] for c in certs], [c[1] for c in certs], "Cancel")
        if filename:
            # Record in DB
            # TODO ask for nickname
            self.record_cert_in_db(self, host, port, root, filename, filename)
            self.certs_used_this_session.add(filename)
            return True
        else:
            return False

    def _import_external_cert(self, host, port, root):
        """
        Interactively load a TLS client certificate from the filesystem in PEM
        format.
        """
        print("Loading client certificate file, in PEM format (blank line to cancel)")
        certfile = input("Certfile path: ").strip()
        if not certfile:
            print("Aborting.")
            return False
        certfile = os.path.expanduser(certfile)
        if not os.path.isfile(certfile):
            print("Certificate file {} does not exist.".format(certfile))
            return False
        print("Loading private key file, in PEM format (blank line to cancel)")
        keyfile = input("Keyfile path: ").strip()
        if not keyfile:
            print("Aborting.")
            return False
        keyfile = os.path.expanduser(keyfile)
        if not os.path.isfile(keyfile):
            print("Private key file {} does not exist.".format(keyfile))
            return False

        # Compute key fingerprint to confirm these seem to be the right kind of file
        try:
            fingerprint = certfile_to_fingerprint(certfile)
        except:
            print("Certificate file {} does not seem to be a certiciate!".format(certfile))
            return False

        # Copy into certdir
        shutil.copy(certfile, os.path.join(self.certdir, "{}.crt".format(fingerprint)))
        shutil.copy(keyfile, os.path.join(self.certdir, "{}.key".format(fingerprint)))

        print("Give this certificate a nickname (or leave blank)")
        name = input("> ")
        if not name.strip():
            name = "No nickname"

        self.record_cert_in_db(self, host, port, root, fingerprint, name)
        self.certs_used_this_session.add(fingerprint)
        return True

    def _generate_client_cert(self, host, port, root):
        """
        Interactively use `openssl` command to generate a new persistent client
        certificate with one year of validity.
        """
        print("Give this certificate a nickname (or leave blank)")
        name = input("> ")
        if not name.strip():
            name = "No nickname"
        # TODO: error handling
        fingerprint = self._openssl_gen_cert()

        self.record_cert_in_db(self, host, port, root, fingerprint, name)
        self.certs_used_this_session.add(fingerprint)
        return True

    def _openssl_gen_cert(self):
        """
        Use `openssl` binary to generate a new client certificate, save it to the
        client certificate directory using its fingerprint as the filename,
        and return the fingerprint for storing in the database against the
        host, port and path.
        """
        if not os.path.exists(self.certdir):
            os.makedirs(self.certdir)
        certfile = tempfile.NamedTemporaryFile(delete=False)
        keyfile = tempfile.NamedTemporaryFile(delete=False)
        certfile.close()
        keyfile.close()
        certfile = certfile.name
        keyfile = keyfile.name
        cmd = "openssl req -x509 -newkey rsa:2048 -days {} -nodes -keyout {} -out {}".format(365, keyfile, certfile)
        os.system(cmd)
        fingerprint = certfile_to_fingerprint(certfile)
        # TODO: don't create these certs in pwd!
        shutil.move(certfile, os.path.join(self.certdir, "{}.crt".format(fingerprint)))
        shutil.move(keyfile, os.path.join(self.certdir, "{}.key".format(fingerprint)))

        return fingerprint

    def _choose_legacy_cert(self, host, port, root):
        """
        Interactively select a previously generated client certificate and
        activate it.
        """
        choice = util.ask_from_numbered_list(self.legacy_certs, self.legacy_certs, "Cancel")
        if choice:
            fingerprint = certfile_to_fingerprint(os.path.join(self.certdir, choice+".crt"))
            shutil.move(os.path.join(self.certdir, choice+".crt"), os.path.join(self.certdir, "{}.crt".format(fingerprint)))
            shutil.move(os.path.join(self.certdir, choice+".key"), os.path.join(self.certdir, "{}.key".format(fingerprint)))

            # Record in DB
            self.record_cert_in_db(self, host, port, root, fingerprint, choice)
            self.certs_used_this_session.add(fingerprint)
            return True
        else:
            return False

    def _activate_client_cert(self, certfile, keyfile):
        self.client_certs["active"] = (certfile, keyfile)
        self.active_cert_domains = []
        ui_out.debug("Using ID {} / {}.".format(*self.client_certs["active"]))

    def _deactivate_client_cert(self):
        self.client_certs["active"] = None
        self.active_cert_domains = []
