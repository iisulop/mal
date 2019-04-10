from typing import Any


class MalException(Exception):
    pass


class MalUnbalancedException(MalException):
    pass


class MalType:
    def __init__(self, val: Any):
        self.val = val


class MalString(MalType):
    def __str__(self) -> str:
        return self.val


class MalInt(MalType):
    def __str__(self) -> str:
        return str(self.val)


class MalList(list, MalType):
    opening_paren = '('
    closing_paren = ')'


class MalHashMap(MalList):
    opening_paren = '{'
    closing_paren = '}'


class MalVector(MalList):
    opening_paren = '['
    closing_paren = ']'


PARENS = {'(': dict(end=')', type=MalList),
          '[': dict(end=']', type=MalVector),
          '{': dict(end='}', type=MalHashMap)}


QUOTES = {"'": 'quote',
          '`': 'quasiquote',
          '~': 'unquote',
          '~@': 'splice-unquote',
          '@': 'deref',
          '^': 'with-meta'}
