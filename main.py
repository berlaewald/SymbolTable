from HashTable import HashTable

hashTable = HashTable()

nameIndex = hashTable.insert('name', 'Berla Ewald')
print("Positions of 'name': ", nameIndex)


passIndex = hashTable.insert('password', '123456')
print("Positions of 'password': ", passIndex)

randomVariableIndex = hashTable.insert('eman', 'random Variable')
print("Positions of 'eman' (collision with name): ", randomVariableIndex)

variableSymbolTest = hashTable.get(randomVariableIndex)     # should be 'eman' after the above operations
print("The symbol found at the index returned by inserting 'eman': ", variableSymbolTest)

namePositionTest   = hashTable.find('name')                 # should be 4 after the above operations
print("Position of token 'name': ", namePositionTest)