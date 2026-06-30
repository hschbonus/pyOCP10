# SoftDesk Support — API REST

API RESTful de suivi de problèmes techniques, développée avec Django REST Framework.

## Prérequis

- Python 3.14+
- [Poetry](https://python-poetry.org/)

## Installation

### 1. Cloner le repository

```bash
git clone https://github.com/hschbonus/pyOCP10.git
cd pyOCP10
```

### 2. Installer les dépendances

```bash
poetry install
```

### 3. Appliquer les migrations

```bash
poetry run python manage.py migrate
```

### 4. Créer un super utilisateur (optionnel)

```bash
poetry run python manage.py createsuperuser
```

### 5. Lancer le serveur

```bash
poetry run python manage.py runserver
```

L'API est accessible à l'adresse : `http://127.0.0.1:8000/`

## Authentification

L'API utilise JWT. Pour obtenir un token :

```
POST /api/token/
{
    "username": "votre_username",
    "password": "votre_password"
}
```

Inclure le token dans les requêtes suivantes :

```
Authorization: Bearer <access_token>
```

## Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/users/` | Inscription |
| GET | `/api/users/` | Lister les utilisateurs |
| GET/PUT/PATCH/DELETE | `/api/users/{id}/` | Détail d'un utilisateur |
| POST | `/api/token/` | Connexion (JWT) |
| POST | `/api/token/refresh/` | Rafraîchir le token |
| GET/POST | `/api/projects/` | Lister / créer des projets |
| GET/PUT/PATCH/DELETE | `/api/projects/{id}/` | Détail d'un projet |
| GET/POST | `/api/contributors/` | Lister / ajouter des contributeurs |
| DELETE | `/api/contributors/{id}/` | Supprimer un contributeur |
| GET/POST | `/api/issues/` | Lister / créer des issues |
| GET/PUT/PATCH/DELETE | `/api/issues/{id}/` | Détail d'une issue |
| GET/POST | `/api/comments/` | Lister / créer des commentaires |
| GET/PUT/PATCH/DELETE | `/api/comments/{id}/` | Détail d'un commentaire |

## Tester l'API

Les requêtes sont disponibles dans le dossier `bruno/` (compatible [Bruno](https://www.usebruno.com/)).
