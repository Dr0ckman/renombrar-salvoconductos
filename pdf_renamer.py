import os
import re

from tika import parser


class PdfRenamer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw = parser.from_file(self.file_path)
        self.content = (self.raw['content'])

    def extract_name(self):
        pattern = r"Nombre Completo \w* \w*"
        name_regex = re.findall(pattern, self.content)
        name_regex = name_regex[0].split(" ")
        # Prune extra words
        name = name_regex[2:]
        # Convert array to string
        name_as_string = ""
        for word in name:
            name_as_string += " " + word
        name_as_string = name_as_string.strip()
        return name_as_string

    def is_day(self):
        regex_pattern = r"Diurno"
        regex = re.findall(regex_pattern, self.content)
        for word in regex:
            if word == "Diurno":
                return True
            else:
                return False

    def rename_file(self, is_day, name_as_string):
        if is_day:
            os.rename(self.file_path, os.path.join(os.path.dirname(self.file_path), name_as_string + ".pdf"))
        else:
            os.rename(self.file_path, os.path.join(os.path.dirname(self.file_path), name_as_string +
                                                   " Nocturno" + ".pdf"))
