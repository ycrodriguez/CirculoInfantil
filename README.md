#INSTALLATION

#Inside the root directory run

#CMD

python -m venv venv

cd venv

cd Scripts

source activate

cd ../../

pip install -r requirements.txt

python manage.py migrate
