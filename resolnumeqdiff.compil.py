# -*- coding: utf-8 -*-
"""
script pour compiler le fichier tex principal. Il peut contenir des insertions de fichiers tex ou de figures. Les figures sont crées par divers scripts.
Les données de compilation sont rassemblées dans une liste:
[nom fichier image, nom fichier source, nom langage script, [options commande] ]
  les clés sont les fichiers pdf
  les valeurs sont des listes. Chacune permettant de créer le fichier pdf 
"""

import depot.compil as cpl

# compilation tex principal
compil_texppal = cpl.Compil("resolnumeqdiff.pdf","resolnumeqdiff.tex","latexmk",["-pdf"])
#date de la dernière compilation du fichier principal
date_compil_ppal = compil_texppal.date_compil()

#insertion  du préambule ipt.tex
compil_ipttex = cpl.Compil("ipt.tex","ipt.tex")
if date_compil_ppal < compil_ipttex.date_compil():
    compil_texppal.a_exec = True
    print(compil_ipttex.image, " modifié")

# compilation python de la figure
compil_fig = cpl.Compil("resolnumeqdiff_1.pdf","resolnumeqdiff_1.py","python3")
if compil_fig.a_exec :
    print("compilation de " + compil_fig.source + " avec " + compil_fig.langage)
    compil_fig.exec()
    compil_texppal.a_exec = True
    
#scripts asymptote créant des figures pdf incluses
#compil_figx = Compil(["resolnumeqdiff_x.asy", "resolnumeqdiff_x.asy","asy"])
    
#compilation principale
if compil_texppal.a_exec :
    print("compilation de " + compil_texppal.source + " avec " + compil_texppal.langage)
    compil_texppal.exec()

"""
            à développer pour automatiser 
# à partir du nom de ce script
# se débarasser du .compil.py pour former 
# le nom principal
moi = os.path.splitext(__file__)[0]
moi = os.path.splitext(moi)[0]

#nom du fichier source tex principal
moi_tex= moi + '.tex'

#nom du fichier pdf principal produit
moi_pdf = moi + '.pdf'
"""
