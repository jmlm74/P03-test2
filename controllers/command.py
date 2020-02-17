# Created by jmlm at 15/02/2020-22:35 - test2
import argparse
"""
parse des arguments (parametres) avec argparse
"""


def parse_arguments():
    """
    renvoi les arguments parsés. Le traitement se fait dans le module appelant
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", '--text', action='store_true', help="""game in text mode""")
    parser.add_argument("-g", '--graphic', action='store_true', help="""game in graphic mode""")
    return parser.parse_args()
