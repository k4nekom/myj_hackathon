# 環境構築手順

リポジトリをクローン
```
git clone git@github.com:masaki987654321/myj_hackathon.git
```
仮想マシンを起動  
```
vagrant up  
```

仮想マシンに入る  
```
vagrant ssh  
```

python環境の作成  
```
sudo apt update  
sudo apt install python3-venv  
cd /vagrant  
python3 -m venv my_venv  
. my_venv/bin/activate  
pip install --upgrade pip 
pip install -r requirements.txt  
```

djnago起動  
```
cd /vagrant/mysite/ 
python manage.py migrate
python manage.py runserver 0.0.0.0:8000  
```

[localhost:8000](localhost:8000)へアクセスできれば完了 
