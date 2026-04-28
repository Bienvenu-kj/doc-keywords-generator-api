# refactor : factorise l'architecture

Voici ce que nous venons de faire dans ces changements : 
- **application**: nous venons d'enrichir le `KeywordGenerationRequest`pour faire 
                   en sorte qu'il ne contient que le nombre de keywords que 
                   l'application doit générer et le fichier depuis lequel générer 
                   les mots-clés.
---
- **infrastructure**: c'est ici que repose la factorisation dont on a pas parlé 
                      dans le titre du commit, voici ce que nous avons vraiment fait :
                      dans les `outils`, nous avons régroupés les taches en dossiers 
                      et dans chaque dossier un fichier par technologie qui réalise 
                      cette tâche.
                      Pour le moment, nous avons des :
                       - `readers`: avec un fichier qui implémente une classe `PymupdfReader`
                       - `document_content_preparators` : avec un fichier qui implémente une fonction `pymupdf_get_document_content`
---

## NB : 
Donc, nous avons repensé la facon d'utiliser certaines fonctions et nous les avons rendus encore plus intelligentes et extensibles, tout en permettent le choix de la méthode ou de la technologie d'implémentation.