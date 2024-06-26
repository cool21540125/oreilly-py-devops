"""
p71
python simple_parse.py
python simple_parse.py -h
python simple_parse.py Hola
python simple_parse.py Hola --twice
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo your input")
    parser.add_argument("message", help="Message to echo")
    parser.add_argument("--twice", "-t", help="Do it twice", action="store_true")

    args = parser.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)
