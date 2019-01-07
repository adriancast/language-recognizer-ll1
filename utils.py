TERMINALS = ['p', 'f', 'i', 's', 'g', 'm', 'h']

def language_recognizer(word: str) -> bool:
    input = word
    is_recognized = True  # We really hope the word is accepted
    stack = []
    stack_push_word(stack=stack, word='P')
    while stack_not_empty(stack=stack) and read_input(input) and is_recognized:
        if stack_top(stack=stack) in TERMINALS:  # Case of terminals
            if stack_top(stack=stack) == read_input(input=input):
                stack = stack_pop(stack=stack)
                input = right_input(input=input)
            else:
                is_recognized = False
        else:  # Case of variables
            if stack_top(stack=stack) == 'P':
                if read_input(input=input) in ['p']:
                    stack = stack_pop(stack=stack)
                    stack = stack_push_word(stack=stack, word='pBf')
                else:
                    is_recognized = False
            else:
                if stack_top(stack=stack) == 'B':
                    if read_input(input=input) in ['i', 's', 'm']:
                        stack = stack_pop(stack=stack)
                        stack = stack_push_word(stack=stack, word='IB')
                    else:
                        if read_input(input=input) in ['f', 'g', 'h']:
                            stack = stack_pop(stack=stack)
                        else:
                            is_recognized = False
                else:
                    if stack_top(stack=stack) == 'I':
                        if read_input(input=input) in ['i']:
                            stack = stack_pop(stack=stack)
                            stack = stack_push_word(stack=stack, word='i')
                        else:
                            if read_input(input=input) in ['s']:
                                stack = stack_pop(stack=stack)
                                stack = stack_push_word(stack=stack, word='sBg')
                            else:
                                if read_input(input=input) in ['m']:
                                    stack = stack_pop(stack=stack)
                                    stack = stack_push_word(stack=stack, word='mBh')
                                else:
                                    is_recognized = False

    if read_input(input) or stack_not_empty(stack=stack):
        is_recognized = False

    return is_recognized


def stack_push_word(stack: list, word: str) -> list:
    for char in word[::-1]:  # Note that the str is reversed
        stack.append(char)
    return stack

def stack_top(stack: list):
    return stack[-1]

def stack_pop(stack: list):
    stack.pop()
    return stack

def stack_not_empty(stack: list):
    return len(stack) > 0

def stack_empty(stack: list):
    return len(stack) == 0

def read_input(input: str) -> str:
    return input[:1]

def right_input(input: str) -> str:
    return input[1:]
