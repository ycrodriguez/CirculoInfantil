#INSTALLATION
#Inside the root directory run

#CMD
python -m venv venv
cd venv
cd Scripts
activate

pip install -r requirements.txt

python manage.py migrate
