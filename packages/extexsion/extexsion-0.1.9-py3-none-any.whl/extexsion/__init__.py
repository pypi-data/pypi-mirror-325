"""
本模块的函数有一大部分都需要管理员权限!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

author:Huang Yi yi

extexsion 模块提供了一系列与系统操作、文件处理、菜单管理等相关的功能。

该模块使用了requests和pywin32和mutagen和wmi和bs4模块,以及Python的标准库

使用示例1：
    from extexsion import attributes
    file_path = 'test.txt'
    result = attributes(file_path,True)#将文件设为隐藏
    print(result)

使用示例2：
    from extexsion import size
    width, height = size()#获取屏幕的宽和高

使用示例3：
    from extexsion import crawl_website
    start_url = "https://example.com"
    base_dir = "D:/test"
    crawl_website(start_url, base_dir)#爬取https://example.com网站,把其中的图片,js,css等都存到一个D:/test的目录里,相对路径也可以
"""
import logging, ctypes


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
__version__ = '0.1.9'

#import ...
from .main import (
    attributes, right_rotate, sha256, filehash, open_url, download,
    system, username, increase, delete, modify, desktop, path, obtain,
    menu_app, add_menu, menu_icon, variable, Systemtime, association, systemkey,
    exvironment, SystemTime, read, read_file, shortcut, add_drivers,
    getregedit, afterdef, driver, winagent, winprohibt, create_process,
    delete_process, backend, split, dirname, copy, copy2, delete_file, filehash,
    ctrlc, curani, size, screenshot, brightness, crawl_page, crawl_website
)


user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32
gdiplus = ctypes.CDLL('gdiplus.dll')


from .main import (
    Path,
)

try:
    from .main import (
        MP3ID3, 
        error, 
        SendEmail,
    )

except Exception as e:
    pass 

"""
width,height = size()
print(width,height)
"""