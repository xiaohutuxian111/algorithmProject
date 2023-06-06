"""
@Author：stone
@Time：2023/6/6 20:36
@Description:
"""
import socket
import asyncio


async def waiter(conn, loop):
    while True:
        try:
            data = await loop.sock_recv(conn, 1024)
            if not data:
                break
            await loop.sock_sendall(conn, data.upper())
        except ConnectionResetError:
            break
    conn.close()


def main(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    loop = asyncio.get_running_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        # 创建task任务
        loop.create_task(waiter(conn, loop))


asyncio.run(main('127.0.0.1',8082))
