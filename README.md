# Cinéma

## Description

Ce service Flask gère les utilisateurs et les réservations dans notre application de réservation de films. Il offre une interface pour ajouter, récupérer, mettre à jour et supprimer des informations d'utilisateur, ainsi que pour gérer les réservations via des appels gRPC.

## Fonctionnalités Principales

+ Gestion des utilisateurs (ajout, récupération, mise à jour, suppression).
+ Récupération des réservations utilisateur via gRPC.
+ Interaction avec un service GraphQL pour obtenir des détails sur les films.

### Routes API

- **GET /user/**: Retourne tous les utilisateurs.
- **GET /user/<id>**: Retourne un utilisateur spécifique par son ID.
- **POST /user/**: Ajoute un nouvel utilisateur.
- **DELETE /user/<id>**: Supprime un utilisateur.
- **GET /reservations/<userid>**: Retourne les réservations d'un utilisateur.
- **POST /user/<userid>/reservation**: Ajoute une réservation pour un utilisateur.
- **DELETE /user/<userid>/reservation**: Supprime une réservation d'un utilisateur.
- **GET /movies**: Retourne tous les films disponibles.
- **GET /movies/<date>**: Retourne les films disponibles à une date spécifique.

#### Ce qui reste à faire

- **PUT /user/<id>**: Met à jour un utilisateur existant.
- **PUT /user/<userid>/reservation**: Met à jour une réservation d'un utilisateur.
- Faire un nombre maximal possible de place disponibles pour un film et une date précise (ex: max 200 réservations peut importe qui réserve)

### Pour démarrer le service :

Pour démarrer les différents services de l'application, notamment le service utilisateur décrit dans le fichier `user.py`, vous devez les exécuter un par un depuis PyCharm. Voici les étapes à suivre :

1. **Ouvrez PyCharm :** Lancez PyCharm et ouvrez le projet contenant vos services Flask.
2. **Démarrage des services :**
   - Cliquez sur le bouton `Run` (ou utilisez le raccourci `Shift + F10` sous Windows/Linux, `Ctrl + R` sous macOS) pour démarrer le service.
3. **Vérification :**
   - Après le démarrage de chaque service, vérifiez que le service fonctionne correctement en ouvrant un navigateur et en accédant aux routes API correspondantes (par exemple, `http://127.0.0.1:3203/user/` pour le service utilisateur).
4. **Arrêt des services :**
   - Pour arrêter un service, cliquez sur le bouton rouge `Stop` dans la barre d'outils de PyCharm.
