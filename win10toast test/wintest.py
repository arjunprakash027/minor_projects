from win10toast import ToastNotifier
import six
import appdirs
import packaging.requirements

toaster = ToastNotifier()
toaster.show_toast(
    "Testing pyinstaller",
    "Trying to find root cause",
    duration=10, icon_path="python.ico")