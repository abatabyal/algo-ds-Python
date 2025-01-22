def braces(values):
    op = []
    count = 0
    for i in values:
        s = []
        count += 1
        for v in range(0, len(i)):
            if i[v] == '(' or i[v] == '{' or i[v] == '[':
                s.append(i[v])
                continue

            if len(s) == 0:
                op.append('NO')
                break

            if i[v] == ')':
                x = s.pop()
                if x == '{' or x == '[':
                    op.append('NO')
                    break

            elif i[v] == '}':
                x = s.pop()
                if x == '(' or x == '[':
                    op.append('NO')
                    break

            elif i[v] == ']':
                x = s.pop()
                if x == '(' or x == '{':
                    op.append('NO')
                    break
        if len(s) == 0:
            op.append('YES')
        if len(s) and len(op) != count:
            op.append('NO')
    return op

values = ['{}[]()', '{[}]{']
print(braces(values))