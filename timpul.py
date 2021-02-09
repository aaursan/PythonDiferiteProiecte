import time

print('Timpul curent este: ' + str(time.time()))
print('Timpul curent este: ' + str(time.ctime()))
later = time.time() + 30
print('Timpul curent plus 30 de secunde: ' + str(time.ctime(later)))