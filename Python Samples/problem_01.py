def rep_dup(s):
    char = string[0]
    new_string=s.replace(char, '$')
    new_string=char+new_string[1:]
    return new_string

string=str(input('Give a string='))
print(rep_dup(string))