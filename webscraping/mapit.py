# mapit.py - launches a map in a browser using an address
# from the command line
# python 3 mapit.py (address)

import webbrowser, sys

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    prefix = "https://www.google.com/maps/place/"

    webbrowser.open(prefix + address)

# TODO: Get address from the clipboard.


