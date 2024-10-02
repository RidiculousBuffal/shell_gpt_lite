import platform
def get_os_type():
    os_type = platform.system()
    if os_type == 'Windows':
        return 'Windows, Powershell'
    if os_type == 'Darwin':
        return 'Mac'
    if os_type == 'Linux':
        return 'Linux'
    else:
        return os_type