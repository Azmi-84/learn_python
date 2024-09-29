name = "azmi-84"
id = 123
float = 3.14
is_ok = True

print(name)
print(id)
print(float)
print(is_ok)

name = "azmi"
id = 456
float = 4.12
is_ok = False

print(name)
print(id)
print(float)
print(is_ok)

if name == "azmi":
    print("hello azmi")
if id == 456:
    print("hello azmi")
if float == 4.12:
    print("hello azmi")

if name == "azmi" and id == 456 and float == 4.12:
    print("hello azmi")

if name == "azmi" or id == 456 or float == 4.12:
    print("hello %s" % name)
