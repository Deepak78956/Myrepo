from Stack import Stack
def infix_to_postfix(strexp):
    tokenList = strexp.split()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    postList = []
    opStack = Stack()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and (prec[opStack.peek()] >= prec[token]):
                postList.append(opStack.pop())
            opStack.push(token)
    while not opStack.is_empty():
        postList.append(opStack.pop())
    return " ".join(postList)
print(infix_to_postfix("A * B + C * D"))