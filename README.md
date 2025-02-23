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
## コンテナ内
```
docker container exec -it docker-web-1 /bin/bash
```

## アプリケーション作成
```
$ python manage.py startapp polls
```
- プロジェクト：アプリ本体
- アプリケーション：機能

## Database設定
https://docs.djangoproject.com/ja/5.0/ref/settings/#databases
### mysite/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
- django.db.backends.postgresql
- django.db.backends.mysql
- django.db.backends.sqlite3
- django.db.backends.oracle

```
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```
## DBファイル作成
```
python manage.py migrate
```
## マイグレーション用のファイルを作成
```
python manage.py makemigrations polls
```

## 管理サイト
http://127.0.0.1:8000/admin/ 

## 管理ユーザーを作成
```
python manage.py createsuperuser
```
