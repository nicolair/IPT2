import subprocess
import os.path

class Compil(object):
    "éléments d'une compilation élémentaire"
    def __init__(self,img,src,lng='',opts=[] ):
        self.image = img
        self.source = src
        self.langage = lng
        self.options = opts
        self.a_exec = os.path.getmtime(img) < os.path.getmtime(src)
        self.commande = [self.langage]
        for opt in self.options:
            self.commande.append(opt)
        self.commande.append(self.source)
        
    def exec(self):
        subprocess.run(self.commande)
        
    def date_compil(self):
        return os.path.getmtime(self.image)
