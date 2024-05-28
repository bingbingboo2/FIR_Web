run 
sudo apt install pipx
pipx ensurepath
pipx install django


login user:
cd login_user
python manage.py runserver 8000



chatbot:
cd palm_chatbot
py otp.py runserver 8080


python chat.py runserver 8090

streamlit hi.py


police dashboard :
cd police_dashboard_project
python manage.py runserver 8880








AWS: 
sudo apt-get update

sudo apt install python3-pip -y

python3 -m venv myenv

source myenv/bin/activate

pip install django


git clone https://github.com/diyshaikh/FIR_Web.git

cd FIR_Web

cd 

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

git pull origin main

Console 1:
sudo apt install pipx
pipx ensurepath
pipx install django
sudo apt-get update
sudo apt install python3-pip -y
python3 -m venv myenv
source myenv/bin/activate
pip install django
git clone https://github.com/diyshaikh/FIR_Web.git
cd FIR_Web
cd login_user
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000


console 2:
python3 -m venv myenv
source myenv/bin/activate
pip install flask
pip install google.generativeai
pip install xhtml2pdf
pip install boto3
cd FIR_Web
cd palm_chatbot
python chat.py runserver 0.0.0.0:5000


console 3:
python3 -m venv myenv
source myenv/bin/activate

cd FIR_Web
cd police_dashboard_project
python manage.py runserver 0.0.0.0:8090

console 4
python3 -m venv myenv
source myenv/bin/activate

cd FIR_Web
cd palm_chatbot
python otp.py 0.0.0.0:5600

