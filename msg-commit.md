# refactor: renforce les ports du domaine et unifie l'extraction/prétraitement des documents

## Constat
Les changements récents avaient amélioré le calcul de l'IDF, mais le flux global de lecture et de
prétraitement des documents restait encore fragile sur plusieurs points :

- le domaine recréait encore certaines implémentations concrètes au lieu de s'appuyer uniquement sur des ports ;
- le contrat d'extraction du contenu mentait sur sa vraie source de données en mélangeant chemin de fichier,
  état interne et upload HTTP ;
- le système de logs dépendait d'un utilitaire d'infrastructure directement utilisé dans le domaine ;
- le pipeline de prétraitement était dupliqué entre la construction du corpus et la génération de mots-clés.

## Objectif
Recentrer le domaine sur des contrats explicites et neutres, puis déplacer les détails techniques
vers la couche d'infrastructure ou de composition.

## Changements
- introduction d'un objet `DocumentSource` pour représenter une source de document de manière neutre ;
- renforcement du port `DocumentContentExtractor` et ajout d'un service dédié côté domaine ;
- refactor de l'extracteur PyMuPDF pour travailler à partir de `DocumentSource` ;
- centralisation du pipeline de prétraitement dans `PreprocessorService` ;
- injection des dépendances de prétraitement et d'extraction au lieu d'instancier les implémentations au milieu du flux ;
- introduction du port `CustomPrint` et d'un utilitaire de log piloté par contrat ;
- adaptation du `GenerateKeywordsUseCase`, du `CorpusService`, du repository fichier et du `server`
  pour composer correctement les dépendances ;
- correction du calcul/contrat IDF déjà amorcée, en cohérence avec le nouveau flux ;
- ajout du modèle `PreprocessingResult` pour transporter proprement les résultats intermédiaires.

## Résultat
Avec ce refactor :

- le domaine dépend mieux de ports que d'implémentations concrètes ;
- l'extraction du contenu ne dépend plus de `UploadFile` ni d'un chemin brut dans son contrat métier ;
- la préparation des documents est réutilisable entre corpus et génération de keywords ;
- le câblage de l'application est plus lisible et plus conforme à l'architecture hexagonale visée.
