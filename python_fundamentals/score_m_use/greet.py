# greet.py use
# python3 score_m_use/greet.py Ash
# Without ash, will print Hola mundo


def greet(name: str):
    print(f"Hola {name}")


if __name__ == "__main__":
    import sys

    # print(sys.argv)
    # print(sys.platform) linux
    # ['score_m_use/greet.py', 'Ash']
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Mundo"
    greet(name)


