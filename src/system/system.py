import platform


def get_os() -> str:
    return platform.system()


def get_python_version() -> str:
    return platform.python_version()


def get_hostname() -> str:
    return platform.node()
