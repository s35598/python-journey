#sets

myList = [10,20,30,10,20,40,10,20,40]
mySet = set(myList)
print(mySet)

mySet.add(10)
mySet.add(50)
print(mySet)

mySet2 = [70,80,10,20]
mySet3 = mySet.union(mySet2)
print(mySet3)

mySet4 = mySet.intersection(mySet2)
print(mySet4)

countryList = ["de","fr","fr","tr","tr","tr","nl"]
print("Total sale: ", len(countryList))
print("How many countries we sold product: ", len(set(countryList)))
# eğer print ederken aynı tür değilse artı(+) yerine virgül(,) kullanmamız gerekir.

emptySet = set() #eğer boş bir set,dict,list oluşturmak istersek hepsinde aynı şekilde yapmamız lazım. {} koyarsak dict () koyarsak tuple [] list olarak algılar default olarak
emptySet.add(10)  # çoklu eleman eklemek istersek add ile ekleyemeyiz
emptySet.update([10,20,30,40]) # çoklu eleman için doğru yol "update"
print("emptySet")
print(emptySet)