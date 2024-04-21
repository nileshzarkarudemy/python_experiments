# Membership operators in python
# in, not in, is, not is

x = 5
y = 10
z = 100

# The in operator is used to check if a sequence is present in an object.
print("5 in [1, 2, 3, 4, 5] ",x in [1, 2, 3, 4, 5])
print("10 in [10, 20, 30, 40, 50] ",y in [10, 20, 30, 40, 50])
print("100 in [10, 20, 30, 40, 50] ",z in [10, 20, 30, 40, 50])

# The not in operator is used to check if a sequence is not present in an object.
print("5 not in [1, 2, 3, 4, 5] ", x not in [1, 2, 3, 4, 5])
print("10 not in [10, 20, 30, 40, 50] ",y not in [10, 20, 30, 40, 50])
print("100 not in [10, 20, 30, 40, 50] ",z not in [10, 20, 30, 40, 50])

x = 3 
print("x in range(3) : ",x in range(3)) # x is started countting from 0
for i in range(3):
    print(i)

files = ['test.py','test.csv','test.txt'] 
print("'test.xml' not in files",'test.xml' not in files)
print("'test.py' in files",'test.py' in files)  


guest_list = {
    'Alice': 45,
    'Bob': 21,
    'Charles': 78,
    'David': 52,
    'Tony': 34
}
print("Alice in guest_list", 'Alice' in guest_list)
print("Jessica in guest_list", 'Jessica' in guest_list)


# The is operator is used to check if two object references are the same
a = [1, 2, 3]
b = [1, 2, 3]
print("a is b ",a is b)

# The is not operator is used to check if two object references are not the same
print("a is not b", a is not b)

# Be careful with the is operator, it checks if the object references are the same.
# It does not check if the objects are equal.
# For checking if two objects are equal, we use the == operator.
