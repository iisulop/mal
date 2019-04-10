PROMPT = 'user> '


def READ(line: str) -> str:
    return line

def EVAL(line: str) -> str:
    return line

def PRINT(line: str) -> str:
    return line

def rep(line: str) -> str:
    return line

def loop():
    while True:
        line = input(PROMPT)
        print(rep(line))

try:
    loop()
except EOFError:
    # Expected
    pass

