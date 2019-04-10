import printer
import reader
from mal_types import MalException

PROMPT = 'user> '


def log_print(*args):
    pass
    # print(*args)


def READ(line: str) -> list:
    log_print(f'READ {line}')
    return reader.read_str(line)


def EVAL(line: list) -> list:
    log_print(f'EVAL {line}')
    return line


def PRINT(line: list) -> str:
    log_print(f'PRINT {line}')
    return printer.pr_str(line)


def rep(line: str) -> str:
    val = line
    try:
        val = READ(val)
        val = EVAL(val)
        val = PRINT(val)
    except MalException as e:
        print(str(e))
    return val


def loop():
    while True:
        line = input(PROMPT)
        print(rep(line))


try:
    loop()
except EOFError:
    # Expected
    pass
