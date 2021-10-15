# SymbolTable 
  - Uses HashTable
  - HashTable size is constant
  - Collisions are resolved with linked lists
  - The position of the token is calculated as follows: position = offset * size + hash(token)

## insert(token, value)
  - Inserts a token and its value in the symbol table
  - Post: Returns the position of the inserted token

## find(token)
  - Post: returns the positions inside the symbol table or -1 if it doesn't exist

## get(position)
  - Post: return the token from a given position or -1 if it doesn't exist

#github repo: https://github.com/berlaewald/SymbolTable
