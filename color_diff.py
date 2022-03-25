import datetime

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

try:
    from colorama import Fore, Back, Style, init
    init()
except ImportError:
    class ColorFallback():
        def __getattr__(self, name=''):
            return name
    Fore = Back = Style = ColorFallback()


def color_diff(diff):
    for line in diff:
        if line.startswith('@@'):
            yield Fore.MAGENTA + line + Fore.RESET
        elif line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line
