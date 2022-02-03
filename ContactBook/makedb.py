from ContactBook import *
import shelve

db = shelve.open('ContactBook')
for object in (nickname1, nickname2, nickname3):
    db[object.name] = object
db.close()
