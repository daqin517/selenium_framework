import unittest
from utils.HTMLTestRunner_PY3 import HTMLTestRunner


class TestHTMLTestRunnerPY3(unittest.TestCase):
    def test_py3_success(self):
        self.assertEqual(1+1, 2)

    def test_py3_fail(self):
        self.assertEqual(1+1, 3)


class TestHTML(unittest.TestCase):
    def test_html_success(self):
        self.assertEqual(1+2, 3)


class TestError(unittest.TestCase):
    def test_error(self):
        self.assertEqual(1/0, 1)


if __name__ == '__main__':
    import os
    report = os.path.join(r'C:\Personal\python\report.html')
    # report = r'C:\Personal\python\report.html'
    print('报告为',type(report))
    st = unittest.TestSuite()
    st.addTests([TestHTMLTestRunnerPY3('test_py3_success'), TestHTMLTestRunnerPY3('test_py3_fail'),
                 TestHTML('test_html_success'), TestError('test_error')])
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
        runner.run(st)