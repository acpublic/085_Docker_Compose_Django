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
$ python manage.py startapp diary
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

## テンプレート
- templates/index.htmlを作成
```python
TEMPLATES = [
    {
    'DIRS': [BASE_DIR / "templates"],
    }
]
```
```python
INSTALLED_APPS = [
    'diary.apps.DiaryConfig',
}
```
- model.py
```python
class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    page_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- マイグレーション用ファイル作成
```
python manage.py makemigrations
```
## DBテーブル作成
```
python manage.py migrate
```


## 管理サイト
http://127.0.0.1:8000/admin/ 

## 管理ユーザーを作成
```
python manage.py createsuperuser
```
## admin 上で編集できるようにする
- polls/admin.py
```python
from django.contrib import admin
from .models import Question
admin.site.register(Question)
```

## CSSとjavascriptを使えるようにする
- static/css,static/cssを作成
- settings.pyに追加
```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
- htmlでロードする場合
```html
<head>
    {% load static %}
</head>
```


