import os
from argparse import ArgumentParser
from configparser import ConfigParser

def validate(in_data: dict):
    for now_path in ['SOLUTION_PATH', 'DUMMY_PATH', 'GENERATOR_PATH']:
        assert (now_path in in_data and in_data[now_path]) != None, f"there is not {now_path}"
        if not os.path.isabs(in_data[now_path]):
            in_data[now_path] = os.path.abspath(in_data[now_path])
        assert os.path.isfile(in_data[now_path]), f"{in_data[now_path]} not such file"
    assert ('NTESTS' in in_data and type(in_data["NTESTS"]) == int and in_data["NTESTS"] > 0), "NTESTS must be positive integer"
    assert ('save_tests' in in_data)


def parse_input() -> dict:
    parser = ArgumentParser()

    parser.add_argument("-c", "--config_path")
    parser.add_argument("-S", "--SOLUTION_PATH")
    parser.add_argument("-D", "--DUMMY_PATH")
    parser.add_argument("-G", "--GENERATOR_PATH")
    parser.add_argument("-N", "--NTESTS", type=int)
    parser.add_argument("-s", "--save_tests", action="store_true")
    args = parser.parse_args()
    res_dict = {}
    if args.config_path == None:
        res_dict = vars(args)
        res_dict.pop('config_path')
    else:
        config = ConfigParser()
        config.optionxform = str
        config.read(os.path.abspath(args.config_path))
        res_dict = (dict(config['settings']))
        res_dict['NTESTS'] = config.getint('settings', 'NTESTS')
        res_dict['save_tests'] = config.getboolean('settings', 'save_tests')
    return res_dict

if __name__ == "__main__":
    in_data = parse_input()
    print(in_data, "\n\n\n")
    validate(in_data)
    print(in_data)