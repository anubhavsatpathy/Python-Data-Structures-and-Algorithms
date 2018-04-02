import stack_adt

def reverse_file(filepath):
    """
    Reverse a given text file and overwrite the same path
    :param filepath: The path of the file that needs to be reversed
    :return: void - modifies the file @ filepath
    """
    stack = stack_adt.ArrayStack()
    orig = open(filepath, 'r')
    for line in orig:

        stack.push(line.rstrip('\n'))
    orig.close()

    out = open(filepath,'w')
    while not(stack.is_empty()):
        out.write(stack.pop() + '\n')

    out.close()

def is_matched(expr):

    stack = stack_adt.ArrayStack()
    left = "[{("
    right = "]})"

    for c in expr:

        if c in left:

            stack.push(c)

        if c in right:

            if stack.is_empty():
                return False
            elif right.index(c) != left.index(stack.pop()):
                return False

    return stack.is_empty()





if __name__ == "__main__":

    filepath = "C:\\Users\\Admin\\PycharmProjects\\Data_Structures_Algo\\reversal.txt"

    reverse_file(filepath)

    expression = "[5 + {2}]"

    print(is_matched(expression))




