"""
p73
python argparse_example.py -h
python argparse_example.py ships list
python argparse_example.py ships sail
python argparse_example.py sailors
python argparse_example.py sailors Tony
python argparse_example.py sailors Tony --greeting Hello
python argparse_example.py sailors --greeting Hello

此範例可使用 git stash list/pop 的概念來想
而此 py file 則為 git 的概念
stash 為 主解析器
list/pop 為 子解析器

此範例有 2 組指令: {ships,sailors}

ships list
ships sail
sailors 
"""

import argparse


def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")


def list_ships():
    ships = ["John B", "Yankee Clipper", "Pequod"]
    for s in ships:
        print("Ships: " + s)


def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)


if __name__ == "__main__":
    # Top level parser
    parser = argparse.ArgumentParser(description="Maritime control")

    # Top level 引數: -t/--twice
    parser.add_argument("--twice", "-t", help="Do it twice", action="store_true")

    # 建立 Top level 的下一層 subparsers
    subparsers = parser.add_subparsers(dest="func")
    # 後續可用 parser.parse_args().func 來使用

    ### 等同於 git stash list 的 stash
    # 建立 subparsers 參數名稱 - ships 及 sailors
    ship_parser = subparsers.add_parser("ships", help="Ship related commands")
    sailor_parser = subparsers.add_parser("sailors", help="Talk to a sailor")

    ### 等同於 git stash list 的 list
    # 建立 subparsers 底下的參數
    ship_parser.add_argument("command", choices=["list", "sail"])
    sailor_parser.add_argument("name", help="Sailors name")
    sailor_parser.add_argument("--greeting", "-g", help="Greeting", default="hola")

    args = parser.parse_args()
    if args.func == "sailors":
        greet(args.greeting, args.name)
    elif args.command == "list":
        list_ships()
    else:
        sail()
