aname = "basic learning of python"
print(aname.index("python"))
print(aname.index("p"))
print(aname.count("p"))
print(aname.count("n"))
print(aname.find("n"))
print(aname[3:6])

# Start from index 3 (i).
# Select every 2nd character → Index 3 is i, index 5 is a space ' '.
print(aname[3:6:2])

print(aname[3:6:1])
#  it doesn't work cuz it is not in the range
# print(aname[3:6:0])

print(aname[::-1])
print(aname[::-2])

print(aname.upper())
print(aname.lower())

print(aname.replace("python", "java"))

print(aname.split(" "))

print(aname.split(" ", 1))

print(aname.split(" ", 2))

print(aname.startswith("basic"))

print(aname.endswith("python"))
