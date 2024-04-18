"""
p82

python fire_example.py
python fire_example.py ships
python fire_example.py ships sail
python fire_example.py ships list
python fire_example.py sailors Hola Tony

# 此外, fire 可以進入 REPL (方便 debug??)
python fire_example.py sailors Hola Tony -- --interactive
>>> sailors
>>> sailors('hi', 'guys')
"""

import fire


class Ships:
    def sail(self):
        ship_name = "Default ship"
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ["AA", "BB", "CC"]
        for s in ships:
            print(s)


def sailors(greeting, name):
    message = f"{greeting} {name}"
    print(message)


class Cli:
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == "__main__":
    fire.Fire(Cli)
