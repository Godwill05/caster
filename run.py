# run.py
#fonction mere de l'applicattion qui permet de lancer le serveur 
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=7000 ,debug=True)
