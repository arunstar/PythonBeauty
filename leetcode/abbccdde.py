

def format_string(s):
    result = []
    result.append(s[0])
    val = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            val += 1
        else:
            if val > 1:
                result.append(str(val))
            result.append(s[i])
            val = 1
    return "".join(result)


print(format_string("aaabccdeef"))