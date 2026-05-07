

- ✅ correction de la formule et du contrat de calcul IDF 
- ✅ nouveau port pour la preparation du document 
- ✅ Changer la structure de la fonction `pymupdf_get_document_content` 
  en une classe `InMemoryPYmuPDFDocumentContentExtractor`
  qui implémenté le port dont on a parlé en haut

- ✅ Adapter le code present a ce nouveau port et voir s'il y a 
  d'autres fonctions de l'infrastructure qui doit avoir à implementer un port
- ✅ Creation d'un service qui centralise le processus de prétraitement pour éviter la repetition du meme code au niveau de `corpusService` et au niveau de `GenerateKeywordsUseCase`