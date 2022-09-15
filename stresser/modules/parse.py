import os
from argparse import ArgumentParser
from configparser import ConfigParser

CHECKER_TYPES = ['base', 'base_with_format']

def validate(in_data: dict):
    for now_path in ['SOLUTION_PATH', 'DUMMY_PATH', 'GENERATOR_PATH']:
        assert (in_data[now_path] != None), f"there is not {now_path}"
        # if not os.path.isabs(in_data[now_path]):
        #     in_data[now_path] = os.path.abspath(in_data[now_path])
        assert os.path.isfile(in_data[now_path]), in_data[now_path] + ': not such file'
    
    assert (type(in_data["NTESTS"]) == int) and (in_data["NTESTS"] > 0), "NTESTS must be positive integer"
    assert (in_data['CHECKER_TYPE'] in CHECKER_TYPES), "wrong CHECKER_TYPE"

def set_default(in_data: dict):
    def_dict = {
        'NTESTS': 10000,
        'SAVE_TESTS': False,
        'CHECKER_TYPE': 'base_with_format',
        'SOLUTION_PATH': None,
        'DUMMY_PATH': None,
        'GENERATOR_PATH': None
    }
    for key, val in in_data.items():
        if val != None:
            def_dict[key] = val
    
    return def_dict


def parse_input() -> dict:
    parser = ArgumentParser()

    parser.add_argument("-c", "--CONFIG_PATH", help="путь к конфигурационному файлу.\
    Если прописан, то все аргументы будут браться из него")
    parser.add_argument("-S", "--SOLUTION_PATH", help="путь к решению с ошибками")
    parser.add_argument("-D", "--DUMMY_PATH", help="путь к правильному решению")
    parser.add_argument("-G", "--GENERATOR_PATH", help="путь к программе, которая генерирует данные в stdout")
    parser.add_argument("-N", "--NTESTS", type=int, help="необходимое количество тестов. Базовое значение: 10000")
    parser.add_argument("-s", "--SAVE_TESTS", help="сохранять ли тесты. варианты: true/false. Базовое значение: false")
    parser.add_argument("-t", "--CHECKER_TYPE", help=f"тип чекера.\
    варианты: {CHECKER_TYPES} Базовое значение: base_with_format")
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
        # res_dict['NTESTS'] = config.getint('settings', 'NTESTS')
        # res_dict['SAVE_TESTS'] = config.getboolean('settings', 'SAVE_TESTS')
    res_dict = set_default(res_dict)
    validate(res_dict)
    return res_dict
