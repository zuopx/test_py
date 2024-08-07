""""""
import socket


def func():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((socket.gethostname(), 9999))

        msg = client.recv(1024)
        print(msg.decode("utf8"))
    except Exception as e:
        raise e
    finally:
        client.close()


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
