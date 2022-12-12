def fun_generator():
	yield "Hello world!!"
	yield "Geeksforgeeks"


obj = fun_generator()

print(type(obj))

print(obj)
print(next(obj))
print(next(obj))
#print(next(obj)) causes stop iteration
