"""socket

套接字的创建
s = socket.socket(xx, xxx)

绑定
s.bind((host, port))

连接
s.connet((host, port))

数据收发，视为文件
s.recv
s.send
"""
import socket


def func():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind(("127.0.0.1", 9999))
        server.listen(5)

        while True:
            client, addr = server.accept()  # blocking

            print(addr)

            msg = "welcome to visit me!"
            client.send(msg.encode("utf8"))

            while True:
                print(client.recv(1024))

    except Exception as e:
        raise e
    finally:
        server.close()


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()
