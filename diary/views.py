from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo
from django.utils import timezone
from django.http import JsonResponse
from .models import Page

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "diary/index.html")
    
    def post(self, request):
        return render(request, "diary/index.html")

class SendView(View):
    def get(self, request):
        return HttpResponse("GETリクエストが送信されました！")

    def post(self, request):
        # 新しいレコードを作成
        obj = Page.objects.create()
        print(obj.created_at)
        # 成功メッセージとともにビューを返す
        return render(request, "diary/success.html", {'datetime': obj.created_at})      
        
index = IndexView.as_view()
send = SendView.as_view()