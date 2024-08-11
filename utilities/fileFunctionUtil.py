import time
import os

class FileFunctionUtil:

    @staticmethod
    def get_dynamic_path(project_name):
        create_path = ""
        root_dir = os.path.abspath(os.curdir)
        split_dir = root_dir.split("\\")
        name = ""
        for list_value in split_dir:
            if list_value == project_name:
                name = list_value
                break
            create_path = create_path + "\\" + list_value
        create_path = create_path + "\\" + name
        final_path = create_path[1::]
        return final_path