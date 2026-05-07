- Est-ce que la facon dont j'ai créé les fichiers jusqu'ici et la facon dont 
  j'ai utilisé leur contenu, est-ce que je respecte l'architecture hexagonale ?

- l'utilisateur upload le fichier, le fichier est lu par pymupdf qui est rapide à ce niveau, 
il nous transmet le contenu texte brut, qui est reçu par les préprocesseurs, 
le premier préprocesseur qui est là pour normaliser, n'a pas des problèmes pour 
le moment, ni celui qui doit nettoyer, ni meme celui qui tokenise. Mais quand on commence 
à calculer le tf, mama eh, c'est là que le problème est bien visible, imagine un document de 300 pages, 
avec plus de 3000 mots uniques sur 29000 mots en général, le tf doit se calculer sur 
chaque mot unique en parcourant tous les mots, donc selon moi là, on a donc 3000 * 29000, 
qui vaut des millions de tours, là l'utilisateur doit attendre meme jusqu'à 30 minutes
pour une génération de mot clé que nous avons promise pour quelques secondes. 
Et là, on signale que les prétraitements est encore basique, donc on n'a 
pas encore commencé à nettoyer les stops words pour l'anglais et le français.