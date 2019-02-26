import socket


def get_host_ip():
    """
    在windows和unix系统中都可以稳定获取本地ip地址的方法
    :return:
    """

    try:
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        return e
    finally:
        s.close()

    return ip
