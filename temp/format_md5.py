import hashlib


def format_md5(string):
    """
    通过hashlib的md5方法对字符串进行加密
    这是一个单向加密的方法
    :param string:
    :return: 返回加密后的十六进制结果
    """
    m = hashlib.md5()
    if not string:
        string = u''
    m.update(string.encode(encoding='utf-8'))
    return m.hexdigest()
