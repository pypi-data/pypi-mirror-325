"""
author:Huang Yi yi

extexsion 模块提供了一系列与系统操作、文件处理、菜单管理等相关的功能。

该模块使用了requests和pywin32模块,以及Python的标准库

使用示例：
    from extexsion import attributes
    file_path = 'test.txt'
    result = attributes(file_path,True)#将文件设为隐藏
    print(result)
"""
import logging


def _initialize_module():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('extexsion.log')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_READONLY = 0x1
FILE_ATTRIBUTE_ARCHIVE = 0x20
FILE_ATTRIBUTE_SYSTEM = 0x4
FILE_ATTRIBUTE_COMPRESSED = 0x800
_initialize_module()

#title
__title__ = "extexsion"

#version
__version__ = '0.1.6'

#import ...
from .main import (
    attributes, right_rotate, sha256, file_hash, open_url, download,
    system, username, increase, delete, modify, desktop, path, _test, obtain,
    menu_app, add_menu, menu_icon, variable, Systemtime, association, systemkey,
    way, exvironment, SystemTime, read, read_file, shortcut, add_drivers,
    getregedit, afterdef, driver, winagent, winprohibt, create_process,
    delete_process, backend, split
)


from .main import Path


if __name__ == '__main__':
    _test()