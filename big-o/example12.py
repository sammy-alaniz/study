
def permutation(string):
    permuations(string, "")

def permuations(string, prefix):
    if len(string) == 0 :
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1::]
            permuations(rem, prefix + string[i])


permutation("abcd")

sammy = "sammy"

print(sammy[0:1])
print(range(len(sammy)))