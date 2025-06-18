# DevOps
## Create projet
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows

pip install fastapi uvicorn pytest
pip install -r requirements.txt  # si tu as un fichier

## Set up fastAPI

mkdir -p fastapi-sonarqube-demo/app
mkdir -p fastapi-sonarqube-demo/tests
mkdir -p fastapi-sonarqube-demo/.github/workflows
cd fastapi-sonarqube-demo

touch app/__init__.py app/main.py app/my_class.py
touch tests/__init__.py tests/test_my_class.py
touch requirements.txt sonar-project.properties .gitignore README.md .github/workflows/sonar.yml

