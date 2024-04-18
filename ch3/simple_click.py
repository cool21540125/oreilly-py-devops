"""
p76
python simple_click.py -h     <- 沒這東西
python simple_click.py --help <- 得用這個

python simple_click.py --greeting Hola --name TonyChou
"""
import click


@click.command()
@click.option("--greeting", default="你好", help="'How' do you want to greet?")
@click.option("--name", default="Tony", help="'Who' do you want to greet?")
def greet(greeting, name):
    print(f"{greeting} {name}")


if __name__ == "__main__":
    greet()
