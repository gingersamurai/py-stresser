import os
from argparse import ArgumentParser
from configparser import ConfigParser



def parse_input() -> dict:
    parser = ArgumentParser()

    parser.add_argument("-c", "--config_path")
    parser.add_argument("-S", "--SOLUTION_PATH")
    parser.add_argument("-D", "--DUMMY_PATH")
    parser.add_argument("-G", "--GENERATOR")
    parser.add_argument("-N", "--NTESTS", type=int)
    args = parser.parse_args()
    res_dict = {}
    if args.config_path == None:
        res_dict = vars(args)
        res_dict.pop('config_path')
        print(res_dict)
    else:
        config = ConfigParser()
        config.optionxform = str
        config.read(os.path.abspath(args.config_path))
        res_dict = (dict(config['settings']))
    print(res_dict)


parse_input()