from fastapi import FastAPI, Depends

app = FastAPI()

# Route /
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Service utilisateur
class UserService:
    def get_user(self, user_id: int) -> dict:
        # Simulation d'accès à une base de données
        return {"id": user_id, "name": "John Doe"}

# Fournisseur de dépendance
def get_user_service():
    return UserService()

# Route /users/{user_id}
@app.get("/users/{user_id}")
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)
