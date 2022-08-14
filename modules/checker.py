def base_check(dummy_ans: str, solution_ans: str) -> bool:
    return dummy_ans == solution_ans


def make_format(s: str) -> str: 
    s = s.strip()
    s = s.replace(' \n', '\n')
    return s

def base_with_format_check(dummy_ans: str, solution_ans: str) -> bool:
    s1 = make_format(dummy_ans)
    s2 = make_format(solution_ans)
    return s1 == s2


if __name__ == "__main__":
    s1 = '3 \n1 2 3 \n\n'
    s2 = '3 \n1 2 3 '
    base_with_format_check(s1, s2)