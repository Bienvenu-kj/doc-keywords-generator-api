# fix : corrige le mauvais calcul de l'IDF score


## constat du problème
Parmi le problème que nous avons constaté dans les changements precedents, figure le problème 
du calcul incorrect de l'IDF, ce n'est pas directement un calcul incorrect, mais une verification,
qu'un term est bien dans les terms du document encours, qui échouait dans tous les cas, et 
ce qui faisait que le nombre de documents dans lesquels le term est trouvé était toujours 1, 
conduisant ainsi à un score IDF similaire pour tous les terms du document.

---
## Le pourquoi (cause)
Mais pourquoi la verification renvoyait toujours `False` ? Eh bien, c'est parce que quand nous 
voulons calculer le IDF, nous devons avoir la valeur représentant `le nombre des documents` dans 
lesquels apparait le term. Mais pour trouver cette valeur, il nous fait tester l'appartenance du term 
à la liste des terms uniques du document encours, alors que le term vient déjà avec une valeur TF déjà 
défini à une valeur differente de 0 au moment où les termes de chaque document du corpus ont leur 
valeur TF à zéro, alors quand l'opérateur `in` régarde si un term du document a la même structure 
et les mêmes valeurs que le terme en cours, ne trouve rien.

---
## Solution
Alors voilà pourqoui, nous avons trouvé une solution qui consistait à déclarer une variable qui va 
stocker la copie du term, puis on modifie le TF de cette copie et on met ça à 0, puis on teste 
l'appartenance avec ce copi, et directement l'opérateur `in` trouve bien un term qui a non 
seulement la même structure, mais surtout les mêmes valeurs : nom, is_n_gram, tf_score…, et incremente 
la valeur là dont on a parlé, et là, la valeur IDF est bien exact.

---
## Resultat : 

Avec ça, on arrive bien à balayer les mots sans importance, les stopwords sont tous ignorés 
et on garde uniquement les terms qui ont de l'importance par rapport au document.