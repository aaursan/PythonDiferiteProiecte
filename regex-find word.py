import re

text = 'In the 1950s, Central American commercial banana growers were facing the death of their most lucrativE product, the Gros Michel bananA, known as Big Mike. And Now it’s happening again to Big Mike’s successor – the Cavendish.With its easily transported, thick-skinned and sweet-tasting fruit, the Gros Michel banana plant dominated the plantations of Central America. United Fruit, the main grower and exporteR in South America at the time, mass-produced its bananas in the most efficient way possible: it cloned shoots from the stems of plants instead of growing plants from seeds, and cultivated them in densely packed fields.Unfortunately, these conditions are also perfect for the spread of the fungus Fusarium oxysporum f. sp. cubense, which attacks the plant’s roots and prevents it from transporting water to the stem and leaves. The TR-1 strain of the fungus was resistant to crop sprays and travelled around on bootS or the tyres of trucks, slowly infecting plantations across the region. In an attempt to escape the fungus, farmers abandoned infected fields, floodeD them and then replanted crops somewhere else, often cutting down rainforesT to do so.Their efforts failed. So, instead, they searched for a variety of banana that the fungus didn’t affect. They found the Cavendish, as it was called, in the greenhouse of a British duke. It wasn’t as well suited to shipping as the Gros Michel, buT its bananas tasted good enough to keep consumers happy. Most importantly, TR-1 didn’t seem to affect it. In a few years, United Fruit had saved itself from bankruptcy by filling its plantations with thousands of the neW plants, copying the samE monoculture growing conditions Gros Michel had thrived in.While the operation was a huge success foR the Latin American industry, the Cavendish banana itself is far from safe. In 2014, South East Asia, another major banana producer, exported four million tons of Cavendish bananaS. But, in 2015, its exports haD droppeD by 46 per cent thanks to a combinatioN of another strain of the fungus, TR-4, and bad weather.'


print(text)

print

for pattern in [ r'(\b\w*Big\b\w*)'          # word at start of string


                ]:

   regex = re.compile(pattern)

   match = regex.search(text)
   s=match.start()
   e=match.end()
   print('%2d : %2d = [%s] ' % (s,e,text[s:e]))
   print('Matching "%s"' % pattern)

   print('  ' ,match.group())

   print

