d = { "sammy" : "alaniz",
      "summer" : "moon"   }

print(d)

item = "sammy"

if item in d:
    print("contains item")


from collections import defaultdict

def def_value():
    #return "not present"
    return list

d = defaultdict(def_value)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])