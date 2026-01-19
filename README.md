# Chess-tournaments
A fully serverless web application (HTML/JS/Firebase) designed to organize competitions in real-time. It handles player registration, live chat, and two major game modes: the Swiss System (with Buchholz tie-breaks) and Single Elimination Brackets. Perfect for LAN parties, board game tournaments, or casual e-sports events.

# 🏆 Tournament Manager (V35 Ultimate)

A complete, responsive, and real-time web application to manage tournaments easily. No server installation required (Node/PHP); it runs entirely in the browser using Firebase as the backend.

## ⚠️ Known Issue

> **The score display in the Bracket (Tree) view is currently broken.**
> While the logic works perfectly (clicking a player advances them as the winner and updates the database), the visual interface (powered by the `jquery-bracket` library) struggles to display specific score numbers (e.g., "2-1") or align connectors perfectly in complex setups.
> *Note: The "Swiss Rounds" mode works perfectly.*

## ✨ Key Features

### 🎮 Game Modes
* **Swiss System:** Dynamic pairing, point-based ranking, **Buchholz** tie-break system.
* **Bracket (Tree):** Automatic generation (powers of 2), smart **BYE** handling for odd numbers of players.
* **Final Phases:** Option to trigger Semi-Finals and a Grand Final after the Swiss rounds.

### 🛠️ Administration
* **Secure Panel:** Protected by a password (hashed with SHA-256).
* **Total Control:** Manually add players, kick players, manage scores, full tournament reset.
* **Drop/Leave Management:** Players can request to leave the tournament; the admin must approve the request.

### 💬 Social & UX
* **Global Chat:** Real-time messaging (Sidebar on Desktop, Overlay on Mobile).
* **Fair-Play:** 5-star rating system popup after every match.
* **Interface:** Dark/Light Mode, Fully Responsive (Mobile/Tablet/PC), TV Mode (Projector view).
* **Feedback:** Sound effects (toggleable), Confetti on victory.

## 🚀 Installation & Configuration

This project does not require Node.js or a local server.

1.  **Clone or Download** the repository files.
2.  **Create a Firebase Project:**
    * Go to the [Firebase Console](https://console.firebase.google.com/).
    * Create a new project and add a "Web App".
    * Enable the **Realtime Database** (start in Test Mode for development).
3.  **Configure API Keys:**
    * Open the `index.html` file in a code editor.
    * Scroll down to the bottom script section to find `const firebaseConfig = { ... }`.
    * Replace the values `"REMPLACE_MOI"` (or placeholders) with your actual keys provided by Firebase.
4.  **Run:** Simply open `index.html` in your web browser.

### Configuration Example:
```javascript
const firebaseConfig = {
    apiKey: "AIzaSyD...",
    authDomain: "your-project.firebaseapp.com",
    databaseURL: "[https://your-project-default-rtdb.firebaseio.com](https://your-project-default-rtdb.firebaseio.com)",
    projectId: "your-project",
    storageBucket: "your-project.appspot.com",
    messagingSenderId: "123456...",
    appId: "1:123456..."
};
