## py-stresser
Данная программа предназначенна для 
стресс-тестирования различных файлов. \
На данный момент поддерживается работа со скриптами
на языках программирования`c, c++, python`

---

## принцип работы
+ у пользователя есть рабочее решение и решение с ошибкой
+ пользователь пишет генератор тестов 
+ пользователь запускает утилиту 



--- 

## установка и использование

+ с помощью pip устанавливаем пакет
```
pip install py-stresser
```

+ запускаем утилиту `stresser` с нужными нам параметрами

---

## конфигурация
параметры можно задавать аргументами командной строки, 
либо с помощью конфигурационного файла с расширением `.ini` \
в случае использования конфигурационного файла все параметры должны быть в секции `[settings]`

### параметры:
```
    -h, --help            show this help message and exit
    -c CONFIG_PATH, --CONFIG_PATH CONFIG_PATH
                            путь к конфигурационному файлу. Если прописан, то все аргументы будут браться из него
    -S SOLUTION_PATH, --SOLUTION_PATH SOLUTION_PATH
                            путь к решению с ошибками
    -D DUMMY_PATH, --DUMMY_PATH DUMMY_PATH
                            путь к правильному решению
    -G GENERATOR_PATH, --GENERATOR_PATH GENERATOR_PATH
                            путь к программе, которая генерирует данные в stdout
    -N NTESTS, --NTESTS NTESTS
                            необходимое количество тестов. Базовое значение: 10000
    -s SAVE_TESTS, --SAVE_TESTS SAVE_TESTS
                            сохранять ли тесты. варианты: True/False. Базовое значение: false
    -t CHECKER_TYPE, --CHECKER_TYPE CHECKER_TYPE
                            тип чекера. варианты: ['base', 'base_with_format'] Базовое значение: base_with_format
```
параметры SOLUTION_PATH, DUMMY_PATH, GENERATOR_PATH являются **обязательными**

---

## пример работы
пример работы можете посмотреть [тут](https://drive.google.com/file/d/167N40B531WfLiR9Ge4Z5qmFb__d_OU9v/view?usp=sharing)

---
## исходный код




дерево проекта:
```
.
├── test 
│   ├── tests
│   └── test.py
├── stresser
│   ├── modules
│   │   ├── parse.py
│   │   ├── launch.py
│   │   ├── __init__.py
│   │   └── checker.py
│   ├── __main__.py
│   └── __init__.py
├── setup.py
├── README.md
├── MANIFEST.in
└── Makefile

```

### команды в Makefile

`make update` - локальное обновление пакета

`make local_test` - локальный запуск тестов

`make deploy_test` - проверка работы на удаленной машине

`make push` - добавление пакета в `pypi`




**автор:** *@gingersamurai*


