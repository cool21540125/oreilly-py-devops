"""
p70
python a_demo_cli_sys_argv.py --help
python a_demo_cli_sys_argv.py --name TonyChou
python a_demo_cli_sys_argv.py --name TonyChou --greeting Hola
python a_demo_cli_sys_argv.py --greeting 摳泥擠哇
"""

import sys


def say_it(greeting, target):
    message = f"{greeting} {target}"
    print(message)


if __name__ == "__main__":
    greeting = "Hello"
    name = "Tony"

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"

    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if "--greeting" in sys.argv:
        greeting_index = sys.argv.index("--greeting") + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)
