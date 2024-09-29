name = "azmi-84"
print("Assalamualaikum " + name)
print("Assalamualaikum {}".format(name))
print(f"Assalamualaikum {name}")
print("Assalamualaikum %s" % name)

data = [1, 2, 3]
print("{} {} {}".format(data[0], data[1], data[2]))
print("{2} {1} {0}".format(data[0], data[1], data[2]))
print("{data[0]} {data[1]} {data[2]}")
print("%d %d %d" % (data[0], data[1], data[2]))
