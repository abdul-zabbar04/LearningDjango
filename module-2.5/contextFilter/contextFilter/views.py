from django.shortcuts import HttpResponse

def default(request):
    return HttpResponse("Go to http://127.0.0.1:8000/firstapp/")