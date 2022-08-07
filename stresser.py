import os
from stresser_data.modules import *


launch_solution = compile("main.cpp", "solution")
launch_solution("input.txt", "output.txt")