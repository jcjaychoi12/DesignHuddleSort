from typing import Dict, List
import re


IMPORT_FILE: str = "./input.txt"
EXPORT_FILE: str = "./output.txt"
REG_EX: str = r'(?:.*[\||_])[^\d]*(\d+)$'
# Regular Expression Explaination (3 Parts):
    # (?:.*[\||_]) = Skip portions of text that is any number of any characters followed by a | or a _
        # (?:...) = Non-capturing group i.e. portions of text that won't be in the result
        # .* = Any number of any characters
            # . = Any character
            # * = Zero or more of the defined character
        # [\||_] = "\|" means the character "|" not the operation; "|" as an operation means "or"; "_" denotes itself
    # [^\d]* = Any non-digit characters
        # ^ = Negation/Opposite of 
        # \d = Numeric digits
        # * = Zero or more of the defined character
    # (\d+)$ = Capture digits
        # \d = Numeric digits
        # + = Capture group i.e. the portion of text that we want
        # $ = End of the RegEx statement

def main() -> None:
    names: Dict[int, List[str]] = {}

    with open(IMPORT_FILE, "r") as infile, open(EXPORT_FILE, "w") as outfile:
        lines: List[str] = [line.replace('"', '').strip() for line in infile]

        for name in lines:
            temp_num: int = int(re.search(REG_EX, name).group(1))
            if temp_num:
                if temp_num not in names:
                    names[temp_num] = []
                names[temp_num].append(name)
            else:
                raise TypeError("Regex did not find the template number. Please make sure the template have the t# at the end.")
            
        sorted_dict: Dict[int, List[str]] = {key: names[key] for key in sorted(names)}
        for k in sorted_dict:
            sorted_value = sorted(sorted_dict[k])
            for i in sorted_value:
                outfile.write(i + '\n')
if __name__ == "__main__":
    main()