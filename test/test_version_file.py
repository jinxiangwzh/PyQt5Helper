import unittest

from widget.sub_win_special.c_version_file import VersionFile


class MyTestCase(unittest.TestCase):

    def test_file_parse(self):
        test = "(filevers=(5, 28, 0, 0),\
                prodvers=(5, 28, 0, 0),\
                )"
        FixedFileInfo = eval(test)






if __name__ == '__main__':
    unittest.main()
