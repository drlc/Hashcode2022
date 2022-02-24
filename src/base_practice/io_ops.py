import os
from pathlib import Path
from typing import List

input_folder_path = Path(os.path.dirname(__file__)) / "../../inputs"
output_folder_path = Path(os.path.dirname(__file__)) / "../../outputs"


class IOOps(object):

    def read_file(self, file_name):
        with open(input_folder_path / file_name, "r") as f:
            content = f.readlines()
            content = [x.replace("\n", "").split(" ") for x in content]
            return ((int(content[0][0]), int(content[0][1])), content[1:])

    def write_objects_in_file(self, filename, objects: List):
        file = open(output_folder_path / filename, "a+")
        file.write(str(len(objects)) + '\n')
        for element in objects:
            file.write(element.__str__() + '\n')
        file.close()

    def write_in_file(self, filename, new_line: str):
        file = open(output_folder_path / filename, "a+")
        file.write(str(new_line) + '\n')
        file.close()
