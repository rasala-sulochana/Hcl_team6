import pytest
from level1.file_search import FileFinder
from level1.find_drive import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj = SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('file1.txt','C:\hcl')
        self.expected_filename=d[0]
        self.actual_res='C:\\hcl\\file1.txt'
        assert self.expected_filename == self.actual_res