# AV-98

AV-98 is a command line client for the Gemini protocol, written in Python and
released under the BSD 2-Clause License.  It features a unique and minimalistic
user interface designed to facilitate rapid keyboard-driven navigation of
Geminispace.  The code for the VF-1 Gopher client was used as a basis to
develop AV-98 and the user interface remains very similar.  Users of one will
feel very comfortable with the other.

AV-98 naturally has
[its own Gemini
capsule](gemini://zaibatsu.circumlunar.space/~solderpunk/software/av98/).
You can use AV-98 (or any other Gemini client!) to access ASCII-formatted
versions of the AV-98 man page there, along with other useful information
on installation, usage, release history, etc.

The source code lives in a
[git repo hosted at Sourcehut](https://git.sr.ht/~solderpunk/AV-98).  There is
also [a ticket tracker](https://todo.sr.ht/~solderpunk/AV-98) you can use to
report bugs.

The repository contains the following files (plus some development / packaging
related noise):

* LICENSE - text of BSD 2-Clause License
* README.md - the README file you are currently reading
* docs/av98.1 - troff source for the av98(1) man page
* src/av98/ - Python source for the AV-98 module

AV-98 has no "strict dependencies", i.e. it will run and work without anything
else beyond the Python standard library.  However, it will "opportunistically
import" a few other libraries if they are available to offer an improved
experience.

* The [ansiwrap library](https://pypi.org/project/ansiwrap/) may result in
  neater display of text which makes use of ANSI escape codes to control colour.
* The [cryptography library](https://pypi.org/project/cryptography/) will
  provide a better and slightly more secure experience when using the default
  TOFU certificate validation mode and is highly recommended.

AV-98 was developed by Solderpunk with contributions many other helpful
Geminispace folk.  See the top of `src/av98/main.py` soure file for all
contributors.
