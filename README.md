# ONOS Application Activation Script

Ce script Python permet d'activer des applications ONOS en utilisant l'API REST northbound. Il lit les informations des applications à partir d'un fichier JSON et active celles dont l'état est "ACTIVE". La configuration (adresse IP, port, etc.) est chargée depuis un fichier `.env` pour une meilleure gestion et sécurité.

## Prérequis

* Python 3.6 ou supérieur
* Les bibliothèques Python : `requests`, `python-dotenv`
* Un fichier JSON contenant les informations des applications ONOS (par exemple, `applications.json`)
* Une instance ONOS en cours d'exécution

## Installation

1.  **Cloner le dépôt (ou télécharger le code)**

    Si vous avez cloné ce dépôt, passez à l'étape suivante. Si vous avez téléchargé le code, assurez-vous d'avoir tous les fichiers nécessaires ( `app_activation.py`, `applications.json` ).

2.  **Créer un environnement virtuel (recommandé)**

    Il est fortement recommandé de travailler dans un environnement virtuel pour isoler les dépendances de ce projet.

    ```bash
    python3 -m venv venv  # Créer un environnement virtuel nommé "venv"
    source venv/bin/activate  # Activer l'environnement (Linux/macOS)
    venv\Scripts\activate  # Activer l'environnement (Windows)
    ```

3.  **Installer les dépendances**

    Installez les bibliothèques Python nécessaires à l'aide de `pip` :

    ```bash
    pip install requests python-dotenv
    ```

## Configuration

1.  **Créer un fichier `.env`**

    Créez un fichier nommé `.env` dans le même répertoire que votre script Python (`app_activation.py`). Ce fichier contiendra les paramètres de configuration de votre instance ONOS.

2.  **Définir les variables d'environnement**

    Ajoutez les variables suivantes à votre fichier `.env`, en remplaçant les valeurs d'espace réservé par les informations réelles de votre installation ONOS :

    ```
    ONOS_IP=your_onos_ip        # Adresse IP de votre instance ONOS (par exemple, 192.168.1.10)
    ONOS_PORT=8181               # Port de l'API REST ONOS (la valeur par défaut est 8181)
    ONOS_USER=your_onos_user     # Nom d'utilisateur pour l'authentification ONOS (par exemple, onos)
    ONOS_PASSWORD=your_onos_password   # Mot de passe pour l'authentification ONOS (par exemple, rocks)
    JSON_FILE_PATH=applications.json  # Chemin vers votre fichier JSON (laissez "applications.json" si c'est dans le même répertoire)
    ```

    **⚠️  Important (Sécurité) :**

    * Ne committez jamais votre fichier `.env` contenant des informations sensibles (comme les mots de passe) dans un dépôt public. Si vous utilisez un dépôt public, envisagez d'autres méthodes de gestion des secrets (variables d'environnement du système, coffres-forts, etc.).

## Utilisation

1.  **Exécuter le script**

    Une fois que vous avez configuré le fichier `.env` et que vous êtes dans l'environnement virtuel (si vous en utilisez un), exécutez le script Python :

    ```bash
    python3 app_activation.py
    ```

    Le script va :

    * Charger les variables de configuration depuis le fichier `.env`.
    * Lire les informations des applications depuis le fichier JSON (`applications.json`).
    * Parcourir la liste des applications.
    * Activer les applications dont l'état est "ACTIVE" en utilisant l'API REST ONOS.
    * Afficher des messages de succès ou d'erreur pour chaque tentative d'activation.

## Gestion des Erreurs

Le script inclut une gestion des erreurs pour :

* Les fichiers manquants (`applications.json` ou `.env`).
* Les erreurs de format JSON dans `applications.json`.
* Les erreurs de connexion à l'API ONOS.
* Les valeurs manquantes ou incorrectes dans le fichier `.env`.

## Exemple de Fichier `applications.json`

```json
{
  "applications": [
    {
      "name": "org.onosproject.lldp",
      "state": "ACTIVE"
    },
    {
      "name": "org.onosproject.openflow",
      "state": "INSTALLED"
    },
    {
      "name": "org.onosproject.drivers.bmv2",
      "state": "ACTIVE"
    }
  ]
}