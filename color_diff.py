from colorama import Fore, init

# initialise colorama
init()


def color_diff(config_diff):
    for line in config_diff:
        if line.startswith('@@'):
            yield Fore.YELLOW + line + Fore.RESET
        elif line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line
