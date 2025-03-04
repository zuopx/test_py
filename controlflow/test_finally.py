""""""


def main():
    try:
        raise AttributeError()
    except Exception as e:
        raise e
    finally:
        print("finally")

    print("hello, world")


if __name__ == "__main__":
    main()
