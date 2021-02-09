# import re
# text = 'abbaaabbbbaaaaa'
# pattern = 'ab'
# for match in re.finditer(pattern, text):
#  print('Found "%s" in textul de mai sus la pozitia "%d"' % (match.group(), match.start()))
import re
text = 'Acesta este un text unde o sa cautam un cuvant text in tot textul.'
pattern = re.compile(r'\b\w*text\w*\b')