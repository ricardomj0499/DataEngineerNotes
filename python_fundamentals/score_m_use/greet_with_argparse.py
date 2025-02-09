import argparse


def greet(name: str, times: int):
    for _ in range(times):
        print(f"Hola {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="programa greet", description="A simple greeting script."
    )

    parser.add_argument("name", type=str, help="nombre de persona a saludar") # Obligatorio
    parser.add_argument(
        "--times", "-t", type=int, default=1, help="num veces a saludar"
    ) # Opcional

    args = parser.parse_args()  # se puede pasar namespace
    greet(args.name, args.times)

"""
other argparse options
    parser = argparse.Namespace
    parser = argparse.MetavarTypeHelpFormatter
    parser = argparse.Action
    parser = argparse.ArgumentError
    parser = argparse.FileType

    parser.add_argument_group()
"""
