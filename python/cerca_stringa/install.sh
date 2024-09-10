mkdir /home/user/cerca_stringa
copy ./cerca.py /home/user/cerca_stringa
copy ./requirements.txt /home/user/cerca_stringa
cd /home/user/cerca_stringa
pip install virtualenv
virtualenv cerca
source cerca/bin/activate
pip install -r requirements.txt