# 🚀 Projet FastAPI + Tests + SonarCloud

Ce dépôt contient un projet Python basé sur **FastAPI**, avec :
- une architecture simple (`app/`, `tests/`)
- des tests unitaires avec `pytest`
- une couverture de code analysée par **SonarCloud**
- une CI automatisée via **GitHub Actions**

---

## 📦 Installation du projet

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-utilisateur/fastapi-sonarqube-demo.git
cd fastapi-sonarqube-demo
````

2. Créez un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
```

3. Installez les dépendances :

```bash
pip install -r requirements.txt
```

---

## 🚀 Lancer l'application FastAPI

```bash
uvicorn app.main:app --reload
```

Puis ouvrez [http://localhost:8000](http://localhost:8000) dans votre navigateur.

---

## 🧪 Exécuter les tests unitaires

```bash
pytest
```

Avec génération de la couverture :

```bash
pytest --cov=app --cov-report=xml
```

Un fichier `coverage.xml` est généré à la racine.

---

## ☁️ Intégration SonarCloud (CI)

Ce projet est intégré avec **SonarCloud** via GitHub Actions. À chaque `push` ou `pull request`, le code est analysé automatiquement.

Les métriques incluent :

* taux de couverture de tests
* duplication
* complexité
* problèmes de sécurité et de style

### 🔐 Secrets nécessaires

Ajoutez ce secret dans votre dépôt GitHub :

* `SONAR_TOKEN` : token généré depuis votre compte SonarCloud ([lien direct](https://sonarcloud.io/account/security))

---

## 🧠 Erreurs connues et solutions

| Erreur                                                            | Solution                                                                                                     |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `Could not open requirements.txt`                                 | Vérifiez que le fichier est bien **commité** dans le repo                                                    |
| `You must define sonar.projectKey`                                | Ajoutez un fichier `sonar-project.properties` à la racine                                                    |
| `You are running CI analysis while Automatic Analysis is enabled` | Désactivez **Automatic Analysis** dans SonarCloud (Project Settings > Analysis Method)                       |
| `0.0% Coverage` dans SonarCloud                                   | Vérifiez que `coverage.xml` est bien généré et déclaré avec `sonar.python.coverage.reportPaths=coverage.xml` |

---

## 📁 Structure du projet

```
fastapi-sonarqube-demo/
├── app/
│   └── main.py, my_class.py
├── tests/
│   └── test_my_class.py
├── .github/workflows/sonar.yml
├── sonar-project.properties
├── requirements.txt
├── README.md
```

---

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l’utiliser et de le modifier.
