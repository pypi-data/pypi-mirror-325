#!/usr/bin/env python3
# AV-98 Gemini client
# Dervied from VF-1 (https://github.com/solderpunk/VF-1),
# (C) 2019, 2020, 2023 Solderpunk <solderpunk@posteo.net>
# With contributions from:
#  - danceka <hannu.hartikainen@gmail.com>
#  - <jprjr@tilde.club>
#  - <vee@vnsf.xyz>
#  - Klaus Alexander Seistrup <klaus@seistrup.dk>
#  - govynnus <govynnus@sdf.org>
#  - Nik <nic@tilde.team>
#  - <sario528@ctrl-c.club>
#  - rmgr
#  - Aleksey Ryndin
import argparse
import os, os.path
import shutil
import sys

from av98 import __version__
from av98.client import GeminiClient, GeminiItem

def main():

    # Parse args
    parser = argparse.ArgumentParser(description='A command line gemini client.')
    parser.add_argument('--bookmarks', action='store_true',
                        help='start with your list of bookmarks')
    parser.add_argument('--dl', '--download', action='store_true',
                        help='download a single URL and quit')
    parser.add_argument('-o', '--output', metavar='FILE',
                        help='filename to save --dl URL to')
    parser.add_argument('--tls-cert', metavar='FILE', help='TLS client certificate file')
    parser.add_argument('--tls-key', metavar='FILE', help='TLS client certificate private key file')
    parser.add_argument('--restricted', action="store_true", help='Disallow shell, add, and save commands')
    parser.add_argument('--version', action='store_true',
                        help='display version information and quit')
    parser.add_argument('url', metavar='URL', nargs='*',
                        help='start with this URL')
    args = parser.parse_args()

    # Handle --version
    if args.version:
        print("AV-98 " + __version__)
        sys.exit()

    # Instantiate client
    gc = GeminiClient(args.restricted, os.getenv("NO_COLOR", "") != "")

    # Activate client certs now in case they are needed for --download below
    if args.tls_cert or args.tls_key:
        if not args.tls_cert:
            print("--tls_key must be used in conjunction with --tls_cert!")
            sys.exit(1)
        if not args.tls_key:
            print("--tls_cert must be used in conjunction with --tls_key!")
            sys.exit(1)
        if not args.dl:
            print("--tls_cert and --tls_key can only be used in conjunction with --download!")
            sys.exit(1)
        if not os.path.exists(args.tls_cert):
            print("Certificate file {} not found!".format(args.tls_cert))
            sys.exit(1)
        if not os.path.exists(args.tls_key):
            print("Private key file {} not found!".format(args.tls_key))
            sys.exit(1)
        gc.client_cert_manager.hard_coded = True
        gc.client_cert_manager.hard_cert = os.path.abspath(args.tls_cert)
        gc.client_cert_manager.hard_key = os.path.abspath(args.tls_key)

    # Handle --download
    if args.dl:
        gc.onecmd("set debug True")
        # Download
        gi = GeminiItem(args.url[0])
        gi, mime = gc._fetch_over_network(gi)
        # Decide on a filename
        if args.output:
            filename = args.output
        else:
            if mime == "text/gemini":
                # Parse gemtext in the hopes of getting a gi.name for the filename
                gc.active_raw_file = gc.raw_file_buffer
                gc._handle_gemtext(gi)
            filename = gi.derive_filename(mime)
        # Copy from temp file to pwd with a nice name
        shutil.copyfile(gc.raw_file_buffer, filename)
        size = os.path.getsize(filename)
        # Notify user where the file ended up
        print("Wrote %d byte %s response to %s." % (size, mime, filename))
        gc.do_quit()
        sys.exit()

    # Process config file
    rcfile = os.path.join(gc.config_dir, "av98rc")
    if os.path.exists(rcfile):
        print("Using config %s" % rcfile)
        with open(rcfile, "r") as fp:
            for line in fp:
                line = line.strip()
                if ((args.bookmarks or args.url) and
                    any((line.startswith(x) for x in ("go", "g", "tour", "t")))
                   ):
                    if args.bookmarks:
                        print("Skipping rc command \"%s\" due to --bookmarks option." % line)
                    else:
                        print("Skipping rc command \"%s\" due to provided URLs." % line)
                    continue
                gc.cmdqueue.append(line)

    # Say hi
    print("Welcome to AV-98!")
    if args.restricted:
        print("Restricted mode engaged!")
    print("Enjoy your patrol through Geminispace...")

    # Add commands to the queue based on command line arguments
    if args.bookmarks:
        gc.cmdqueue.append("bookmarks")
    elif args.url:
        if len(args.url) == 1:
            gc.cmdqueue.append("go %s" % args.url[0])
        else:
            for url in args.url:
                if not url.startswith("gemini://"):
                    url = "gemini://" + url
                gc.cmdqueue.append("tour %s" % url)
            gc.cmdqueue.append("tour")

    # Endless interpret loop until user quits
    while True:
        try:
            gc.cmdloop()
            break
        except KeyboardInterrupt:
            print("")

    # Say goodbye
    print()
    print("Thank you for patrolling with AV-98!")
    sys.exit()

if __name__ == '__main__':
    main()
