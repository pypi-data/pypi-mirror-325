import os, ctypes, logging
from . import system

def desktop():
    """获取桌面位置(Desktop)"""
    return os.path.join(os.path.expanduser("~"), "Desktop")


def getcwd():
    """get? 获取当前工作目录"""
    if system() == 'Windows':
        kernel32 = ctypes.WinDLL('kernel32')
        buffer = ctypes.create_unicode_buffer(260)
        kernel32.GetCurrentDirectoryW(260, buffer)
        return buffer.value
        
    else:  # Unix/Linux
        libc = ctypes.CDLL(ctypes.util.find_library('c'))
        buffer = ctypes.create_string_buffer(4096)
        libc.getcwd(buffer, 4096)
        return buffer.value.decode('utf-8')
    

def montage(*paths):
    """拼接路径"""
    sep = os.sep
    # 处理 Windows 系统下路径的特殊字符
    seps = os.altsep or sep
    colon = ':'

    result_drive = ''
    result_path = ''

    for path in paths:
        if not path:
            continue
        # 处理驱动器号和路径部分
        drive, path_part = os.path.splitdrive(path)

        if path_part and path_part[0] in seps:
            # 如果当前路径是绝对路径
            if drive or not result_drive:
                result_drive = drive
            result_path = path_part
        elif drive and drive != result_drive:
            if drive.lower() != result_drive.lower():
                # 不同的驱动器，忽略之前的路径
                result_drive = drive
                result_path = path_part
            else:
                # 相同驱动器但大小写不同
                result_drive = drive
        else:
            # 当前路径是相对路径
            if result_path and result_path[-1] not in seps:
                result_path += sep
            result_path += path_part

    # 处理 UNC 路径和非绝对路径之间的分隔符
    if result_path and result_path[0] not in seps and result_drive and result_drive[-1:] != colon:
        return result_drive + sep + result_path
    return result_drive + result_path


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sdb(path, windows_disallowed=None, unix_disallowed=None):
    try:
        if os.name == 'nt':  # Windows 系统
            if windows_disallowed is None:
                disallowed_chars = '<>:"/\\|?*'
            else:
                disallowed_chars = windows_disallowed
        elif os.name == 'posix':  # 类 Unix 系统（包括 macOS 和 Linux）
            if unix_disallowed is None:
                disallowed_chars = '/'
            else:
                disallowed_chars = unix_disallowed
        else:
            logging.warning(f"不支持的操作系统: {os.name}，将使用默认的类 Unix 规则。")
            if unix_disallowed is None:
                disallowed_chars = '/'
            else:
                disallowed_chars = unix_disallowed

        result = ''
        for char in path:
            if char not in disallowed_chars:
                result += char
        return result
    except Exception as e:
        logging.error(f"处理路径时出现错误: {e}")
        return path