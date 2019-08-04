
def is_balance(expr):
    s = []

    for i in range(len(expr)):
        if expr[i] in ['{', '[', '(']:
            print('append ', expr[i])
            s.append(expr[i])
            continue

        if not s:
            return False

        pre = s.pop()
        if expr[i] == ']' and pre == '[':
            print('check ', expr[i])
            continue
        elif expr[i] == '}' and pre == '{':
            print('check ', pre, expr[i])
            continue
        elif expr[i] == ')' and pre == '(':
            continue
        else:
            return False
    if s:
        return False
    else:
        return True

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    entries = []
    result = []
    for line in queries:
        if line[0] == 'add':
            entries.append(line[1])
        elif line[0] == 'find':
            ret = 0
            for entry in entries:
                if entry.startwith(line[1]):
                    ret += 1
            result.append(ret)
    return result

def atoi(string):
    res = 0

    for i in xrange(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))

    return res
