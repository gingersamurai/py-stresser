import os
from argparse import ArgumentParser
from configparser import ConfigParser

CHECKER_TYPES = ['base', 'base_with_format']

def validate(in_data: dict):
    for now_path in ['SOLUTION_PATH', 'DUMMY_PATH', 'GENERATOR_PATH']:
        assert (now_path in in_data and in_data[now_path]) != None, f"there is not {now_path}"
        if not os.path.isabs(in_data[now_path]):
            in_data[now_path] = os.path.abspath(in_data[now_path])
        assert os.path.isfile(in_data[now_path]), f"{in_data[now_path]} not such file"
    assert ('NTESTS' in in_data) and (type(in_data["NTESTS"]) == int) and (in_data["NTESTS"] > 0), "NTESTS must be positive integer"
    assert ('SAVE_TESTS' in in_data), "must be SAVE_TESTS (true/false)"
    assert ('CHECKER_TYPE' in in_data) and (in_data['CHECKER_TYPE'] in CHECKER_TYPES), "wrong CHECKER_TYPE"


def parse_input() -> dict:
    parser = ArgumentParser()

    parser.add_argument("-c", "--CONFIG_PATH", help="path to config.\
    If set, args will ge gotten from config")
    parser.add_argument("-S", "--SOLUTION_PATH", help="path to code with mistakes")
    parser.add_argument("-D", "--DUMMY_PATH", help="path to code without mistakes")
    parser.add_argument("-G", "--GENERATOR_PATH", help="path to programm generates text data to stdout")
    parser.add_argument("-N", "--NTESTS", type=int, help="count of tests")
    parser.add_argument("-s", "--SAVE_TESTS", action="store_true", help="if set, test will be saved")
    parser.add_argument("-t", "--CHECKER_TYPE", help=f"values: {CHECKER_TYPES}")
    args = parser.parse_args()
    res_dict = {}
    if args.CONFIG_PATH == None:
        res_dict = vars(args)
        res_dict.pop('CONFIG_PATH')
    else:
        config = ConfigParser()
        config.optionxform = str
        config.read(os.path.abspath(args.CONFIG_PATH))
        res_dict = (dict(config['settings']))
        res_dict['NTESTS'] = config.getint('settings', 'NTESTS')
        res_dict['SAVE_TESTS'] = config.getboolean('settings', 'SAVE_TESTS')
    validate(res_dict)
    return res_dict

if __name__ == "__main__":
    print(parse_input())