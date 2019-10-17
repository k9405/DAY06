import unittest

import time

from case.TpShop_Login import TPShopLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

# suite.addTest(TPShopLogin("tetsLogin"))
suite.addTest(unittest.makeSuite(TPShopLogin))
file = "./report/repotr111111"

with open(file  + ".html", "wb") as f:
    runner = HTMLTestRunner(f, title="我的报告", description="chrome")
    runner.run(suite)
