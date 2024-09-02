# This is a raw python file
# The code here is the same as in our notebook files, but without the markdown cells that make it website-like. 
# This is how we'd write a "normal" program - write code in several .py files, run them to execute the program.
# We don't use these files much, as we normally want to see and interact with the output as we go.

name = "akeem"
i = 0
height = 72.5
my_numbers = [i,height, 0]

print(name)
print("is this many inches tall:")
height

print(type(name))
print(type(i))

print(i)
i = i + 1
print(i)

testBool = True
testTouple = (1,2)
testChar = 'a'

print(type(testBool))
testBool = "Apple"
print(type(testBool))

my_stuff = [name, i, height, "this measures my height"]
my_stuff

print(my_numbers)
my_numbers.append(1)
print(my_numbers)
my_numbers.pop(1)
print(my_numbers)

print(my_stuff[0])
print(my_numbers[2])

my_length = len(my_stuff)
print(my_length)
print(my_stuff[my_length - 1])

my_tuple = ("akeem", "semper")
print(my_tuple[0])
print(my_tuple[1])

print(my_tuple[0:2])
print(my_tuple[0]+ " " + my_tuple[1])