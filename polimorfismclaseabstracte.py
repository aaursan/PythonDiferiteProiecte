class Document:
     def __init__(self,name):
           self.name=name
     def show(self):
           raise NotImplementedError("sublcasa terbuie sa implemneteze meoda abstracta")
class Pdf(Document):
     def show(self):
           return'Show pdf contents!'

class Word(Document):
     def show(self):
           return"Show word contents!"
#mai adugam o clasa
class MOBI(Document):
    def show(self):
           return"8888"

documents=[Pdf('Document1'),Pdf('Document2'),Word("Document3"),MOBI("Document4")]
for document in documents:
        print (document.name + ':' +document.show())#pot apela direct fctia show



