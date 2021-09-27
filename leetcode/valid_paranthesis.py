

def valid_param(s):
    d = {'}':'{',']':'[',')':'('}
    stack = []
    end = d.keys()
    for char in s:
        if char in end: 
            if ( not stack ) or stack.pop() != d[char] :
                return False
        else:
            stack.append(char)
        print(stack)
    return len(stack) == 0


s = r']'
print(valid_param(s))