
# Question 1
a = 5
b= 5
c = a == b
print(c) # True
# what is the output?

# Question 2
def find_most_char(s):
    #  Write logic
    d = {}
    for char in s:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1
    
    # max_char = max(d.items(),key=lambda x : x[1])[0]
    max_val = max(d.values())
    for k,v in d.items():
        if v == max_val:
            return k

s = 'aaabbbdcccc'
print(find_most_char(s))
# print max char from string
# For e.g :  s = 'aaabbbcccc'
# above should return letter 'c'
# which has maximum occurences