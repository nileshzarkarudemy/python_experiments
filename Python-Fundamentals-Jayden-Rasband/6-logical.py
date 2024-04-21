# Logical operators in python
# and = &
# or = | 
# not = !=

# Logical AND
print("True and True : ",True & True)
print("True and False : ",True and False)
print("False and True : ",False and True)
print("False and False : ",False and False)

# Logical OR
print("True or True : ",True or True)
print("True  or False : ",True  or False)
print("False or True : ",False or True)
print("False or False : ",False or False)

# Logical NOT
print("not True : ",not True)
print("not False : ",not False)

# Using logical operators in if statements
age = 20
if age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a kid or an elder")

# Short circuiting
print("True and False or True : ",True and False or True)
print("False or True and True : ",False or True and True)

# Precedence
print("not False and True or False : ",not False and True or False)
