# IPT2

Dépôt de fichiers sources pour la création de documents relatifs à l'enseignement de l'IPT (informatique pour tous) en MPSI.

Ces documents d'enseignement sont des fichiers pdf d'extension .doc.pdf créés par LaTex.

Les fichiers de ce dépôt sont  des scripts (tex, py, asy) qui produisent des fichiers pdf. Ce dépôt contient aussi quelques fichiers pdf pour les figures qui ne sont pas produites par un script. 
Deux types de fichiers pdf interviennet: les documents et les figures qui y sont incluses.

Pour créer les documents, il faut exécuter les scripts tex qui les génèrent. Mais ces scripts incluent d'autres scripts tex qui n'ont pas à être exécutés seuls ainsi que des figures en pdf elles mêmes produites par des scripts (asy ou python) qui doivent éventuellement (en cas de modification) être exécutés avant. Ils incluent aussi parfois des lignes de code python issues de fichiers Python.

On adopte une convention de nommage:

    les scripts qui génèrent des documents: nom.doc.tex. Le document produit est nom.doc.pdf
    les scripts qui génèrent des figures:  nom_fig.py ou _fig.asy. La figure produite est nom_fig.pdf

Noter le _fig en effet .fig.pdf est interprété comme une extension particulière par latex qui refuse alors d'insérer les figures. Les inputs et les includegraphics doivent contenir le nom complet avec l'extension .tex ou .pdf 
Inventaire des types de fichiers tex dans IPT2

    TPannnu(E|C)doc..tex
    Sannu(E|C)doc.tex
    (C|E)nom.tex
    Anom.doc.tex
    ipt.tex
    nom.cours.tex et nom_beam.cours.tex
    exo_nom_(C|E).tex
    exo_nom_A.doc.tex
