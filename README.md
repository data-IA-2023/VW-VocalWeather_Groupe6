# VW-VocalWeather_Groupe6
Sandy et Paolo

SCHEMA DU PROJET:
![alt text](https://github.com/data-IA-2023/VW-VocalWeather_Groupe6/blob/paolo/schemaprojet.png)

La miission est la suivante :
- Intégrer la connexion à l’API Azure Cognitives Services.
- Intégrer les appels aux fonctions de speech to text.
- Intégrer la connexion à l’API de prédiction météo.
- Paramétrer l’appel à l’API de prédiction météo en fonction de l’instruction vocale (lieu, horizon de prédiction…)
- Monitorer la qualité du résultat en tenant compte de l’incertitude liée à la prédiction météo et de celle liée au speech to text
- Définir la procédure en cas de résultat en deçà d’un seuil de qualité minimum
- Stocker les résultats en base de données sur Azure.
- Exposer et intégrer les résultats de prévision dans une interface web simple.
- Documenter, versionner, livrer.
​
Ce projet s'inscrit dans un cadre global consistant à exploiter des services d’IA externes dans le développement d’applications d’IA, avec pour missions de :
- préconiser un service d’IA en fonction du besoin et des paramètres du projet,
- intégrer dans une application existante l’API du modèle ou du service d’intelligence artificielle,
- appliquer les bonnes pratiques de sécurité et d’accessibilité dans le développement d’application web,
- développer des tests d’intégration sur le périmètre de l’API exploité,
- rédiger une documentation technique.

Application web fonctionnelle et conforme aux attentes (Streamlit, Flask, FastAPI, etc.)
Dépôt github avec les scripts 
Slides de présentation du projet avec au moins les éléments suivants :
- Schéma fonctionnel de l’application avec les services nécessaires les technologies utilisées
- Identification des services d'IA existants et utilisés. Savoir expliquer leur fonctionnement
- Liste des spécifications fonctionnelles de l’application

Critères de performance

L'application finale doit :
- Correspondre aux objectifs énoncés
- Intégrer tous les services nécessaires à son bon fonctionnement

Bonus :
- La procédure en cas de résultat en deçà d’un seuil de qualité minimum est appliquée
- L'application peut intégrer les modalités du "ML Feedback loop".
- L'application peut exposer des données sous forme analytiques et graphiques
- L'application peut intégrer un template "user friendly"
- L'application peut intégrer une carte géographique pour positionner la ville
- L'application est sécurisée selon le top 10 OWASP
- L'application est Dockerisée
