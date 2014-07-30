"""
Main file of evplan
"""

import sys

def usage():
    print("Usage: evplan CMD [ARGS]")

def main():
    if len(sys.argv) == 1:
        print("ERROR: Needs arguments")
        usage()
        exit(1)

    cmd = sys.argv[1]
    if cmd == "generate":
        from evplan import generate
        generate.generate(sys.argv[2])
    else:
        print("ERROR: Command '{}' not found".format(cmd))
