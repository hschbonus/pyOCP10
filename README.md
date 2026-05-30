# SoftDesk Support — API REST

API RESTful de suivi de problèmes techniques, développée avec Django REST Framework.

## Prérequis

- Python 3.12+
- [Poetry](https://python-poetry.org/) *(ou Pipenv — à compléter)*

## Installation

### 1. Cloner le repository

```bash
git clone https://github.com/HerveSchmidt/pyOCP10.git
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

## Endpoints principaux

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/users/` | Inscription |
| POST | `/api/token/` | Connexion (JWT) |
| POST | `/api/token/refresh/` | Rafraîchir le token |
| GET/POST | `/api/projects/` | Lister / créer des projets |
| GET/PUT/DELETE | `/api/projects/{id}/` | Détail d'un projet |
| GET/POST | `/api/projects/{id}/contributors/` | Contributeurs d'un projet |
| GET/POST | `/api/projects/{id}/issues/` | Issues d'un projet |
| GET/POST | `/api/projects/{id}/issues/{id}/comments/` | Commentaires d'une issue |

## Tester l'API

Les requêtes peuvent être testées avec [Bruno](https://www.usebruno.com/) ou Postman.
