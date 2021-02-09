try:
   import cPickle as pickle
except:
   import pickle

import pprint

data1 = [{'a':1.2, 'b':2.3, 'c':3.7}]
print('Inainte de serializare: ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)
print('\n')
print('\n')
print('Cum arata stringul dupa serializare')
pprint.pprint(data1_string)
print('\n')
print('\n')
data2 = pickle.loads(data1_string)
print('Cum arata dupa incarcam iar serializarea in ce era inainte folosint load: ')
pprint.pprint(data2)
print('Sunt obiectele identice?:', (data1 is data2))
print('Sunt obiectele egale?:', (data1 == data2))