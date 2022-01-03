import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '~/Documents/dsi/ntropy_assessment/utils2')

from utils2.mnist_reader import load_mnist
import pandas as pd
# from .utils2 import *


# print(__name__)

# try:
#     # Trying to find module in the parent package
#     from . import utils2
#     print(utils2.)
#     del config
# except ImportError:
#     print('Relative import failed')

# try:
#     # Trying to find module on sys.path
#     import config
#     print(config.debug)
# except ModuleNotFoundError:
#     print('Absolute import failed')


if __name__ == '__main__':
    print('test')