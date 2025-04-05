import win32api
import win32com.client
import win32gui
import win32con
import pythoncom


class BaseIcon:
    def __init__(self, target_path, icon_path):
        """
        初始化 BaseIcon 类的实例。

        :param target_path: 目标文件的完整路径，可以是快捷方式文件（.lnk）或可执行文件（.exe）。
        :param icon_path: 要设置的图标文件的完整路径，通常是 .ico 文件。
        """
        self.target_path = target_path
        self.icon_path = icon_path
        self.shell = None
        self.hUpdate = None
        self.hIcon = None

    def __enter__(self):
        """
        进入上下文管理器时执行的操作。
        初始化 COM 库，并根据目标文件类型做相应准备。

        :return: 返回当前实例本身，以便在 with 语句块中使用。
        """
        try:
            pythoncom.CoInitialize()
            return self
        except Exception as e:
            print(f"初始化时出错: {e}")
            self.__exit__(type(e), e, None)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器时执行的操作。
        释放 COM 库资源。

        :param exc_type: 异常类型，如果没有异常则为 None。
        :param exc_val: 异常值，如果没有异常则为 None。
        :param exc_tb: 异常追踪信息，如果没有异常则为 None。
        """
        try:
            pythoncom.CoUninitialize()
        except Exception as e:
            print(f"释放 COM 资源时出错: {e}")


class ExeIcon(BaseIcon):
    def __init__(self, target_path, icon_path):
        super().__init__(target_path, icon_path)

    def __enter__(self):
        super().__enter__()
        try:
            self.hIcon = win32gui.LoadImage(0, self.icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
            if self.hIcon == 0:
                print(f"无法加载图标: {self.icon_path}")
                raise Exception(f"无法加载图标: {self.icon_path}")
            return self
        except Exception as e:
            print(f"初始化时出错: {e}")
            self.__exit__(type(e), e, None)
            raise


    def icon(self):
        """
        更改可执行文件的图标。
        """
        try:
            self.hUpdate = win32api.BeginUpdateResource(self.target_path, False)
            if self.hUpdate == 0:
                print(f"无法打开可执行文件进行更新: {self.target_path}")
                return
            result = win32api.UpdateResource(self.hUpdate, win32con.RT_ICON, 1, 0, win32gui.GetIconInfo(self.hIcon)[4])
            if result == 0:
                print(f"无法更新图标资源: {self.target_path}")
                return
            win32api.EndUpdateResource(self.hUpdate, False)
        except Exception as e:
            print(f"Error: {e}")


    def get_icon(self):
        """
        获取可执行文件的图标句柄。

        :return: 可执行文件的图标句柄，如果获取失败则返回 None。
        """
        try:
            self.hIcon = win32gui.LoadImage(0, self.icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
            if self.hIcon == 0:
                print(f"无法加载图标: {self.icon_path}")
                return None
            return self.hIcon
        except Exception as e:
            print(f"Error: {e}")
            return None


class LnkIcon(BaseIcon):
    def __init__(self, target_path, icon_path):
        super().__init__(target_path, icon_path)


    def __enter__(self):
        super().__enter__()
        try:
            self.shell = win32com.client.Dispatch("WScript.Shell")
            return self
        except Exception as e:
            print(f"初始化时出错: {e}")
            self.__exit__(type(e), e, None)
            raise


    def icon(self):
        """
        更改快捷方式文件的图标。
        """
        try:
            if self.shell:
                shortcut = self.shell.CreateShortCut(self.target_path)
                shortcut.IconLocation = self.icon_path
                shortcut.Save()
            else:
                print("WScript.Shell 对象未正确初始化，无法更改图标。")
        except Exception as e:
            print(f"Error: {e}")


    def get_icon(self):
        """
        获取快捷方式文件的图标路径。

        :return: 快捷方式文件的图标路径，如果获取失败则返回 None。
        """
        try:
            if self.target_path.endswith('.lnk') and self.shell:
                shortcut = self.shell.CreateShortCut(self.target_path)
                return shortcut.IconLocation
            else:
                print("目标文件不是快捷方式或 WScript.Shell 对象未正确初始化。")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None