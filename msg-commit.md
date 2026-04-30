# feat : met enfin opérationnelle la génération de mots-clés

Enfin, la génération de mots-clés est opérationnelle et nous avons fait nos prémières générations

Dans ces changements :
## 1. Ajouts(*nouveautés*) : 
- **Les préprocesseurs natifs (`infrastructure.preprocessors_adapters`)**: Natifs pour signifier que nous avons uniquement utilisé du 
                                                    python pur. ce sont des adapters.
- **Un service pour la génération des mots clés (`domaine.services`)** : Nous avons ajouté un nouveau service pour faire la génération 
                                                    complète des mots clés en faisant en son sein les calculs du tf,
                                                    idf et tf_idf de chaque mot et retourne une liste de mot-clé 
                                                    dont le nombre peut aller jusqu'au nombre de mots-clés qu'a 
                                                    demandées le client.
---
## 2. Changements (Réajustement) :
- **Retour à l'utilisation complète de Pydantic** : Nous avons dans les changements précédents, abandonées `Pydantic` pour les objets
                                                    metiers, mais après avoir vu que l'api repose sur lui pour valider les requettes, 
                                                    nous avons repris son utilisation pour representer les objets metiers, mais nous 
                                                    allons voir comment limiter son utilisation hors du domaine.

- **Et d'autres détails pour faire fonctionner le code actuels** : Il y a bien sûr d'autres changements dont nous n'avons pas parlé 
                                                                   directement ici, mais qui ont été fait pour juste faire en sorte que 
                                                                   le code actuel puisse fonctionner sans problème. 
---
## NB : 
Mais nous avons déjà constaté le manque de precision et de justesse de nos preprocesseurs natifs, ils conduisent encore à des resultats indesirables.
Le premier teste sur un document, a presenté `/` comme étant le mot important du document, suivi du mot `command`, c'était un document qui montre 
les raccourcis de `Davinci resolve`, je ne sais pas si l'on peut faire de prédictions sur ces resultats là, vraiment, je n'ai pas encore de réponses pour le moment.

Mais, nous passons que la cause de ce manque de precision et de justesse est causé, d'une part, par le fait que le corpus est encore petit et non varié, de l'autre côté, 
nos préprocesseurs actuels ne sont pas sophistiqués pour bien préparer non seulement le corpus, mais aussi le document sur lequel on tire les mots-clés. 