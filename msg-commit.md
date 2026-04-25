# fix: corrige l'erreur `ModuleNotFoundError: No module named 'Domain'`

On importait les modules personnalisés avec des imports absolus comme `from Domain...`, alors que l’application est chargée par `fastapi dev` comme un module du package `src`.

Dans ce contexte, `Domain` n’existe pas à la racine du chemin d’import, ce qui provoquait l’erreur `ModuleNotFoundError: No module named 'Domain'`.

Cette modification remplace donc les imports absolus par des imports relatifs dans les modules concernés, afin de respecter la structure réelle du 
package Python et permettre à `fastapi dev ./src/server.py` de démarrer correctement. 