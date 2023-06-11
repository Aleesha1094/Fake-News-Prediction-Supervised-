This is a prediction model in Django Using AI algorithm (Naive Bayes Algorithm). It was useful to handle Dataset of 57k+ rows. We have one Class Attribute and 1 Class label having Fake or Real instances. Can predict most of the results truly.

#########   for running the application please perform below steps before #########

create a directory with any name like FakeNewsPredictor

open folder in VS code and then open terminal for the directory or simply open Command prompt in the folder

create a virtual Enviroment using following command:
  
  python.exe -m pip install --upgrade pip       #Upgrade your pip  
 

python -m venv myenv                      #create a virtual enviroment

myenv/scripts/activate                    # to activate venv in cmd or terminal

source myenv/scripts/activate             # to avtivate myenv in gitbash

then install DJANGO and below libraries:

pip install Django
pip install Pandas
pip install scikit-learn

after that change the directry using command 

cd fake_news_detector

run the project now 

python manage.py runserver





