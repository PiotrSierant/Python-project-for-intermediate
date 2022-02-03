import shelve
from ContactBook import *
print(open('ContactBook.dir').read())


db = shelve.open('ContactBook')
print('Amount contact: {} \n {}'.format(len(db), list(db.keys())))

rec = db['Peter Sierant']  # wyswietlanie za pomoca __str__ z klasy
print(rec)

# print(list(db))
db.close()
