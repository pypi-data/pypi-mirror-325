"""
注意!使用此模块时有很多函数需要管理员权限!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def admin():
    #判断有没有管理员权限
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
else:
    #代码

"""

import wmi
import bz2
import gzip
import time
import lzma
import py7zr
import shutil
import winreg
import ctypes
import sys, os
import inspect
import tarfile
import zipfile
import hashlib
import logging
import win32gui
import win32con
import win32api
import requests
import subprocess
import win32clipboard
from pyunpack import Archive
from ctypes import wintypes
from bs4 import BeautifulSoup
from win32com.client import Dispatch
from urllib.parse import urljoin, urlparse
from mutagen.id3 import ID3, TIT2, TPE1, TALB


FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_READONLY = 0x1
FILE_ATTRIBUTE_ARCHIVE = 0x20
FILE_ATTRIBUTE_SYSTEM = 0x4
FILE_ATTRIBUTE_COMPRESSED = 0x800


def attributes(file_path, hidden=False, readonly=False, archive=False, system=False, compressed=False):
    """
    设置指定文件的属性为隐藏、只读、存档、系统或压缩
    :param file_path: 文件路径
    :param hidden: 是否设置为隐藏，默认为False
    :param readonly: 是否设置为只读，默认为False
    :param archive: 是否设置为存档，默认为False
    :param system: 是否设置为系统，默认为False
    :param compressed: 是否设置为压缩，默认为False
    """
    if os.name == 'nt':
        if os.path.exists(file_path):
            # 获取当前文件属性
            attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            
            # 根据参数设置属性
            if hidden:
                attributes |= FILE_ATTRIBUTE_HIDDEN
            else:
                attributes &= ~FILE_ATTRIBUTE_HIDDEN
            
            if readonly:
                attributes |= FILE_ATTRIBUTE_READONLY
            else:
                attributes &= ~FILE_ATTRIBUTE_READONLY
            
            if archive:
                attributes |= FILE_ATTRIBUTE_ARCHIVE
            else:
                attributes &= ~FILE_ATTRIBUTE_ARCHIVE
            
            if system:
                attributes |= FILE_ATTRIBUTE_SYSTEM
            else:
                attributes &= ~FILE_ATTRIBUTE_SYSTEM
            
            if compressed:
                attributes |= FILE_ATTRIBUTE_COMPRESSED
            else:
                attributes &= ~FILE_ATTRIBUTE_COMPRESSED
            
            # 更新文件属性
            ctypes.windll.kernel32.SetFileAttributesW(file_path, attributes)
        else:
            raise SIONValueError('attributes Error: 我没找着文件啊!')

    else:
        print('attributes: 此功能只支持Windows系统! ')


# 初始常量
K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

def right_rotate(x, n):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def sha256(message):
        # 预处理
        original_byte_len = len(message)
        message += b'\x80'
        message += b'\x00' * ((55 - original_byte_len % 64) % 64)
        message += (original_byte_len * 8).to_bytes(8, 'big')

        # 分块处理
        chunks = [message[i:i+64] for i in range(0, len(message), 64)]
        for chunk in chunks:
            w = [0] * 64
            for i in range(16):
                w[i] = int.from_bytes(chunk[i*4:i*4+4], 'big')
            for i in range(16, 64):
                s0 = right_rotate(w[i-15], 7) ^ right_rotate(w[i-15], 18) ^ (w[i-15] >> 3)
                s1 = right_rotate(w[i-2], 17) ^ right_rotate(w[i-2], 19) ^ (w[i-2] >> 10)
                w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

            a, b, c, d, e, f, g, h = H

            for i in range(64):
                S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
                ch = (e & f) ^ ((~e) & g)
                temp1 = (h + S1 + ch + K[i] + w[i]) & 0xFFFFFFFF
                S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) & 0xFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFF

            H[0] = (H[0] + a) & 0xFFFFFFFF
            H[1] = (H[1] + b) & 0xFFFFFFFF
            H[2] = (H[2] + c) & 0xFFFFFFFF
            H[3] = (H[3] + d) & 0xFFFFFFFF
            H[4] = (H[4] + e) & 0xFFFFFFFF
            H[5] = (H[5] + f) & 0xFFFFFFFF
            H[6] = (H[6] + g) & 0xFFFFFFFF
            H[7] = (H[7] + h) & 0xFFFFFFFF

        # 生成最终结果
        result = b''
        for h in H:
            result += h.to_bytes(4, 'big')
        return result.hex()
    
def filehash(file_path):
        """
        计算给定文件的自定义哈希值
        :param file_path: 文件路径
        :return: 自定义哈希值
        """
        try:
            with open(file_path, 'rb') as f:
                # 读取文件的所有内容
                file_data = f.read()
                # 计算自定义哈希值
                hash_value = sha256(file_data)
            return hash_value
        except Exception as e:
            raise SIONValueError('filehash Error:',e)
            return None


def open_url(url = '',browser = 'msedge'):
    """
    对应不同的操作系统打开浏览器和url
    url:url
    如果url为空那就打开浏览器主页.
    browser:使用的浏览器,默认msedge(Edge).可以自己切换,
    比如firefox,chrome等,不过你得确认你有没有安装这个浏览器!(browser也是执行的文件名)(Edge测试正常).
    如果你把默认的浏览器改成空,那他就会打开用户主页.
    """
    if system() == 'Windows':
        try:
            subprocess.run(["start", browser, url], shell=True)

        except Exception as e:
            raise SIONTypeError('open_url Error:',e)

    elif system() == 'macOS':
        try:
            if browser == 'msedge':
                #Microsoft Edge
                subprocess.run(["open", "-a", "Microsoft Edge", url])
            else:
                subprocess.run(["open", "-a", "Safari", url])  # 替换为相应浏览器
        except Exception as e:
            raise SIONTypeError('open_url Error:',e)

    elif system() == 'Linux':
        try:
            if browser == 'msedge':
                #microsoft-edge
                subprocess.run(["microsoft-edge", url])
            else:
                subprocess.run(["xdg-open", url])  # xdg-open 是在大多数 Linux 发行版中使用的命令
        except Exception as e:
            raise SIONTypeError('open_url Error:',e)


def download(url, destination, Savelocation,
              Sen = 'get'):
    """
    在互联网上下载文件
    url:下载链接
    destination:下载完成后的名字
    Savelocation:保存位置
    Sen:发送方式,可填'get'和'post',默认get.
    """
    try:
        os.chdir(Savelocation)
        if Sen == 'get':
            response = requests.get(url, stream=True)

        if Sen == 'post':
            response = requests.post(url, stream=True)

        else:
            response = requests.get(url, stream=True)

        response.raise_for_status()

        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

    except Exception as e:
        raise SIONTypeError('download Error:',e)


def system(none = None):
    """通过调用系统命令识别操作系统"""
    if none == None:
        try:
            result = subprocess.run("ver", capture_output=True, text=True, shell=True)
            if "Microsoft" in result.stdout:
                return "Windows"
            
            result = subprocess.run("uname", capture_output=True, text=True, shell=True)
            if "Darwin" in result.stdout:
                return "macOS"
            
            result = subprocess.run("uname", capture_output=True, text=True, shell=True)
            if "Linux" in result.stdout:
                return "Linux"
            
        except Exception as e:
            return f"发生错误: {e}"

        return "未知操作系统"

    else:
        return none


def username():
    """获取用户名"""

    if system() == "Windows":
        return os.getenv("USERNAME")

    else:
        return os.getenv("USER")


def increase(file_extension=None, file_type=None, icon_path=None, associated_program=None):
    """
    :param file_extension 自定义后缀名
    :param file_type 自定义文件类型名称
    :param icon_path 图标文件路径，确保图标文件存在
    :param associated_program 关联的程序路径
    """
    if all(arg is None for arg in [file_extension, file_type, icon_path, associated_program]):
        print("Error: 至少需要提供一个参数")
        return

    try:
        if system() == 'Windows':
            try:
                if file_type:
                    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_type)
                    winreg.SetValue(key, "", winreg.REG_SZ, "Custom File")

                if icon_path and file_type:
                    icon_key = winreg.CreateKey(key, "DefaultIcon")
                    winreg.SetValue(icon_key, "", winreg.REG_SZ, icon_path)

                if associated_program and file_type:
                    shell_key = winreg.CreateKey(key, r"shell\open\command")
                    winreg.SetValue(shell_key, "", winreg.REG_SZ, f'"{associated_program}" "%1"')

                if file_extension and file_type:
                    ext_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_extension)
                    winreg.SetValue(ext_key, "", winreg.REG_SZ, file_type)

            except Exception as e:
                print(f"Error: {e}")
            finally:
                if 'key' in locals():
                    winreg.CloseKey(key)
                if 'icon_key' in locals():
                    winreg.CloseKey(icon_key)
                if 'shell_key' in locals():
                    winreg.CloseKey(shell_key)
                if 'ext_key' in locals():
                    winreg.CloseKey(ext_key)
        elif system() == 'macOS':
            # 使用duti命令设置文件关联
            if file_extension and associated_program:
                try:
                    subprocess.run(["duti", "-s", associated_program, file_extension], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
        elif system() == 'Linux':
            # 修改~/.local/share/applications/mimeapps.list文件来设置文件关联
            if file_extension and associated_program:
                mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{file_extension}'], capture_output=True, text=True).stdout.strip()
                try:
                    with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'a') as f:
                        f.write(f'[Default Applications]\n{mime_type}={associated_program}\n')
                except Exception as e:
                    print(f"Error: {e}")

    except Exception as e:
        raise SIONValueError('increase Error:',e)


def delete(file_extension, file_type):
    """
    删除文件扩展名关联的函数
    :param file_extension: 要删除关联的文件扩展名
    :param file_type: 要删除关联的文件类型
    """
    if system() == 'Windows':
        try:
            # 先删除文件扩展名的关联
            try:
                ext_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_extension, 0, winreg.KEY_ALL_ACCESS)
                winreg.DeleteKey(ext_key, "")
                winreg.CloseKey(ext_key)
            except FileNotFoundError:
                pass  # 如果扩展名关联不存在，忽略错误

            # 再删除文件类型的关联
            try:
                key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_type, 0, winreg.KEY_ALL_ACCESS)
                winreg.DeleteKey(key, "")
                winreg.CloseKey(key)
            except FileNotFoundError:
                raise SIONValueError('delete Error: 文件不存在')

        except Exception as e:
            print(f"Error: {e}")
    elif system() == 'macOS':
        # 使用duti命令删除文件关联
        if file_extension:
            try:
                subprocess.run(["duti", "-d", file_extension], check=True)
            except subprocess.CalledProcessError as e:
                raise SIONValueError('delete Error:',e)
    elif system() == 'Linux':
        # 修改~/.local/share/applications/mimeapps.list文件来删除文件关联
        if file_extension:
            mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{file_extension}'], capture_output=True, text=True).stdout.strip()
            try:
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'r') as f:
                    lines = f.readlines()
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{mime_type}='):
                            f.write(line)
            except Exception as e:
                raise SIONValueError('delete Error:',e)


def modify(old_file_extension=None, old_file_type=None, new_file_extension=None, new_file_type=None,
           new_icon_path=None, new_associated_program=None):
    """修改 文件后缀名的关联 """
    # 检查是否至少提供了一个新参数
    new_params = [new_file_extension, new_file_type, new_icon_path, new_associated_program]
    if all(arg is None for arg in new_params):
        print("Error: 至少需要提供一个新参数进行修改")
        return

    if system() == 'Windows':
        try:
            # 先删除旧的关联
            if old_file_extension and old_file_type:
                try:
                    ext_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, old_file_extension, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(ext_key, "")
                    winreg.CloseKey(ext_key)
                except FileNotFoundError:
                    pass

                try:
                    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, old_file_type, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(key, "")
                    winreg.CloseKey(key)
                except FileNotFoundError:
                    pass

            # 再增加新的关联
            increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)

        except Exception as e:
            raise SIONValueError('modify Error:',e)
    elif system() == 'macOS':
        # 先删除旧的关联
        if old_file_extension:
            try:
                subprocess.run(["duti", "-d", old_file_extension], check=True)
            except subprocess.CalledProcessError as e:
                raise SIONValueError('modify Error:',e)
        # 再增加新的关联
        increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)
    elif system() == 'Linux':
        # 先删除旧的关联
        if old_file_extension:
            mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{old_file_extension}'], capture_output=True, text=True).stdout.strip()
            try:
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'r') as f:
                    lines = f.readlines()
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{mime_type}='):
                            f.write(line)
            except Exception as e:
                raise SIONValueError('modify Error:',e)
        # 再增加新的关联
        increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)


def desktop():
    """获取桌面位置(Desktop)"""
    return os.path.join(os.path.expanduser("~"), "Desktop")


def path(path):
    # 首先判断传入的路径是否已经是绝对路径
    if os.path.isabs(path):
        return path
    else:
        # 如果是相对路径，获取当前工作目录
        current_working_directory = os.getcwd()
        # 使用 os.path.join() 函数将当前工作目录和相对路径拼接起来
        absolute_path = os.path.join(current_working_directory, path)
        # 对拼接后的路径进行规范化处理，处理路径中的.、.. 等符号
        normalized_path = os.path.normpath(absolute_path)

        return normalized_path


def _test():
    try:
        file = path('APK_file.exe')
        backend(file)
        file_extension = ".testext"
        file_type = "TestFile"
        associated_program = r"C:\Windows\explorer.exe"

        def admin():
            """判断有没有管理员权限"""
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if not admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        
        else:
            increase(file_extension, file_type, associated_program=associated_program)

            os.chdir(desktop())
            with open('.testext','w',encoding='utf-8') as f:
                    f.write('Extexsion')

            print(f'已成功创建 ".testext" 文件后缀名，已创建 .testext 文件，路径：{desktop()}')

            time.sleep(10)

            os.remove(desktop()+r'\.testext')

            print('已删除 .testext 文件。')

            delete(file_extension, file_type)

    except Exception as e:
        raise SIONError('_test Error:',e)


def obtain():
    """
    通过查看注册表获取系统中所有的文件后缀名
    :return: 包含所有文件后缀名的列表
    """
    file_extensions = []
    try:
        # 打开HKEY_CLASSES_ROOT注册表根键
        root_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT)
        # 枚举HKEY_CLASSES_ROOT下的所有子键
        index = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(root_key, index)
                # 检查子键名是否以'.'开头，若是则为文件后缀名
                if subkey_name.startswith('.'):
                    file_extensions.append(subkey_name)
                index += 1
            except OSError:
                # 枚举结束
                break
        # 关闭注册表键
        winreg.CloseKey(root_key)
    except Exception as e:
        raise SIONKeyError('obtain Error:',e)
    return file_extensions


def menu_app(entry_name, exe_path):
    """
    在桌面右键菜单中添加一个新的菜单项，点击该菜单项会直接打开指定的 exe 程序。

    :param entry_name: 菜单项的显示名称
    :param exe_path: 要打开的 exe 程序的路径
    """
    try:
        # 打开桌面右键菜单的注册表项
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"Directory\Background\shell", 0, winreg.KEY_WRITE)

        # 创建一个新的子项，用于我们的菜单项
        new_key = winreg.CreateKey(key, entry_name)

        # 设置菜单项的显示名称
        winreg.SetValue(new_key, "", winreg.REG_SZ, entry_name)

        # 创建一个子项，用于指定菜单项点击后要执行的命令
        command_key = winreg.CreateKey(new_key, "command")
        # 这里需要注意，命令需要使用双引号括起来，以处理路径中可能包含的空格
        winreg.SetValue(command_key, "", winreg.REG_SZ, f'"{exe_path}"')

        # 关闭注册表项
        winreg.CloseKey(command_key)
        winreg.CloseKey(new_key)
        winreg.CloseKey(key)

    except Exception as e:
        raise SIONKeyError('menu_app Error:',e)


def add_menu(file_extension, file_description):
    """
    将自定义文件类型添加到桌面右键菜单的“新建”选项中。

    :param file_extension: 文件扩展名，例如 ".py"
    :param file_description: 文件描述，例如 "Python File"
    """
    try:
        # 打开 HKEY_CLASSES_ROOT 根键
        root_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_extension, 0, winreg.KEY_ALL_ACCESS)

        # 设置文件类型描述
        winreg.SetValue(root_key, "", winreg.REG_SZ, file_description)

        # 创建 ShellNew 子键
        shell_new_key = winreg.CreateKey(root_key, "ShellNew")

        # 设置 ShellNew 子键的默认值为空字符串
        winreg.SetValue(shell_new_key, "", winreg.REG_SZ, "")

        # 设置 NullFile 键，告诉系统创建一个空文件
        winreg.SetValue(shell_new_key, "NullFile", winreg.REG_SZ, "")

        # 关闭注册表键
        winreg.CloseKey(shell_new_key)
        winreg.CloseKey(root_key)

    except Exception as e:
        raise SIONKeyError('add_menu Error:',e)


def menu_icon(menu_key_name, icon_path):
    """
    修改或添加 Windows 右键菜单项的图标
    :param menu_key_name: 菜单项在注册表中的键名
    :param icon_path: 图标文件的路径
    """
    try:
        # 打开 HKEY_CLASSES_ROOT\*\shell 注册表项，这是文件右键菜单的位置
        # 如果是文件夹右键菜单，可将 * 替换为 Directory
        root_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell", 0, winreg.KEY_ALL_ACCESS)
        try:
            # 尝试打开指定的菜单项键
            menu_key = winreg.OpenKey(root_key, menu_key_name, 0, winreg.KEY_ALL_ACCESS)
            # 设置或修改 Icon 值为指定的图标路径
            winreg.SetValueEx(menu_key, "Icon", 0, winreg.REG_SZ, icon_path)
        except FileNotFoundError:
            print(f"未找到 {menu_key_name} 菜单项对应的注册表键。")
        finally:
            if 'menu_key' in locals():
                winreg.CloseKey(menu_key)
        winreg.CloseKey(root_key)
    except Exception as e:
        raise SIONKeyError('menu_icon Error:',e)


def variable(variable, value):
    """环境变量"""
    try:
        # 打开环境变量所在的注册表项
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Environment", 0, winreg.KEY_ALL_ACCESS)
        # 设置环境变量的值
        winreg.SetValueEx(key, variable, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        #print(f"环境变量 {variable} 已设置为 {value}")
    except Exception as e:
        raise SIONValueError('variable Error:',e)
        

def Systemtime(wYear, wMonth, wDay, wHour, wMinute, wSecond, wMilliseconds):
    global SYSTEMTIME
    # 定义 SYSTEMTIME 结构体
    class SYSTEMTIME(ctypes.Structure):
        _fields_ = [
            ("wYear", wintypes.WORD),
            ("wMonth", wintypes.WORD),
            ("wDayOfWeek", wintypes.WORD),
            ("wDay", wintypes.WORD),
            ("wHour", wintypes.WORD),
            ("wMinute", wintypes.WORD),
            ("wSecond", wintypes.WORD),
            ("wMilliseconds", wintypes.WORD)
        ]

    # 加载 kernel32.dll 库
    kernel32 = ctypes.windll.kernel32
    # 获取 SetSystemTime 函数
    SetSystemTime = kernel32.SetSystemTime
    SetSystemTime.argtypes = [ctypes.POINTER(SYSTEMTIME)]
    SetSystemTime.restype = wintypes.BOOL


    # 设置新的系统时间
    new_time = SYSTEMTIME()
    new_time.wYear = wYear
    new_time.wMonth = wMonth
    new_time.wDay = wDay
    new_time.wHour = wHour
    new_time.wMinute = wMinute
    new_time.wSecond = wSecond
    new_time.wMilliseconds = wMilliseconds

    # 调用 SetSystemTime 函数
    if SetSystemTime(ctypes.byref(new_time)):
        pass
    else:
        raise SIONValueError('Systemtime Error')


def association(file_extension, program_path):
    """将指定的 文件关联的后缀名 关联到指定的程序"""
    try:
        # 打开 .txt 文件关联的注册表项
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                               fr"Software\Classes\{file_extension}")
        # 设置默认值为自定义的文件类型名称
        winreg.SetValue(key, "", winreg.REG_SZ, "MyTextFile")
        winreg.CloseKey(key)

        # 打开自定义文件类型的注册表项
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                               r"Software\Classes\MyTextFile\shell\open\command")
        # 设置默认值为要关联的程序路径
        winreg.SetValue(key, "", winreg.REG_SZ, f'"{program_path}" "%1"')
        winreg.CloseKey(key)

    except Exception as e:
        raise SIONValueError('association Error:',e)

"""set_file_association(".txt", r"C:\Windows\System32\notepad.exe")"""


def systemkey():
    """Windows 系统密钥"""
    global GUID
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

    # 加载 wbemcli.dll 库
    wbemcli = ctypes.windll.wbemcli

    # 定义函数原型
    wbemcli.WBEMInitializeNamespace.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPVOID]
    wbemcli.WBEMInitializeNamespace.restype = wintypes.HRESULT

    wbemcli.WBEMConnectServer.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPVOID]
    wbemcli.WBEMConnectServer.restype = wintypes.HRESULT

    wbemcli.WBEMExecQuery.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPVOID]
    wbemcli.WBEMExecQuery.restype = wintypes.HRESULT

    wbemcli.WBEMGetObject.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.LPVOID]
    wbemcli.WBEMGetObject.restype = wintypes.HRESULT

    wbemcli.WBEMRelease.argtypes = [wintypes.LPVOID]
    wbemcli.WBEMRelease.restype = wintypes.HRESULT

    # 初始化 COM 库
    ctypes.windll.ole32.CoInitialize(None)

    # 初始化 WMI 命名空间
    wbem_svc = wintypes.LPVOID()
    wbemcli.WBEMInitializeNamespace(None, r"\\.\root\cimv2", None, None, None, None, None, ctypes.byref(wbem_svc))

    # 连接到 WMI 服务
    wbemcli.WBEMConnectServer(None, r"\\.\root\cimv2", None, None, None, None, None, ctypes.byref(wbem_svc))

    # 执行查询
    wbem_enum = wintypes.LPVOID()
    wbemcli.WBEMExecQuery(wbem_svc, "WQL", "SELECT * FROM SoftwareLicensingService", None, None, ctypes.byref(wbem_enum))

    # 获取对象
    wbem_obj = wintypes.LPVOID()
    wbemcli.WBEMGetObject(wbem_enum, 0, None, ctypes.byref(wbem_obj))

    # 获取产品密钥
    product_key = wintypes.LPWSTR()
    wbemcli.WBEMGetObjectText(wbem_obj, 1, ctypes.byref(product_key))

    # 释放资源
    wbemcli.WBEMRelease(wbem_obj)
    wbemcli.WBEMRelease(wbem_enum)
    wbemcli.WBEMRelease(wbem_svc)

    # 释放 COM 库
    ctypes.windll.ole32.CoUninitialize()

    return product_key.value


def exvironment():
    kernel32 = ctypes.windll.kernel32

    # 获取环境变量块的大小
    buf_size = kernel32.GetEnvironmentStringsLengthW()

    # 分配内存
    buf = ctypes.create_unicode_buffer(buf_size)

    # 获取环境变量块
    kernel32.GetEnvironmentStringsW(ctypes.byref(buf))

    # 解析环境变量
    env_vars = {}
    i = 0
    while buf[i]:
        var_name = ""
        var_value = ""
        while buf[i] and buf[i] != '=':
            var_name += buf[i]
            i += 1
        i += 1
        while buf[i]:
            var_value += buf[i]
            i += 1
        env_vars[var_name] = var_value
        i += 1

    # 打印环境变量
    for var_name, var_value in env_vars.items():
        return var_name , var_value


def SystemTime():
    """系统时间"""
    # 定义 SYSTEMTIMES 结构体
    class SYSTEMTIMES(ctypes.Structure):
        _fields_ = [
            ("wYear", wintypes.WORD),
            ("wMonth", wintypes.WORD),
            ("wDayOfWeek", wintypes.WORD),
            ("wDay", wintypes.WORD),
            ("wHour", wintypes.WORD),
            ("wMinute", wintypes.WORD),
            ("wSecond", wintypes.WORD),
            ("wMilliseconds", wintypes.WORD)
        ]

    # 加载 kernel32.dll 库
    kernel32 = ctypes.windll.kernel32
    # 获取 GetSystemTime 函数
    GetSystemTime = kernel32.GetSystemTime
    GetSystemTime.argtypes = [ctypes.POINTER(SYSTEMTIMES)]

    # 创建 SYSTEMTIME 结构体实例
    system_time = SYSTEMTIMES()
    # 调用 GetSystemTime 函数
    GetSystemTime(ctypes.byref(system_time))

    formatted_time = f"{system_time.wYear}-{system_time.wMonth:02d}-{system_time.wDay:02d} {system_time.wHour:02d}:{system_time.wMinute:02d}:{system_time.wSecond:02d}"

    return formatted_time


def read(file_extension, file_path):
    """
    读取指定后缀名的文件内容
    :param file_extension: 文件后缀名，例如 ".txt"
    :param file_path: 文件路径
    :return: 文件内容，如果文件不存在或读取失败则返回 None
    """
    try:
        # 检查文件路径是否以指定后缀名结尾
        if file_path.endswith(file_extension):
            with open(file_path, 'r', encoding='utf-8') as file:
                # 读取文件内容
                content = file.read()
                return content
        else:
            #print(f"文件路径 {file_path} 不是以 {file_extension} 后缀名结尾。")
            return None
    except FileNotFoundError:
        raise SIONValueError('read Error: 不对啊,没找着文件啊!')
        return None
    except Exception as e:
        raise SIONValueError('read Error:',e)
        return None


def read_file(file_extension):
    """
    读取指定后缀名的文件的绝对路径
    :param file_extension: 文件后缀名，例如 ".txt"
    :return: 文件的绝对路径，如果文件后缀名不匹配则返回 None
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path.endswith(file_extension):
            absolute_path = os.path.abspath(file_path)
            return absolute_path
        else:
            print("文件后缀名不匹配")
    else:
        print("没有传递文件路径参数")
    return None


def shortcut(target_path, shortcut_path, run_as_admin=False):
    """
    创建指定文件的快捷方式
    :param target_path: 目标文件路径
    :param shortcut_path: 快捷方式保存路径
    :param run_as_admin: 是否以管理员权限运行，默认为False
    """
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    if run_as_admin:
        # 设置快捷方式以管理员权限运行
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        shortcut.RunAsAdmin = True
    shortcut.save()


def add_drivers(exe_path, icon_path, display_name, GUID = "{20D04FE0-3AEA-1069-A2D8-08002B30309D}"):
    """
    在（设备和驱动器）页面增加图标，点击图标进入指定的exe程序
    :param exe_path: 指定的exe程序的路径
    :param icon_path: 图标文件的路径
    :param display_name: 显示的名称
    :param GUID:GUID
    """
    try:
        # 打开注册表的特定键
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace", 0, winreg.KEY_WRITE)

        new_guid = GUID

        # 创建新的子键
        new_key = winreg.CreateKey(key, new_guid)

        # 设置子键的默认值为显示名称
        winreg.SetValueEx(new_key, "", 0, winreg.REG_SZ, display_name)

        # 设置图标路径
        winreg.SetValueEx(new_key, "DefaultIcon", 0, winreg.REG_SZ, icon_path)

        # 设置命令，点击图标时执行的程序
        winreg.SetValueEx(new_key, "Command", 0, winreg.REG_SZ, exe_path)

        # 关闭注册表键
        winreg.CloseKey(new_key)
        winreg.CloseKey(key)

    except Exception as e:
        raise SIONKeyError('add_drivers Error:',e)


def getregedit(root_key, sub_key, target_name, target_value):
    """
    自动查找注册表，直到找到一个选定的值和名称
    :param root_key: 根键，例如 winreg.HKEY_CURRENT_USER 或 winreg.HKEY_LOCAL_MACHINE
    :param sub_key: 子键路径，例如 "Software\\Microsoft"
    :param target_name: 要查找的名称
    :param target_value: 要查找的值
    :return: 如果找到则返回对应的键对象，否则返回 None
    """
    try:
        # 打开指定的注册表键
        key = winreg.OpenKey(root_key, sub_key)
        index = 0
        while True:
            try:
                # 枚举子键
                sub_key_name = winreg.EnumKey(key, index)
                sub_key_path = f"{sub_key}\\{sub_key_name}"
                # 递归调用函数查找子键
                result = getregedit(root_key, sub_key_path, target_name, target_value)
                if result:
                    return result
                index += 1
            except OSError:
                # 没有更多子键，开始枚举值
                break
        
        index = 0
        while True:
            try:
                # 枚举值
                name, value, _ = winreg.EnumValue(key, index)
                if name == target_name and value == target_value:
                    return key
                index += 1
            except OSError:
                # 没有更多值，退出循环
                break
        
        # 关闭当前键
        winreg.CloseKey(key)
        return None
    except Exception as e:
        raise SIONKeyError('getregedit Error:',e)
        return None


def afterdef(func):
    """
    获取函数的参数信息
    :param func: 要获取参数信息的函数
    :return: 包含参数信息的字典
    """
    sig = inspect.signature(func)
    parameters = sig.parameters
    param_info = {}
    for name, param in parameters.items():
        param_info[name] = {
            'default': param.default if param.default is not inspect.Parameter.empty else None,
            'kind': param.kind.name
        }
    return param_info


def driver():
    # 调用Windows API函数GetLogicalDrives
    drive_bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    count = 0
    # 遍历所有可能的驱动器字母
    for i in range(26):
        # 检查当前位是否为1，如果为1表示该驱动器存在
        if drive_bitmask & (1 << i):
            count += 1
    return count


def winagent(proxy_server, proxy_port):
    """
    设置系统代理
    :param proxy_server:服务器地址
    :param proxy_port:端口
    """
    try:
        # 打开注册表项
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                             0, winreg.KEY_ALL_ACCESS)

        proxy_str = f"{proxy_server}:{proxy_port}"
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy_str)

        # 启用代理
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)

        # 关闭注册表项
        winreg.CloseKey(key)


    except PermissionError:
        raise SIONValueError('winagent Error: 没有权限搞不了.')

    except Exception as e:
        raise SIONValueError('winagent Error:',e)


def winprohibt():
    """禁用系统代理"""
    try:
        # 打开注册表项
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                             0, winreg.KEY_ALL_ACCESS)

        # 禁用代理
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)

        # 关闭注册表项
        winreg.CloseKey(key)

    except Exception as e:
        raise SIONValueError('winprohibt Error:')


kernel32 = ctypes.windll.kernel32

# 定义 STARTUPINFO 结构体
class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ('cb', ctypes.c_ulong),
        ('lpReserved', ctypes.c_char_p),
        ('lpDesktop', ctypes.c_char_p),
        ('lpTitle', ctypes.c_char_p),
        ('dwX', ctypes.c_ulong),
        ('dwY', ctypes.c_ulong),
        ('dwXSize', ctypes.c_ulong),
        ('dwYSize', ctypes.c_ulong),
        ('dwXCountChars', ctypes.c_ulong),
        ('dwYCountChars', ctypes.c_ulong),
        ('dwFillAttribute', ctypes.c_ulong),
        ('dwFlags', ctypes.c_ulong),
        ('wShowWindow', ctypes.c_short),
        ('cbReserved2', ctypes.c_short),
        ('lpReserved2', ctypes.c_char_p),
        ('hStdInput', ctypes.c_void_p),
        ('hStdOutput', ctypes.c_void_p),
        ('hStdError', ctypes.c_void_p)
    ]

# 定义 PROCESS_INFORMATION 结构体
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('hProcess', ctypes.c_void_p),
        ('hThread', ctypes.c_void_p),
        ('dwProcessId', ctypes.c_ulong),
        ('dwThreadId', ctypes.c_ulong)
    ]

# 调用 CreateProcess 函数创建新进程
def create_process(command):
    """
    创建新进程,(只能exe程序)
    pi.dwProcessId = pid
    """
    global kernel32, pi
    si = STARTUPINFO()
    si.cb = ctypes.sizeof(si)
    pi = PROCESS_INFORMATION()

    # 调用 CreateProcess 函数
    result = kernel32.CreateProcessW(
        None,  # 可执行文件路径（这里为 None 表示从命令中解析）
        command,  # 命令行参数
        None,  # 进程安全属性
        None,  # 线程安全属性
        False,  # 是否继承句柄
        0,  # 创建标志
        None,  # 环境变量
        None,  # 当前目录
        ctypes.byref(si),  # STARTUPINFO 结构体指针
        ctypes.byref(pi)  # PROCESS_INFORMATION 结构体指针
    )

    if result:
        return pi
    
    else:
        print("Not process ERROR!")
        sys.exit()


def delete_process(pid):
    """
    终止进程
    需要管理员权限
    :param pid:pid
    """
    # 打开进程
    try:
        process_handle = kernel32.OpenProcess(0x0400 | 0x0010, False, pid)
        if process_handle:
            # 终止进程
            result = kernel32.TerminateProcess(process_handle, 0)
            if result:
                pass
            else:
                print(f"终止进程 {pid} 失败")
            # 关闭进程句柄
            kernel32.CloseHandle(process_handle)
        else:
            print(f"无法打开进程 {pid}，可能进程不存在")
    except PermissionError:
        raise SIONValueError('delete_process Error: 没权限啊!')


def backend(file):
    """将指定的文件在后台运行"""
    subprocess.Popen(file, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


def split(path):
    if '/' not in path:
        return ('', path)
    last_slash_index = path.rfind('/')
    directory = path[:last_slash_index]
    filename = path[last_slash_index + 1:]
    return (directory, filename)


def dirname(path):
    directory, _ = split(path)
    return directory


def copy(src, dst):
    """
    复制文件
    :param src:源文件
    :param dst:复制后的文件
    """
    try:
        # 复制文件内容
        with open(src, 'rb') as source_file:
            with open(dst, 'wb') as dest_file:
                while True:
                    # 每次读取 4096 字节的数据
                    chunk = source_file.read(4096)
                    if not chunk:
                        break
                    dest_file.write(chunk)

        # 获取源文件的元数据
        src_stat = os.stat(src)
        # 设置目标文件的访问时间和修改时间
        os.utime(dst, (src_stat.st_atime, src_stat.st_mtime))
        # 设置目标文件的权限
        os.chmod(dst, src_stat.st_mode)

    except FileNotFoundError:
        raise SIONValueError('copy Error: 文件路径对不对啊!没有找到.')
    except PermissionError:
        raise SIONValueError('copy Error: 没权限进行复制操作。')
    except Exception as e:
        raise SIONValueError('copy Error:',e)


def delete_file(file_path):
    """删除文件"""
    if system() == 'Windows':
        try:
            # 构建要执行的命令
            command = ['del', file_path]
            # 执行命令
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"删除文件时出错: {e.stderr.strip()}")
        except FileNotFoundError:
            raise SIONValueError('delete_file Error: 文件路径对不对啊!没有找到.')

    else:
        try:
            # 构建要执行的命令
            command = ['rm', file_path]
            # 执行命令
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            raise SIONValueError('delete_file Error:',e)
        except FileNotFoundError:
            raise SIONValueError('delete_file Error: 文件路径对不对啊!没有找到.')


def filehash(file_path):
    """计算文件的哈希值"""
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def copy2(source_file, destination_file, TrueorFalse=False):
    """
    更保险的方式复制文件,且不用管理员权限(如果文件是管理员权限或更高权限复制需要管理员权限)
    :param source_file:源文件路径,例如 "C:/path/to/source.txt"
    :param destination_file:目标文件路径,例如 "C:/path/to/destination.txt"
    :param TrueorFalse:是否覆盖文件,默认不覆盖.False:不覆盖,True:覆盖
    """
    if os.path.exists(destination_file):
        if not TrueorFalse:
            print(f"目标文件 {destination_file} 已存在，且不允许覆盖，跳过复制操作。")
            return

    try:
        source_hash = filehash(source_file)
        temp_file = destination_file + '.tmp'

        chunk_size = 4096
        with open(source_file, 'rb') as src_file:
            with open(temp_file, 'wb') as dest_file:
                while True:
                    chunk = src_file.read(chunk_size)
                    if not chunk:
                        break
                    dest_file.write(chunk)

        temp_hash = filehash(temp_file)

        if source_hash == temp_hash:
            os.replace(temp_file, destination_file)
        else:
            print("文件复制完成，但验证失败：内容不匹配。")
            os.remove(temp_file)

    except FileNotFoundError:
        raise SIONValueError('copy2 Error: 复制失败')
    except PermissionError:
        if os.path.exists(temp_file):
            os.remove(temp_file)

        raise SIONError('copy2 Error: 没有权限')
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)

        raise SIONError('copy2 Error:',e)
    
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)

        raise SIONValueError('copy2 Error:',e)


def ctrlc(text):
    """复制指定的内容"""
    # 打开剪贴板
    win32clipboard.OpenClipboard()
    # 清空剪贴板
    win32clipboard.EmptyClipboard()
    # 将文本以Unicode格式放入剪贴板
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    # 关闭剪贴板
    win32clipboard.CloseClipboard()


def curani(cursor_path):
    """设置鼠标指针(.cur,.ani)"""
    # 加载自定义光标
    hCursor = win32gui.LoadImage(0, cursor_path, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
    if hCursor:
        # 设置全局光标
        win32api.SetSystemCursor(hCursor, win32con.OCR_NORMAL)


def size():
    """获取屏幕分辨率"""
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    return screen_width, screen_height


user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32
gdiplus = ctypes.CDLL('gdiplus.dll')


def screenshot(image_path,format):
    """
    截图
    :param image_path:保存后图片的位置(包含文件名也包含后缀名)
    :param format:要保存的格式
    """
    if system() == 'Windows':
        GdiplusStartupInput = ctypes.Structure(
            _fields_=[
                ('GdiplusVersion', wintypes.UINT),
                ('DebugEventCallback', wintypes.LPVOID),
                ('SuppressBackgroundThread', wintypes.BOOL),
                ('SuppressExternalCodecs', wintypes.BOOL)
            ]
        )
        gdiplusStartupOutput = wintypes.DWORD()
        token = wintypes.DWORD()
        startup_input = GdiplusStartupInput(2, None, 0, 0)
        gdi32 = ctypes.windll.gdi32
        user32 = ctypes.windll.user32
        gdiplus = ctypes.CDLL('gdiplus.dll')
        gdiplus.GdiplusStartup(ctypes.byref(token), ctypes.byref(startup_input), ctypes.byref(gdiplusStartupOutput))

        # 获取屏幕尺寸
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)

        # 获取桌面窗口的设备上下文
        hdcScreen = user32.GetDC(None)
        hdcMemDC = gdi32.CreateCompatibleDC(hdcScreen)

        # 创建位图对象
        hBitmap = gdi32.CreateCompatibleBitmap(hdcScreen, width, height)
        gdi32.SelectObject(hdcMemDC, hBitmap)

        # 拷贝屏幕内容到位图
        gdi32.BitBlt(hdcMemDC, 0, 0, width, height, hdcScreen, 0, 0, 0x00CC0020)

        # 获取位图信息
        class BITMAPINFOHEADER(ctypes.Structure):
            _fields_ = [
                ('biSize', wintypes.DWORD),
                ('biWidth', wintypes.LONG),
                ('biHeight', wintypes.LONG),
                ('biPlanes', wintypes.WORD),
                ('biBitCount', wintypes.WORD),
                ('biCompression', wintypes.DWORD),
                ('biSizeImage', wintypes.DWORD),
                ('biXPelsPerMeter', wintypes.LONG),
                ('biYPelsPerMeter', wintypes.LONG),
                ('biClrUsed', wintypes.DWORD),
                ('biClrImportant', wintypes.DWORD)
            ]

        bmi = BITMAPINFOHEADER()
        bmi.biSize = ctypes.sizeof(BITMAPINFOHEADER)
        bmi.biWidth = width
        bmi.biHeight = -height
        bmi.biPlanes = 1
        bmi.biBitCount = 32
        bmi.biCompression = 0
        bmi.biSizeImage = 0
        bmi.biXPelsPerMeter = 0
        bmi.biYPelsPerMeter = 0
        bmi.biClrUsed = 0
        bmi.biClrImportant = 0

        # 获取位图数据
        buffer_size = width * height * 4
        buffer = ctypes.create_string_buffer(buffer_size)
        gdi32.GetDIBits(hdcMemDC, hBitmap, 0, height, buffer, ctypes.byref(bmi), 0)

        # 创建 GDI+ 位图对象
        Bitmap = gdiplus.GdipCreateBitmapFromScan0
        Bitmap.argtypes = [wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT, wintypes.UINT, ctypes.c_void_p, ctypes.c_void_p]
        Bitmap.restype = wintypes.INT
        hBitmapGdiplus = ctypes.c_void_p()
        Bitmap(width, height, width * 4, 32, 0x00FF0000, buffer, ctypes.byref(hBitmapGdiplus))

        # 定义不同格式的编码器 CLSID
        JPEGEncoder = (ctypes.c_ubyte * 16)(
            0x557CF401, 0x1A04, 0x11D3, 0x9A73, 0x0000F81EF32E
        )
        PNGEncoder = (ctypes.c_ubyte * 16)(
            0x557CF406, 0x1A04, 0x11D3, 0x9A73, 0x0000F81EF32E
        )
        BMPEncoder = (ctypes.c_ubyte * 16)(
            0x557CF400, 0x1A04, 0x11D3, 0x9A73, 0x0000F81EF32E
        )

        GIFEncoder = (ctypes.c_ubyte * 16)(
            0x557CF402, 0x1A04, 0x11D3, 0x9A73, 0x0000F81EF32E
        )

        TIFFEncoder = (ctypes.c_ubyte * 16)(
            0x557CF405, 0x1A04, 0x11D3, 0x9A73, 0x0000F81EF32E
        )

        # 保存为 JPEG 格式
        if format == 'jpg':
            jpeg_path = image_path
            SaveImage = gdiplus.GdipSaveImageToFile
            SaveImage.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p]
            SaveImage.restype = wintypes.INT
            SaveImage(hBitmapGdiplus, jpeg_path, ctypes.byref(JPEGEncoder), None)

        if format == 'jpeg':
            jpeg_path = image_path
            SaveImage = gdiplus.GdipSaveImageToFile
            SaveImage.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p]
            SaveImage.restype = wintypes.INT
            SaveImage(hBitmapGdiplus, jpeg_path, ctypes.byref(JPEGEncoder), None)

        if format == 'png':
            png_path = image_path
            SaveImage(hBitmapGdiplus, png_path, ctypes.byref(PNGEncoder), None)

        if format == 'bmp':
            bmp_path = image_path
            SaveImage(hBitmapGdiplus, bmp_path, ctypes.byref(BMPEncoder), None)

        if format == 'gif':
            gif_path = 'screenshot.gif'
            SaveImage(hBitmapGdiplus, gif_path, ctypes.byref(GIFEncoder), None)

        if format == 'tiff':
            tiff_path = 'screenshot.tiff'
            SaveImage(hBitmapGdiplus, tiff_path, ctypes.byref(TIFFEncoder), None)

        else:
            raise SIONImageError('screenshot Error')

        # 释放资源
        gdi32.DeleteObject(hBitmap)
        gdi32.DeleteDC(hdcMemDC)
        user32.ReleaseDC(None, hdcScreen)
        gdiplus.GdipDisposeImage(hBitmapGdiplus)
        gdiplus.GdiplusShutdown(token)

    else:
        subprocess.run(['screencapture', image_path])


class SendEmail:
    """发邮件"""
    global smtplib, MIMEMultipart, MIMEText, MIMEImage, Header, text, image_attachment, html, image_html
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.header import Header


    def image_attachment(sender, password, receivers, subject, text_content, image_path):
            """
            该函数用于发送带有图片附件的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（不是登录密码，部分邮箱需要开启 SMTP 服务并获取授权码）。
            receivers (list): 收件人的邮箱地址列表，每个元素为一个字符串。
            subject (str): 邮件的主题。
            text_content (str): 邮件的文本正文内容。
            image_path (str): 要作为附件发送的图片文件的本地路径。

            返回:
            None
            """
            try:
                # 创建一个带附件的邮件对象
                message = MIMEMultipart()
                message['Subject'] = Header(subject, 'utf-8')
                message['From'] = Header(sender, 'utf-8')
                message['To'] = Header(", ".join(receivers), 'utf-8')

                # 添加邮件正文
                text_part = MIMEText(text_content, 'plain', 'utf-8')
                message.attach(text_part)

                # 读取图片文件
                with open(image_path, 'rb') as file:
                    # 创建图片附件对象
                    image = MIMEImage(file.read())
                    # 设置附件文件名
                    image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
                    message.attach(image)

                # 连接 SMTP 服务器，这里以常见的端口 587 为例，根据实际邮箱修改服务器地址
                smtpObj = smtplib.SMTP('smtp.example.com', 587)
                # 开启 TLS 加密
                smtpObj.starttls()
                # 登录发件人邮箱
                smtpObj.login(sender, password)
                # 发送邮件
                smtpObj.sendmail(sender, receivers, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                raise SIONError('system Error:',e)
            finally:
                # 关闭 SMTP 连接
                smtpObj.quit()


    def image_html(sender, password, receivers, subject, html_content, image_path):
            """
            该函数用于发送嵌入图片到邮件正文的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（不是登录密码，部分邮箱需要开启 SMTP 服务并获取授权码）。
            receivers (list): 收件人的邮箱地址列表，每个元素为一个字符串。
            subject (str): 邮件的主题。
            html_content (str): 包含 HTML 代码的邮件正文内容，其中需要使用 <img src="cid:image1"> 来引用嵌入的图片。
            image_path (str): 要嵌入到邮件正文中的图片文件的本地路径。

            返回:
            None
            """
            try:
                # 创建一个混合的邮件对象
                message = MIMEMultipart('related')
                message['Subject'] = Header(subject, 'utf-8')
                message['From'] = Header(sender, 'utf-8')
                message['To'] = Header(", ".join(receivers), 'utf-8')

                # 添加 HTML 格式的邮件正文
                html_part = MIMEText(html_content, 'html', 'utf-8')
                message.attach(html_part)

                # 读取图片文件
                with open(image_path, 'rb') as file:
                    # 创建图片对象
                    image = MIMEImage(file.read())
                    # 设置图片的 Content-ID，用于在 HTML 中引用
                    image.add_header('Content-ID', '<image1>')
                    message.attach(image)

                # 连接 SMTP 服务器，这里以常见的端口 587 为例，根据实际邮箱修改服务器地址
                smtpObj = smtplib.SMTP('smtp.example.com', 587)
                # 开启 TLS 加密
                smtpObj.starttls()
                # 登录发件人邮箱
                smtpObj.login(sender, password)
                # 发送邮件
                smtpObj.sendmail(sender, receivers, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                raise SIONError('system Error:',e)
            finally:
                # 关闭 SMTP 连接
                smtpObj.quit()


    def html(sender, password, receivers, subject, html_content, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于发送 HTML 格式的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（部分邮箱需要使用授权码而非登录密码）。
            receivers (list): 收件人的邮箱地址列表，列表中的每个元素为一个字符串形式的邮箱地址。
            subject (str): 邮件的主题，用于在收件人的邮箱列表中标识该邮件的大致内容。
            html_content (str): 邮件的 HTML 格式正文内容，可以包含各种 HTML 标签来实现丰富的排版和样式。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需要根据实际邮箱提供商进行修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587，部分邮箱可能使用其他端口。

            返回:
            None
            """
            try:
                # 创建一个 MIMEMultipart 对象来表示邮件，可包含多种类型的内容
                message = MIMEMultipart()
                # 设置邮件的主题，并使用 Header 处理中文编码
                message['Subject'] = Header(subject, 'utf-8')
                # 设置邮件的发件人，并使用 Header 处理中文编码
                message['From'] = Header(sender, 'utf-8')
                # 设置邮件的收件人，并使用 Header 处理中文编码
                message['To'] = Header(", ".join(receivers), 'utf-8')

                # 创建一个 MIMEText 对象，指定邮件类型为 HTML 格式，并设置编码为 UTF-8
                html_part = MIMEText(html_content, 'html', 'utf-8')
                # 将 HTML 格式的邮件正文添加到邮件对象中
                message.attach(html_part)

                # 连接到指定的 SMTP 服务器和端口
                smtpObj = smtplib.SMTP(smtp_server, smtp_port)
                # 开启 TLS 加密，确保与 SMTP 服务器的通信安全
                smtpObj.starttls()
                # 使用发件人的邮箱地址和授权码登录 SMTP 服务器
                smtpObj.login(sender, password)
                # 发送邮件，将邮件对象转换为字符串形式进行发送
                smtpObj.sendmail(sender, receivers, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                # 若发送过程中出现 SMTP 相关异常，打印错误信息
                raise SIONError('html Error:',e)
            finally:
                # 无论邮件发送是否成功，最后都关闭与 SMTP 服务器的连接
                smtpObj.quit()


    def text(sender, password, receivers, subject, text_content, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于发送纯文字格式的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（部分邮箱需要使用授权码而非登录密码）。
            receivers (list): 收件人的邮箱地址列表，列表中的每个元素为一个字符串形式的邮箱地址。
            subject (str): 邮件的主题，用于在收件人的邮箱列表中标识该邮件的大致内容。
            text_content (str): 邮件的纯文字正文内容。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需要根据实际邮箱提供商进行修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587，部分邮箱可能使用其他端口。

            返回:
            None
            """
            try:
                # 创建一个 MIMEText 对象来表示邮件内容，指定邮件类型为纯文本，编码为 UTF-8
                message = MIMEText(text_content, 'plain', 'utf-8')
                # 设置邮件的主题，并使用 Header 处理中文编码
                message['Subject'] = Header(subject, 'utf-8')
                # 设置邮件的发件人，并使用 Header 处理中文编码
                message['From'] = Header(sender, 'utf-8')
                # 设置邮件的收件人，并使用 Header 处理中文编码
                message['To'] = Header(", ".join(receivers), 'utf-8')

                # 连接到指定的 SMTP 服务器和端口
                smtpObj = smtplib.SMTP(smtp_server, smtp_port)
                # 开启 TLS 加密，确保与 SMTP 服务器的通信安全
                smtpObj.starttls()
                # 使用发件人的邮箱地址和授权码登录 SMTP 服务器
                smtpObj.login(sender, password)
                # 发送邮件，将邮件对象转换为字符串形式进行发送
                smtpObj.sendmail(sender, receivers, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                # 若发送过程中出现 SMTP 相关异常，打印错误信息
                raise SIONError('text Error:',e)
            finally:
                # 无论邮件发送是否成功，最后都关闭与 SMTP 服务器的连接
                smtpObj.quit()


    def repeat_text(sender, password, receivers, subject, text_content, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于批量发送纯文字邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（部分邮箱需要使用授权码而非登录密码）。
            receivers (list): 收件人的邮箱地址列表，列表中的每个元素为一个字符串形式的邮箱地址。
            subject (str): 邮件的主题，用于在收件人的邮箱列表中标识该邮件的大致内容。
            text_content (str): 邮件的纯文字正文内容。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需要根据实际邮箱提供商进行修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587，部分邮箱可能使用其他端口。

            返回:
            None
            """
            for receiver in receivers:
                text(sender, password, receiver, subject, text_content, smtp_server, smtp_port)


    def repeat_html(sender, password, receivers, subject, html_content, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于批量发送 HTML 邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（部分邮箱需要使用授权码而非登录密码）。
            receivers (list): 收件人的邮箱地址列表，列表中的每个元素为一个字符串形式的邮箱地址。
            subject (str): 邮件的主题，用于在收件人的邮箱列表中标识该邮件的大致内容。
            html_content (str): 邮件的 HTML 格式正文内容。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需要根据实际邮箱提供商进行修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587，部分邮箱可能使用其他端口。

            返回:
            None
            """
            for receiver in receivers:
                html(sender, password, receiver, subject, html_content, smtp_server, smtp_port)


    def repeat_image_html(sender, password, receivers, subject, html_content, image_path, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于批量发送嵌入图片到邮件正文的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（不是登录密码，部分邮箱需要开启 SMTP 服务并获取授权码）。
            receivers (list): 收件人的邮箱地址列表，每个元素为一个字符串。
            subject (str): 邮件的主题。
            html_content (str): 包含 HTML 代码的邮件正文内容，其中需要使用 <img src="cid:image1"> 来引用嵌入的图片。
            image_path (str): 要嵌入到邮件正文中的图片文件的本地路径。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需根据实际邮箱修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587。

            返回:
            None
            """
            for receiver in receivers:
                image_html(sender, password, receiver, subject, html_content, image_path, smtp_server, smtp_port)


    def repeat_image_attachment(sender, password, receivers, subject, text_content, image_path, smtp_server='smtp.example.com', smtp_port=587):
            """
            该函数用于批量发送带有图片附件的邮件。

            参数:
            sender (str): 发件人的邮箱地址。
            password (str): 发件人邮箱的授权码（不是登录密码，部分邮箱需要开启 SMTP 服务并获取授权码）。
            receivers (list): 收件人的邮箱地址列表，每个元素为一个字符串。
            subject (str): 邮件的主题。
            text_content (str): 邮件的文本正文内容。
            image_path (str): 要作为附件发送的图片文件的本地路径。
            smtp_server (str, 可选): SMTP 服务器的地址，默认为 'smtp.example.com'，需根据实际邮箱修改。
            smtp_port (int, 可选): SMTP 服务器的端口号，默认为 587。

            返回:
            None
            """
            for receiver in receivers:
                image_attachment(sender, password, receiver, subject, text_content, image_path, smtp_server, smtp_port)


class Path:
    def desktop():
        """获取桌面位置(Desktop)"""
        return os.path.join(os.path.expanduser("~"), "Desktop")


    def system(none = None):
        """通过调用系统命令识别操作系统"""
        if none == None:
            try:
                result = subprocess.run("ver", capture_output=True, text=True, shell=True)
                if "Microsoft" in result.stdout:
                    return "Windows"
                
                result = subprocess.run("uname", capture_output=True, text=True, shell=True)
                if "Darwin" in result.stdout:
                    return "macOS"
                
                result = subprocess.run("uname", capture_output=True, text=True, shell=True)
                if "Linux" in result.stdout:
                    return "Linux"
                
            except Exception as e:
                raise SIONError('system Error:',e)

            return "未知操作系统"

        else:
            return none


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


error = Exception


class SIONError(Exception):
    """extexsion错误异常类,继承于Exception"""
    def __init__(self, message="发生 SION 相关错误"):
        # 调用父类 Exception 的构造函数，并传入错误信息
        super().__init__(message)


class SIONTypeError(SIONError):
    """基于SIONError拓展出的第一个异常类SIONTypeError"""
    def __init__(self, message="SIONTypeError occurred"):
        self.message = message
        super().__init__(self.message)


class SIONValueError(SIONError):
    """基于SIONError拓展出的第二个异常类SIONValueError"""
    def __init__(self, message="SIONValueError occurred"):
        self.message = message
        super().__init__(self.message)


class SIONKeyError(SIONError):
    """基于SIONError拓展出的第三个异常类SIONKeyError"""
    def __init__(self, message="SIONKeyError occurred"):
        self.message = message
        super().__init__(self.message)


class SIONImageError(SIONError):
    """基于SIONError拓展出的第四个异常类SIONImageError"""
    def __init__(self, message="SIONImageError occurred"):
        self.message = message
        super().__init__(self.message)


def SIONErrorNote():
    """对SIONError, SIONTypeError, SIONValueError, SIONKeyError, SIONImageError的分支树"""
    on = """
        SIONError
            |
            |___SIONImageError
            |
            |___SIONValueError
            |
            |___SIONKeyError
            |
            |___SIONTypeError
    """

    return on


class MP3ID3:
    """修改mp3-ID3的歌手和标题."""
    def __init__(self, file_path, title=None, artist=None, album=None):
        """
        初始化类，接收 MP3 文件的路径，以及可选的标题、艺术家和专辑信息
        :param file_path: MP3 文件的路径
        :param title: 新的标题，如果为 None 则不修改
        :param artist: 新的艺术家，如果为 None 则不修改
        :param album: 新的专辑，如果为 None 则不修改
        """
        self.file_path = file_path
        if title is not None or artist is not None or album is not None:
            self.modify_id3_tags(title, artist, album)
        else:
            self.read_id3_tags()


    def read_id3_tags(self):
        """
        读取 MP3 文件的 ID3 标签信息
        :return: 包含标题、艺术家和专辑信息的字典，如果出错返回空字典
        """
        try:
            audio = ID3(self.file_path)
            title = audio.get('TIT2')
            artist = audio.get('TPE1')
            album = audio.get('TALB')

            result = {}
            if title:
                result['title'] = title.text[0]
            if artist:
                result['artist'] = artist.text[0]
            if album:
                result['album'] = album.text[0]

            print("现有标签信息:")
            for key, value in result.items():
                print(f"{key}: {value}")
            return result
        except Exception as e:
            print(f"读取 ID3 标签时出错: {e}")
            return {}


    def modify_id3_tags(self, title, artist, album):
        """
        修改并保存 MP3 文件的 ID3 标签信息
        :param title: 新的标题
        :param artist: 新的艺术家
        :param album: 新的专辑
        """
        try:
            audio = ID3(self.file_path)

            # 修改标题
            if title is not None:
                audio['TIT2'] = TIT2(encoding=3, text=title)
            # 修改艺术家
            if artist is not None:
                audio['TPE1'] = TPE1(encoding=3, text=artist)
            # 修改专辑
            if album is not None:
                audio['TALB'] = TALB(encoding=3, text=album)

            # 保存修改后的标签
            audio.save()
            print(f"成功修改 {self.file_path} 的标签：标题为 {title}，艺术家为 {artist}，专辑为 {album}")
        except Exception as e:
            print(f"Error: {e}")


def brightness(brightness):
    """
    设置笔记本屏幕亮度
    brightness:设置亮度的百分比
    """
    if system() == 'Windows':
        try:
            # 创建 WMI 实例
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            # 设置屏幕亮度
            methods.WmiSetBrightness(brightness, 0)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

    if system() == 'Linux':
        try:
            # 查找背光控制器目录
            backlight_dir = '/sys/class/backlight'
            controllers = os.listdir(backlight_dir)
            if not controllers:
                print("未找到背光控制器")
                return
            controller = controllers[0]
            # 获取最大亮度值
            max_brightness_path = os.path.join(backlight_dir, controller, 'max_brightness')
            with open(max_brightness_path, 'r') as f:
                max_brightness = int(f.read().strip())
            # 计算要设置的亮度值
            brightness_value = int(max_brightness * (brightness / 100))
            # 设置亮度
            brightness_path = os.path.join(backlight_dir, controller, 'brightness')
            with open(brightness_path, 'w') as f:
                f.write(str(brightness_value))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

    if system() == 'macOS':
        try:
            subprocess.run(['brightness', str(brightness / 100)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            sys.exit()

    else:
        print("不支持的操作系统")


def crawl_page(url, base_dir):
    """
    爬取单个页面及其相关资源
    :param url: 页面的 URL
    :param base_dir: 保存文件的基础目录
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # 创建保存该页面的目录
        parsed_url = urlparse(url)
        page_dir = os.path.join(base_dir, parsed_url.netloc, parsed_url.path.strip('/'))
        os.makedirs(page_dir, exist_ok=True)

        # 保存 HTML 文件
        html_path = os.path.join(page_dir, 'index.html')
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        # 提取并下载 CSS、JavaScript 和其他资源
        for tag in soup.find_all(['link', 'script', 'img']):
            if tag.name == 'link' and tag.has_attr('href'):
                resource_url = urljoin(url, tag['href'])
            elif tag.name == 'script' and tag.has_attr('src'):
                resource_url = urljoin(url, tag['src'])
            elif tag.name == 'img' and tag.has_attr('src'):
                resource_url = urljoin(url, tag['src'])
            else:
                continue

            resource_path = urlparse(resource_url).path.strip('/')
            save_path = os.path.join(base_dir, parsed_url.netloc, resource_path)
            save_dir = os.path.dirname(save_path)
            os.makedirs(save_dir, exist_ok=True)

            download(resource_url, save_path)

        # 提取并递归爬取其他页面链接
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            if next_url.startswith(parsed_url.scheme + '://' + parsed_url.netloc):
                crawl_page(next_url, base_dir)

    except Exception as e:
        print(f"爬取页面失败: {url}, 错误信息: {e}")


def crawl_website(start_url, base_dir):
    """
    爬取整个网站
    :param start_url: 起始页面的 URL
    :param base_dir: 保存文件的基础目录
    """
    crawl_page(start_url, base_dir)


class WinRightCilck:
    global SORT_METHODS
    def auto_arrange(enable):
        try:
            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 根据 enable 参数设置 AutoArrange 键值
            auto_arrange_value = 0 if enable else 1
            winreg.SetValueEx(key, "AutoArrange", 0, winreg.REG_DWORD, auto_arrange_value)

        except FileNotFoundError:
            print("未找到对应的注册表项，请检查路径是否正确。")
        except PermissionError:
            print("没有足够的权限修改注册表，请以管理员身份运行程序。")
        except Exception as e:
            print(f"修改自动排列图标设置时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    def grid(enable):
        try:
            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 根据 enable 参数设置 SnapToGrid 键值
            snap_to_grid_value = 0 if enable else 1
            winreg.SetValueEx(key, "SnapToGrid", 0, winreg.REG_DWORD, snap_to_grid_value)

        except FileNotFoundError:
            print("未找到对应的注册表项，请检查路径是否正确。")
        except PermissionError:
            print("没有足够的权限修改注册表，请以管理员身份运行程序。")
        except Exception as e:
            print(f"修改将图标与网格对齐设置时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    def icon(enable):
        try:
            # 打开包含桌面设置的注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 根据传入的 enable 参数设置键值
            snap_to_grid_value = 1 if enable else 0
            winreg.SetValueEx(key, "SnapToGrid", 0, winreg.REG_DWORD, snap_to_grid_value)

        except Exception as e:
            print(f"修改图标与网格对齐设置时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    def desktop_icons(show):
        try:
            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 根据 show 参数设置 DesktopIcons\NewStartPanel 键值
            value = 1 if show else 0
            winreg.SetValueEx(key, "HideIcons", 0, winreg.REG_DWORD, value)

            # 通知 Explorer 进程刷新桌面
            import ctypes
            SHCNE_ASSOCCHANGED = 0x08000000
            SHCNF_FLUSH = 0x1000
            ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_FLUSH, None, None)

        except Exception as e:
            print(f"操作桌面图标显示状态时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    def icon_size(size):
        """设置桌面"""
        try:
            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 设置 IconSize 键值
            winreg.SetValueEx(key, "IconSize", 0, winreg.REG_DWORD, size)

            # 通知 Explorer 进程刷新桌面
            import ctypes
            SHCNE_ASSOCCHANGED = 0x08000000
            SHCNF_FLUSH = 0x1000
            ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_FLUSH, None, None)

        except Exception as e:
            print(f"设置桌面图标大小出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    def defaults():
        """恢复默认"""
        try:
            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 恢复 IconSize 为默认值（通常为 32）
            default_icon_size = 32
            winreg.SetValueEx(key, "IconSize", 0, winreg.REG_DWORD, default_icon_size)

            # 恢复 AutoArrange 为默认值（通常为 1，表示自动排列）
            default_auto_arrange = 1
            winreg.SetValueEx(key, "AutoArrange", 0, winreg.REG_DWORD, default_auto_arrange)

            # 恢复 SnapToGrid 为默认值（通常为 1，表示与网格对齐）
            default_snap_to_grid = 1
            winreg.SetValueEx(key, "SnapToGrid", 0, winreg.REG_DWORD, default_snap_to_grid)

            print("已恢复桌面图标的默认设置。")

            # 通知 Explorer 进程刷新桌面
            import ctypes
            SHCNE_ASSOCCHANGED = 0x08000000
            SHCNF_FLUSH = 0x1000
            ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_FLUSH, None, None)

        except Exception as e:
            print(f"恢复桌面图标默认设置时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


    SORT_METHODS = {
        "name": (0, 0),
        "date": (0, 2),
        "size": (0, 3),
    }


    def sort_order(sort_type):
        """排序方式"""
        try:
            if sort_type not in SORT_METHODS:
                print(f"不支持的排序类型: {sort_type}，支持的类型有: {', '.join(SORT_METHODS.keys())}")
                return

            # 打开注册表项
            key_path = r"Software\Microsoft\Windows\Shell\Bags\1\Desktop"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

            # 获取对应排序方式的键值
            sort_direction, sort_column = SORT_METHODS[sort_type]

            # 设置排序方式
            winreg.SetValueEx(key, "SortDirection", 0, winreg.REG_DWORD, sort_direction)
            winreg.SetValueEx(key, "SortColumn", 0, winreg.REG_DWORD, sort_column)

            print(f"已将桌面文件设置为按 {sort_type} 排序。")

            # 通知 Explorer 进程刷新桌面
            SHCNE_ASSOCCHANGED = 0x08000000
            SHCNF_FLUSH = 0x1000
            ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_FLUSH, None, None)

        except Exception as e:
            print(f"设置桌面文件排序方式时出错: {e}")
        finally:
            if 'key' in locals():
                key.Close()


class FileCompressor:
    """可以压缩各种格式的文件,支持with语句."""
    def __init__(self, source_path, output_path):
        self.source_path = source_path
        self.output_path = output_path


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


    def zip(self):
        with zipfile.ZipFile(self.output_path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(self.source_path):
                zipf.write(self.source_path, os.path.basename(self.source_path))
            else:
                for root, dirs, files in os.walk(self.source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.source_path)
                        zipf.write(file_path, arcname)


    def tar(self):
        with tarfile.open(self.output_path + '.tar', 'w') as tar:
            if os.path.isfile(self.source_path):
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))
            else:
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))


    def tarbz2(self):
        with tarfile.open(self.output_path + '.tar.bz2', 'w:bz2') as tar:
            if os.path.isfile(self.source_path):
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))
            else:
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))


    def targz(self):
        with tarfile.open(self.output_path + '.tar.gz', 'w:gz') as tar:
            if os.path.isfile(self.source_path):
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))
            else:
                tar.add(self.source_path, arcname=os.path.basename(self.source_path))

    def bz2(self):
        if os.path.isfile(self.source_path):
            with open(self.source_path, 'rb') as f_in, bz2.open(self.output_path + '.bz2', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        else:
            print("BZ2 格式仅支持压缩单个文件。")


    def gz(self):
        if os.path.isfile(self.source_path):
            with open(self.source_path, 'rb') as f_in, gzip.open(self.output_path + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        else:
            print("GZ 格式仅支持压缩单个文件。")


    def rar(self):
        if os.path.exists(self.source_path):
            Archive(self.source_path).extractall(self.output_path + '.rar')

        else:
            print(f"源文件或文件夹 {self.source_path} 不存在。")


    def zip7(self):
        if os.path.exists(self.source_path):
            with py7zr.SevenZipFile(self.output_path + '.7z', 'w') as archive:
                if os.path.isfile(self.source_path):
                    archive.write(self.source_path, os.path.basename(self.source_path))
                else:
                    for root, dirs, files in os.walk(self.source_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, self.source_path)
                            archive.write(file_path, arcname)
        else:
            print(f"源文件或文件夹 {self.source_path} 不存在。")


    def ziplzma(self):
        if os.path.isfile(self.source_path):
            with open(self.source_path, 'rb') as f_in, lzma.open(self.output_path + '.lzma', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        else:
            print("LZMA 格式仅支持压缩单个文件。")


class FileDecompressor:
    """解压缩各种格式"""
    def __init__(self, source_path, output_path):
        """
        初始化类，接收压缩文件路径和目标解压路径
        :param source_path: 压缩文件的路径
        :param output_path: 解压文件的输出路径
        """
        self.source_path = source_path
        self.output_path = output_path

    def __enter__(self):
        """
        支持 with 语句，返回类的实例
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出 with 语句块时执行，目前为空
        """
        pass


    def zip(self):
        """
        解压 ZIP 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.zip'):
            with zipfile.ZipFile(self.source_path, 'r') as zip_ref:
                zip_ref.extractall(self.output_path)

        else:
            print(f"{self.source_path} 不是有效的 ZIP 文件。")


    def tar(self):
        """
        解压 TAR 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.tar'):
            with tarfile.open(self.source_path, 'r') as tar_ref:
                tar_ref.extractall(self.output_path)

        else:
            print(f"{self.source_path} 不是有效的 TAR 文件。")


    def tar_bz2(self):
        """
        解压 TAR.BZ2 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.tar.bz2'):
            with tarfile.open(self.source_path, 'r:bz2') as tar_ref:
                tar_ref.extractall(self.output_path)

        else:
            print(f"{self.source_path} 不是有效的 TAR.BZ2 文件。")


    def tar_gz(self):
        """
        解压 TAR.GZ 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.tar.gz'):
            with tarfile.open(self.source_path, 'r:gz') as tar_ref:
                tar_ref.extractall(self.output_path)

        else:
            print(f"{self.source_path} 不是有效的 TAR.GZ 文件。")


    def bz2(self):
        """
        解压 BZ2 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.bz2'):
            output_file = os.path.join(self.output_path, os.path.basename(self.source_path).replace('.bz2', ''))
            with bz2.open(self.source_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        else:
            print(f"{self.source_path} 不是有效的 BZ2 文件。")


    def gz(self):
        """
        解压 GZ 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.gz'):
            output_file = os.path.join(self.output_path, os.path.basename(self.source_path).replace('.gz', ''))
            with gzip.open(self.source_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        else:
            print(f"{self.source_path} 不是有效的 GZ 文件。")


    def rar(self):
        """
        解压 RAR 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.rar'):
            try:
                Archive(self.source_path).extractall(self.output_path)

            except Exception as e:
                print(f"解压 {self.source_path} 时出错: {e}")
        else:
            print(f"{self.source_path} 不是有效的 RAR 文件。")


    def zip7(self):
        """
        解压 7-Zip 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.7z'):
            with py7zr.SevenZipFile(self.source_path, 'r') as archive:
                archive.extractall(self.output_path)

        else:
            print(f"{self.source_path} 不是有效的 7-Zip 文件。")


    def ziplzma(self):
        """
        解压 LZMA 格式的文件
        """
        if os.path.exists(self.source_path) and self.source_path.endswith('.lzma'):
            output_file = os.path.join(self.output_path, os.path.basename(self.source_path).replace('.lzma', ''))
            with lzma.open(self.source_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        else:
            print(f"{self.source_path} 不是有效的 LZMA 文件。")


if __name__ == "__main__":
    _test()