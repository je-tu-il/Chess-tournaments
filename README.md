# 🏆 Chess-tournaments — Gestionnaire de Tournois en Temps Réel

[![Live Demo](https://img.shields.io/badge/Demo%20en%20Ligne-Organiser%20sur%20GitHub%20Pages-success?style=for-the-badge&logo=github)](https://je-tu-il.github.io/Chess-tournaments/)
[![Firebase](https://img.shields.io/badge/Backend-Firebase%20Realtime-FFCA28.svg?logo=firebase)](https://firebase.google.com/)
[![Zero Node.js](https://img.shields.io/badge/Dependencies-0%20(Pure%20HTML%2FJS)-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Une application web complète, sans aucun serveur à installer (100% serverless), pour organiser des compétitions d'échecs, tournois de jeux de société, LAN parties ou événements e-sport en temps réel.  
> Gère l'inscription des joueurs, les rondes du système Suisse (avec départage Buchholz), les tableaux à élimination directe, le chat en direct et un mode projection TV.

---

## ⚡ Utilisation Immédiate (Sans Installation)

👉 **[Accéder directement à l'application : https://je-tu-il.github.io/Chess-tournaments/](https://je-tu-il.github.io/Chess-tournaments/)**

1. Ouvrez l'application dans votre navigateur.
2. Cliquez sur l'icône **⚙️ (Configuration)** en haut à droite pour connecter votre base de données Firebase gratuite (Realtime Database).
3. Vos clés sont sauvegardées localement dans votre navigateur (`localStorage`) : **aucun besoin de modifier le code source**.

---

## ✨ Fonctionnalités Majeures

- ♟️ **Deux Modes de Tournoi au Choix** :
  - **Système Suisse** : Appariement dynamique, classement par points et calcul automatique du départage de **Buchholz**.
  - **Tableau à Élimination Directe (Bracket)** : Arbre de tournoi automatique (puissances de 2) avec gestion intelligente des exemptions (BYE).
- ⚙️ **Panneau Administrateur Sécurisé** :
  - Accès protégé par mot de passe (hachage SHA-256).
  - Ajout manuel, exclusion de joueur, validation des résultats, réinitialisation de tournoi.
- 💬 **Chat Intégré en Temps Réel** : Messagerie instantanée pour les participants (barre latérale sur bureau, tiroir sur mobile).
- 📺 **Mode TV & Projecteur** : Masque les menus d'administration pour afficher les rondes et classements en plein écran sur vidéo-projecteur.
- 🌓 **Thèmes Sombre & Clair** : Basculable d'un clic avec le bouton 🌗.

---

## 🛠️ Lancement Local

Aucun runtime Node.js n'est nécessaire. Clonez et ouvrez simplement `index.html` :

```bash
git clone https://github.com/je-tu-il/Chess-tournaments.git
cd Chess-tournaments
```
Ouvrez directement `index.html` dans votre navigateur préféré.

---

## 📄 Licence

Ce projet est sous licence MIT. Libre d'utilisation pour vos événements et clubs.
