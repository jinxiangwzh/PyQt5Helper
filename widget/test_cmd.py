import logging
import subprocess
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_add_data_cmd(self):
        cmd = ['pyinstaller', '--onedir', '--add-data', 'readme.md;.', 'E:/PyQt5Helper/PyQt5Helper.py']
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, encoding="utf-8")
        while self.proc.poll() is None:  # 检查子进程是否被终止
            out = self.proc.stdout.readline().strip()
            logging.info(out)


if __name__ == '__main__':
    unittest.main()
