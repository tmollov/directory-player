import os
from src.components.folder_files_section.StandardItem import StandardItem


class Directories():
    def __init__(self):
        self.homeDir = "/home"
        self.userDir = self.homeDir + "/tmollov"

    # Get directories from rootdir
    def get_dirs(self, rootdir, include_hidden=False):
        ls = []
        for it in os.scandir(rootdir):
            if it.is_dir():
                if include_hidden or not it.name.startswith('.'):
                    ls.append(it.path.split('/')[-1])
        return ls

    def get_standard_items(self, rootdir, include_hidden=False):
        dirs = self.get_dirs(rootdir)
        items = []
        for it in dirs:
            items.append(StandardItem(it))
        return items
