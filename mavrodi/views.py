from .models import *
from django.http import HttpResponse
import json


def get_user_info(request):
    data = request.POST
    if data:
        try:
            client = Client.objects.get(chat_id=data['chat_id'])
            cleaned = {}
            try:
                cleaned['name'] = client.name
                cleaned['chat_id'] = client.chat_id
                cleaned['balance'] = client.balance
                cleaned['paid'] = client.paid
                cleaned['referer']
            finally:
                cleaned['correct'] = True
                return HttpResponse(json.dumps(cleaned, ensure_ascii=False), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"correct": False}, ensure_ascii=False), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"correct": False}, ensure_ascii=False), content_type="application/json")


def create_user(request):
    data = request.POST
    if data:
        Client.objects.create(chat_id=data['chat_id'], name=data['name'], referer=data['referer'])
        return HttpResponse(json.dumps({"correct": True}, ensure_ascii=False), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"correct": False}, ensure_ascii=False), content_type="application/json")
