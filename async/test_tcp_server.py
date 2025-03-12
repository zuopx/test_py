import asyncio


async def handle_client(reader, writer):
    """
    处理客户端连接的协程
    :param reader: asyncio.StreamReader 对象，用于读取客户端数据
    :param writer: asyncio.StreamWriter 对象，用于向客户端写入数据
    """
    client_addr = writer.get_extra_info('peername')
    print(f"客户端 {client_addr} 已连接")

    try:
        while True:
            # 异步读取数据（最大 1024 字节）
            data = await reader.read(1024)
            if not data:
                break

            # 处理接收到的数据
            message = data.decode().strip()
            print(f"收到来自 {client_addr} 的消息: {message}")

            # 回显响应（末尾加换行符）
            response = f"ECHO: {message}\n"
            writer.write(response.encode())
            await writer.drain()  # 确保数据已发送

    except ConnectionResetError:
        print(f"客户端 {client_addr} 异常断开")
    finally:
        print(f"客户端 {client_addr} 断开连接")
        writer.close()
        await writer.wait_closed()


async def main(host='127.0.0.1', port=8888):
    """
    启动 TCP 服务器的主协程
    """
    # 创建 TCP 服务器
    server = await asyncio.start_server(
        handle_client,
        host=host,
        port=port
    )

    # 获取服务器地址信息
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"服务器已启动，监听地址: {addrs}")

    # 永久运行服务器
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n服务器已关闭")
