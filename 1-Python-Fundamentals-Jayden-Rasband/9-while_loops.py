print("While loop")
# While loop
count = 0
while count < 5:
    print("Count : ",count)
    count += 1

print("While loop with break")
# While loop with break
count = 0
while True:
    print("Count : ",count)
    count += 1
    if count == 5:
        break

print("While loop with continue")
# While loop with continue
count = 0
while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print("Count : ",count)


print("While loop with else")
# While loop with else
l = 0
while l < 5:
    l += 1
else:
    print("Finally done!")

print("While loop with else and break")
# While loop that counts down from 10 to 0
count = 10
while count >= 0:
    print("Count: ",count)
    count -= 1

print("While loop that counts down from 10 to 0 using a step size of -1")
# While loop that counts down from 10 to 0 using a step size of -1
count = 10
while count >= 0:
    print("Count: ",count)
    count -= 1
