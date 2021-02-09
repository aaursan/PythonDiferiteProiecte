print("Folosim functia search din regexp ne ajuta sa cautam daca un text (la-nceput) se gaseste in alt text\n\n")
import re
paternuri = ['aici' , 'acolo']
text = 'aici invatam Python regular expresion, pe care le putem folosi acolo in exercitii'
for patern in paternuri:
 print('Cautam paternul "%s" in textul "%s" -> ' % (patern, text))
 if re.search(patern, text):
  print("se potriveste")
 else:
  print("nu se potriveste")
print("\n\n re search - pentru a afla pozitia de potrivire\n\n")

paternuri = 'aici'
text = 'aici invatam Python regular expresion, pe care le putem folosi acolo in exercitii, aici putem invata'
potrivire = re.search(paternuri, text)
start = potrivire.start()
end = potrivire.end()
print(start)
print(end)
print('Gasim "%s" in "%s" de la %d pana la %d ("%s")' % \
 (potrivire.re.pattern, potrivire.string, start, end, text[start:end]))