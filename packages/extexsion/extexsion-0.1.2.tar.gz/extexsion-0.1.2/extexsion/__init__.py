"""
注意!使用此模块时有很多函数需要管理员权限!
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

import winreg
import time
import ctypes
import sys, os
import inspect
import requests
import subprocess
import tkinter as tk
from ctypes import wintypes
from win32com.client import Dispatch

def check_admin():
    """
    判断有没有管理员权限
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_admin():
    """
    以管理员身份重新运行脚本
    """
    if not check_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

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
            print(f"文件 {file_path} 不存在")

    else:
        print("此功能仅支持Windows系统")


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
    
def file_hash(file_path):
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
            print(f"Error: {e}")
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
            print(f"打开浏览器失败: {e}")

    elif system() == 'macOS':
        try:
            if browser == 'msedge':
                #Microsoft Edge
                subprocess.run(["open", "-a", "Microsoft Edge", url])
            else:
                subprocess.run(["open", "-a", "Safari", url])  # 替换为相应浏览器
        except Exception as e:
            print(f"打开浏览器失败: {e}")

    elif system() == 'Linux':
        try:
            if browser == 'msedge':
                #microsoft-edge
                subprocess.run(["microsoft-edge", url])
            else:
                subprocess.run(["xdg-open", url])  # xdg-open 是在大多数 Linux 发行版中使用的命令
        except Exception as e:
            print(f"打开浏览器失败: {e}")


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
        print(f"Failed to download the file due to error: {e}")


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
        print('Error:',e)


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
                pass  # 如果文件类型关联不存在，忽略错误

        except Exception as e:
            print(f"Error: {e}")
    elif system() == 'macOS':
        # 使用duti命令删除文件关联
        if file_extension:
            try:
                subprocess.run(["duti", "-d", file_extension], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
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
                print(f"Error: {e}")


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
            print(f"Error: {e}")
    elif system() == 'macOS':
        # 先删除旧的关联
        if old_file_extension:
            try:
                subprocess.run(["duti", "-d", old_file_extension], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
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
                print(f"Error: {e}")
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


def obtain():
    """
    通过查看注册表获取系统中所有的文件后缀名
    :return: 包含所有文件后缀名的列表
    """
    run_admin()
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
        print(f"访问注册表时出错: {e}")
    return file_extensions


def menu_app(entry_name, exe_path):
    """
    在桌面右键菜单中添加一个新的菜单项，点击该菜单项会直接打开指定的 exe 程序。

    :param entry_name: 菜单项的显示名称
    :param exe_path: 要打开的 exe 程序的路径
    """
    run_admin()
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

        print(f"成功添加菜单项：{entry_name}")
    except Exception as e:
        print(f"添加菜单项失败：{e}")


def add_menu(file_extension, file_description):
    """
    将自定义文件类型添加到桌面右键菜单的“新建”选项中。

    :param file_extension: 文件扩展名，例如 ".py"
    :param file_description: 文件描述，例如 "Python File"
    """
    run_admin()
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
        print(f"Error: {e}")


def menu_icon(menu_key_name, icon_path):
    """
    修改或添加 Windows 右键菜单项的图标
    :param menu_key_name: 菜单项在注册表中的键名
    :param icon_path: 图标文件的路径
    """
    run_admin()
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
        print(f"操作注册表时出错：{e}")


def variable(variable, value):
    """环境变量"""
    try:
        # 打开环境变量所在的注册表项
        run_admin()
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Environment", 0, winreg.KEY_ALL_ACCESS)
        # 设置环境变量的值
        winreg.SetValueEx(key, variable, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        #print(f"环境变量 {variable} 已设置为 {value}")
    except Exception as e:
        print(f"Error: {e}")
        
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

    run_admin()
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
        print("ERROR.")


def association(file_extension, program_path):
    try:
        run_admin()
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

        print(f"{file_extension} 文件已关联到 {program_path}")
    except Exception as e:
        print(f"设置文件关联时出错: {e}")

"""set_file_association(".txt", r"C:\Windows\System32\notepad.exe")"""


def systemkey():
    global GUIDs
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

    # 加载 wbemcli.dll 库
    run_admin()
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


def way():
    # 加载 user32.dll 库
    user32 = ctypes.windll.user32

    # 获取当前输入语言的句柄
    input_lang_handle = user32.GetKeyboardLayout(0)

    # 获取语言 ID
    lang_id = input_lang_handle & 0xFFFF

    # 判断语言是否为中文（简体）
    if lang_id == 0x0804:
        return 'Chinese'
    else:
        return 'English'


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
    run_admin()
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
        print(f"文件 {file_path} 不存在。")
        return None
    except Exception as e:
        print(f"Error: {e}")
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
        print(f"Error: {e}")


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
        run_admin()
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
        print(f"查找注册表时出错：{e}")
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
    proxy_server:服务器地址
    proxy_port:端口
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

    except Exception as e:
        print(f"Error: {e}")


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
        print(f"Error: {e}")


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
    """pi.dwProcessId = pid"""
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
    # 打开进程
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
        print(f"源文件 {src} 未找到。")
    except PermissionError:
        print("没有足够的权限进行复制操作。")
    except Exception as e:
        print(f"复制过程中出现错误: {e}")


def delete_file(file_path):
    if system() == 'Windows':
        try:
            # 构建要执行的命令
            command = ['del', file_path]
            # 执行命令
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"删除文件时出错: {e.stderr.strip()}")
        except FileNotFoundError:
            print(f"文件 {file_path} 未找到")

    else:
        try:
            # 构建要执行的命令
            command = ['rm', file_path]
            # 执行命令
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"删除文件时出错: {e.stderr.strip()}")
        except FileNotFoundError:
            print(f"文件 {file_path} 未找到")


if __name__ == "__main__":
    _test()