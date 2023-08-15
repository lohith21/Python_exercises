## use %i to format integers:

age = 25
message = "I am %i years old." % age
print(message)

age = [23, 25, 22, 27]
message = "I am %i years old." % age[2]
print(message)

## Using str.format():

age = 25
message = "I am {} years old.".format(age)
print(message)

##Using f-strings:

age = 25
message = f"I am {age} years old."
print(message)
