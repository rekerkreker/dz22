def check(text:str):
    for i in range(1, int(len(text) / 2)+ 1):
        if set(text.split(text[0:i])) == {''}:
            return True
    return False
a = input('Input:')
print(check(a))

assert check("a") == False

assert check("abab") == True

assert check("ababab") == True

assert check("aba") == False

assert check("abcabcabcabc") == True

assert check("aaxxtaaxztaaxxt") == False