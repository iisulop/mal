from typing import List, Type
import re
from mal_types import MalList, MalInt, MalString, MalUnbalancedException, MalType, PARENS, QUOTES, MalKeyword, \
    MalBoolType, MalNilType


def log_print(*args):
    pass
    # print(*args)


class Reader:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def next(self) -> str:
        val = self.tokens[self.pos]
        self.pos += 1
        return val

    def peek(self) -> str:
        return self.tokens[self.pos]


def tokenize(line: str) -> List[str]:
    r = re.compile('''[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)''')
    return r.findall(line)


def closing_for(opening: str) -> str:
    return PARENS[opening]['end']


def type_for(opening: str) -> Type[MalList]:
    return PARENS[opening]['type']


def check_val(opening: str, val: MalList):
    PARENS[opening].get('checker', lambda x: None)(val)


def read_list(reader: Reader) -> MalList:
    opening = reader.next()
    atoms = type_for(opening)()

    log_print(f'opening {opening}')
    try:
        while reader.peek() != closing_for(opening):
            log_print(f'peek {reader.peek()}')
            atoms.append(read_form(reader))
    except IndexError as e:
        raise MalUnbalancedException(f'unbalanced `{opening}`') from e
    val = reader.next()
    log_print(f'val {val}')
    check_val(opening, atoms)
    return atoms


def read_atom(reader: Reader) -> MalType:
    atom = reader.next()
    try:
        return MalInt(int(atom))
    except ValueError:
        while atom.endswith('\\'):
            atom += reader.next()
        if atom in QUOTES.keys():
            val = MalList()
            val.append(QUOTES[atom])
            val.append(read_form(reader))
            if QUOTES[atom] == 'with-meta':
                # Turn the parameters around
                last = val.pop()
                val.append(read_form(reader))
                val.append(last)
            return val
        if atom == 'nil':
            return MalNilType(atom)
        if atom in ['true, false']:
            return MalBoolType(atom)
        return MalString(atom)


def read_string(reader: Reader) -> MalString:
    atom = reader.next()
    while atom[-2:] == '\\"':
        atom += reader.next()
        if reader.peek() == '"':
            atom += reader.next()
    if not atom.endswith('"'):
        raise MalUnbalancedException(f'unbalanced "')
    return MalString(atom)


def read_keyword(reader: Reader) -> MalKeyword:
    atom = reader.next()
    return MalKeyword(atom)


def read_form(reader: Reader) -> list:
    char = reader.peek()
    log_print(f'char {char}')
    if char in PARENS.keys():
        val = read_list(reader)
    elif char.startswith('"'):
        val = read_string(reader)
    elif char.startswith(':'):
        val = read_keyword(reader)
    else:
        val = read_atom(reader)
    return val


def read_str(line):
    tokens = tokenize(line)
    log_print(f'tokens: {tokens}')
    reader = Reader(tokens)
    val = read_form(reader)
    log_print(f'read_form: {val}')
    return val
