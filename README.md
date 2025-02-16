## プロジェクト作成
```
sudo docker-compose run web django-admin startproject mysite .
```
## パーミッション変更
```
sudo chown -R $USER:$USER mysite manage.py
```
## Django起動
```
docker-compose up
```
