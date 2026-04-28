# refactor : approfondissement de notre usage de l'architecture hexagonale

Nous avons profondément revu la façon dont nous avons utilisé l'architecture hexagonale dans ce projet.

Voici en détail ce que nous avons changé :

- ## models :
            nous avons retiré `pydantic` de nos objets métiers principaux afin que le `Domain`
            décrive d'abord le métier lui-même, sans être attaché à une contrainte de sérialisation
            ou de validation externe.

            Dans cette même logique, nous avons sorti de `Domain/models` les fichiers
            `keyword_request.py` et `keyword_response.py`, car ils ne décrivaient pas des
            concepts du métier, mais des objets de circulation de données.

            Nous avons aussi gardé `document_path` comme `str`, parce que nous avons constaté
            que le chemin du document n'est pas une information centrale pour la logique métier.
            C'est une information secondaire, fournie par les adaptateurs selon l'endroit où ils
            vont chercher les documents.
            Le domaine n'a donc pas besoin d'être lié à `Path` ou à une représentation plus
            technique venant de l'extérieur.

---

- ## application :
           nous avons introduit une nouvelle couche `application`, pour porter ce qui relève
           des cas d'usage applicatifs de notre système.

           Cette couche contient maintenant deux dossiers :
           - `dto`
           - `use_cases`

           Le dossier `dto` contient les `Data Transfer Objects`, c'est-à-dire les objets dont
           le rôle est de faire circuler les données entre couches dans une forme adaptée.
           Ces objets ne sont pas là pour représenter le coeur du métier, mais pour transporter
           les données d'entrée et de sortie de manière propre.

           Le dossier `use_cases` contient les actions applicatives du système, c'est-à-dire les
           opérations complètes qu'un point d'entrée peut demander au système d'exécuter.
           Pour le moment, cela correspond essentiellement aux actions exposées par les endpoints
           de l'API.

---

- ## Domain :
            nous avons remis au `Domain` une part de responsabilité qui lui revient,
            notamment autour de la préparation des termes et de la construction logique du corpus.

            L'idée ici n'était plus de laisser l'infrastructure décider à la place du domaine
            comment enrichir un document, mais bien de faire en sorte que le domaine conserve
            l'autorité sur les transformations qui appartiennent à la logique métier.

            Nous avons aussi pris en compte le fait que nos objets métiers sont maintenant des
            objets Python purs.
            Par conséquent, lorsque la couche `application` doit encore utiliser `pydantic`
            pour structurer une réponse, elle ne peut plus exposer directement ces objets métiers
            comme s'ils étaient eux-mêmes des modèles Pydantic.
            Nous avons donc adapté le DTO de réponse pour qu'il transforme explicitement les
            objets métiers Python en structure sérialisable côté application.

---

- ## infrastructure :
          ici, nous avons réduit les responsabilités techniques à ce qui leur appartient
          réellement.

          Le cas principal est `fs_corpus_repository.py`, qui allait auparavant trop loin dans
          le traitement : lecture des fichiers, extraction du contenu, préparation des termes et
          construction d'un corpus presque complet.

          Nous avons réduit cette responsabilité afin qu'il se concentre surtout sur :
          - la lecture des documents
          - la vérification de la lisibilité des PDF
          - la remise d'une liste de `Document` avec leur contenu brut

          Cela remet la frontière au bon endroit :
          l'infrastructure récupère les données techniques,
          tandis que le domaine décide quoi faire de ces données.

---

## Important à savoir

Ce que nous devons signaler est que nous avons vraiment changé beaucoup de choses,
mais voici les plus capitales :

- Nous avons changé la façon dont nous pensions l'architecture hexagonale
- Nous avons compris qu'une architecture hexagonale ne consiste pas seulement à bien ranger les fichiers,
  mais à bien répartir l'autorité entre métier, application et technique
- Nous avons compris qu'il existe une couche `application` chargée d'orchestrer le domaine
  et l'infrastructure pour répondre aux attentes des utilisateurs
- Nous avons compris que tout besoin du domaine de parler avec l'extérieur doit passer
  par des `ports`, sans pour autant conclure que toute logique doit immédiatement devenir
  une abstraction
- Nous avons compris que retirer `pydantic` du domaine implique aussi d'assumer explicitement
  la transformation des objets métiers vers les DTO de sortie

En résumé, cette refactorisation ne concerne pas seulement l'organisation des dossiers.
Elle corrige surtout notre manière de distribuer les responsabilités entre les couches,
et notre manière de faire cohabiter objets métiers purs et objets de transfert applicatifs.
