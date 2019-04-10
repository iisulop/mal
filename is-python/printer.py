from mal_types import MalType, MalList


def pr_str(mal: MalType) -> str:
    output = []
    # print(f'pr {type(mal)} {mal}')
    if not isinstance(mal, MalList):
        # print(f'^list')
        return mal
    for m in mal:
        if isinstance(m, MalList):
            output.append(pr_str(m))
        else:
            output.append(str(m))
    return mal.opening_paren  + ' '.join(output) + mal.closing_paren
