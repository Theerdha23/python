# Python Basics

This repository contains examples and practice code for learning Python fundamentals.  
It demonstrates how different data types work, how mutable and immutable objects behave, and how to inspect object identities with `id()`.

---

## 📚 Topics Covered
- **Data Types**
  - Integers (`int`)
  - Strings (`str`)
  - Booleans (`bool`)
  - Lists (`list`)
  - Dictionaries (`dict`)
  - Tuples (`tuple`)
  - Sets (`set`)
  - Bytes (`bytes`)
  - Bytearray (`bytearray`)

- **Mutability**
  - Immutable: `int`, `str`, `tuple`, `bytes`
  - Mutable: `list`, `dict`, `set`, `bytearray`

- **Object Identity**
  - Using `id()` to check memory references
  - Understanding how immutable objects create new IDs when modified
  - Seeing how mutable objects keep the same ID when updated

---

## 🚀
Example Code
```python
m = 120
print(type(m), id(m))

h = "harry"
print(type(h), id(h))

l = ["theerdha", 2, 99]
print(type(l), id(l))

s = {1, 2, 3}
print(type(s), id(s))

theerdha = {'name': 'theerdha', 'age': 12}
print(type(theerdha), id(theerdha))

t = (1, 2, 3)
print(type(t), id(t))
