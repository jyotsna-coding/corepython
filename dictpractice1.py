dict1 = {}
list = [('James',112233454),('Andy', 223344551),('James', 33445121)]

for name, phno in list:
    try:
        dict1[name].append(phno)
    except KeyError:
        dict1[name] = [phno]
print(dict1)