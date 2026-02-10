#dictionary

fitness_dictionary = {"banana":100, "apple":200, "orange":300}
print("fitness_dictionary")
print(fitness_dictionary)
print(list(fitness_dictionary.values()))
fitness_dictionary["banana"] = 125
print(list(fitness_dictionary.values()))
print(fitness_dictionary.get("apple",0))
print(fitness_dictionary.get("orang",0))

mixed_dictionary = {"key1":100,"key2":3.14,"key3":[1,2,3]}
print("mixed_dictionary")
print(mixed_dictionary)
print(list(mixed_dictionary.values()))
print(mixed_dictionary["key3"][1])

last_dictionary = {"k1":10,"k2":[10,20,30,40,50],"k3":"string","k4":{"a":100,"b":200}}
print("last_dictionary")
print(last_dictionary)
print(last_dictionary["k2"][3])
print(last_dictionary["k4"]["b"])
