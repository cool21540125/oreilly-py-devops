"""
p77
python click_example.py --help
python click_example.py ships sail
python click_example.py ships list-ships
python click_example.py sailors --help
python click_example.py sailors -g Hola~~ TonyChou
python click_example.py sailors TonyChou -g Hola~~
"""

import click


@click.group()  # 將此 function(也就是 cli) 轉變成 一個群組
def cli():
    pass


@click.group(
    help="Ship related commands"
)  # 為 ships 建立一個群組 (有點像 git stash list 的 stash)
def ships():
    pass


cli.add_command(ships)  # 將 ships 註冊到 cli (等同於 git stash list 裏頭, 將 stash 註冊到 git)


@ships.command(help="Sail a ship")
def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")


@ships.command(help="List all of the ships")
def list_ships():
    for s in ["Ship A", "Ship BB", "Ship ccc"]:
        print(s)


@cli.command(help="Talk to a sailor")
@click.option("--greeting", "-g", default="Hi there", help="Greeting for sailor")
@click.argument("name")
def sailors(greeting, name):
    print(f"{greeting} {name}")


if __name__ == "__main__":
    cli()
