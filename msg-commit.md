# Domain quasi prêt pour le test

Nous venons de mettre en place une version presque déjà prête de notre Domaine

Nous avons déjà ajouté des :

- `models` (entities) qui sont les objets qui représentent les différents 
éléments que nous allons manipuler

- `ports` (interfaces ou contracts) 
qui vont pouvoir communiquer avec les `adapters` que nous allons 
implementer d'ici peu pour tester le Domaine.

- `services` (use-cases) qui représentent la logique metier


## Prochaines étapes
- Ajouter des `adapters` simples
- et tester la logique avant d'ajouter les `adapters` complexes

**NB** : Nous avouons le fait que nous soyons trop minimaliste jusqu'ici, les raisons sont bien là :
- `Python` est un langage que j'avais longtemps abandoné, mais je suis en train de vouloir me récupérer ;
- Je suis en train d'utiliser une architecture que je viens de découvrir à peine.
