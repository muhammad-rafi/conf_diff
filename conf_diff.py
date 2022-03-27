from color_diff import color_diff
from html_format import html_style, difflib
from pathlib import Path
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")


class ConfDiff:

    def __init__(self, config_file1: Path, config_file2: Path, html_output: Path = None):

        """
        Initialise ConfDiff.
        @param config_file1: Path of the first config file
        @param config_file2: Path of the second config file
        @param html_output: Optional path for the HTML output file
        """

        self.file1 = Path(config_file1)
        self.file2 = Path(config_file2)

        if html_output:
            self.file3 = Path(html_output)
        else:
            self.file3 = None

    def diff(self):

        """ function to generate a colorful configuration difference
        on the cli between two configuration files and if third
        parameter is defined, that will be treated as html output
        which generates the html output file in the current directory
        by default unless desired absolute path is defined.
        """

        file1 = open(self.file1).readlines()
        file2 = open(self.file2).readlines()
        file3 = self.file3

        if file1 == file2:
            print("\n *** No Configuration Difference Found ! *** \n")

        else:
            try:
                if file3:
                    d = html_style()
                    config_diff = d.make_file(file1, file2, self.file1.name, self.file2.name)

                    with open(file3, "w") as f:
                        f.write(config_diff)

                    print(f"\n{'*'*75}\nHTML output file ({file3}) has been saved\n{'*'*75}")

                else:
                    config_diff = difflib.unified_diff(file1, file2, self.file1.name, self.file2.name, n=4)
                    display_diff = color_diff(config_diff)

                    print("\n" + "*" * 75)
                    print(f"Configuration Difference (ConfDiff) @ {date_time}")
                    print("*" * 75, "\n")

                    """testing purpose only
                    return sys.stdout.writelines(config_diff)
                    return sys.stdout.writelines(''.join(display_diff))
                    """
                    return ''.join(display_diff)

            except Exception as error:
                return error
