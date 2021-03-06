# Created by jmlm at 15/02/2020-22:35 - test2
import argparse
"""
args parser with argparse
"""


def parse_arguments():
    """
    return parsed agrs --> treated by the caller
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", '--text', action='store_true', help="""game in text mode""")
    parser.add_argument("-g", '--graphic', action='store_true', help="""game in graphic mode""")
    return parser.parse_args()
