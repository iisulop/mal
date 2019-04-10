from mal_types import MalType, MalList, MalString


def pr_str(mal: MalType, print_readably: bool = True) -> str:
    output = []
    # print(f'pr {type(mal)} {mal}')
    if not isinstance(mal, MalList):
        # print(f'^list')
        return mal
    for m in mal:
        if isinstance(m, MalList):
            output.append(pr_str(m))
        elif isinstance(m, MalString):
            s = str(m)
            if not print_readably:
                for replace_what, replace_with in [('\\n', '\n'), ('\\"', '"'), ('\\\\', '\\')]:
                    s.replace(replace_what, replace_with)
            output.append(s)
        else:
            output.append(str(m))
    return mal.opening_paren  + ' '.join(output) + mal.closing_paren
