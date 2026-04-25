# Instructions du Projet : doc-keywords-generator-api

## Architecture
- Nous suivons une approche **Hexagonal Architecture** (Domain, Infrastructure).
- Les modèles Pydantic sont utilisés pour la validation des entrées/sorties.

## Conventions de Code
- Langue : Code en anglais et commentaires en français.
- Style : PEP 8 strict.
- Tests : Utiliser `pytest`. Chaque service de `Domain.services` doit avoir ses tests.

## Dépendances Préférées
- Extraction PDF et TXT : `PyMuPDF`.
- NLP : `spaCy` ou `nltk` (à confirmer selon les besoins).
- serveur Web : FastAPI

## Méthodes pour la génération de Keywords
Nous nous basons sur le modèle TF-IDF pour générer les mots clés, on peut toujours signaler son alternative.

## Façon de répondre  (Save_memory)
Soit toujours claire dans les explications, et vraiment technique, proposant et non imposant

## Workflows Spécifiques
- On se concentre d'abord sur Le Domaine, les implementations (infrastructures) on va voir après.
- Toujours vérifier si un fichier PDF dans `src/assets` est lisible avant de traiter l'extraction.