import os

SUT_BUG = False
if os.environ.get('SUT_BUG') is not None:
    SUT_BUG = True