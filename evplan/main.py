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
        if len(sys.argv) < 3:
            print(("ERROR: '{}' needs argument").format(cmd))
            usage()
            exit(1)
        from evplan import generate
        generate.generate(sys.argv[2])
    elif cmd == "run":
        from evplan import run
        run.run()
    elif cmd == "demo":
        from evplan import demo
        demo.create_demo()
    else:
        print("ERROR: Command '{}' not found".format(cmd))
