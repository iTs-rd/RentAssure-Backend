echo " BUILD START"
sudo python3.9 -m pip install -r requirements.txt
sudo python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END" 
