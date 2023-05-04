def validity(s) :
    brackets = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []
    for i in s:
        if i in brackets.keys() :
            stack.append(i)
        elif i == brackets[stack[-1]] :
            stack.pop()
        else:
            return False
    return stack == []            

string = input("Enter your string that includes only (, ) , [, ], { ,}:  ")
print(validity(string))

