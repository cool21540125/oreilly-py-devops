"""
p80

python simple_fire.py --help
python simple_fire.py --greeting Hello
python simple_fire.py --greeting Hello --name TonyChou
python simple_fire.py --name TonyChou
"""

import fire


def greet(greeting="hi", name="tony"):
    print(f"{greeting} {name}")


if __name__ == "__main__":
    fire.Fire(greet)
