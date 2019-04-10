from typing import Any


class MalException(Exception):
    pass


class MalUnbalancedException(MalException):
    pass


class MalUnbalancedHashException(MalUnbalancedException):
    pass


class MalUnsupportedHashKeyType(MalException):
    pass


class MalType:
    def __init__(self, val: Any):
        self.val = val


class MalNilType(MalType):
    def __str__(self) -> str:
        return self.val


class MalBoolType(MalType):
    def __str__(self) -> str:
        return self.val


class MalString(MalType):
    def __str__(self) -> str:
        return self.val


class MalKeyword(MalType):
    def __str__(self) -> str:
        return self.val


class MalInt(MalType):
    def __str__(self) -> str:
        return str(self.val)


class MalList(list, MalType):
    opening_paren = '('
    closing_paren = ')'


class MalVector(MalList):
    opening_paren = '['
    closing_paren = ']'


class MalHashMap(MalList):
    opening_paren = '{'
    closing_paren = '}'


def check_hash_map(hash_map: MalHashMap):
    if len(hash_map) % 2 != 0:
        raise MalUnbalancedHashException('Unbalanced hash key-value pairs')
    for key in hash_map[::2]:
        if not isinstance(key, (MalString, MalKeyword, MalInt)):
            raise MalUnsupportedHashKeyType(f'Unsupported hash key type `{type(key)}`')


PARENS = {'(': dict(end=')', type=MalList),
          '[': dict(end=']', type=MalVector),
          '{': dict(end='}', type=MalHashMap, checker=check_hash_map)}

QUOTES = {"'": 'quote',
          '`': 'quasiquote',
          '~': 'unquote',
          '~@': 'splice-unquote',
          '@': 'deref',
          '^': 'with-meta'}
