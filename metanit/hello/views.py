from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello BROOOO</h1>'
    '<a href="https://avatars.mds.yandex.net/i?id=9ab2cdd87104420b22825a657c5419509f0831fc-2392471-images-thumbs&n=13" target="_blank">То что тебе надо</a>'
    '<div><a href="http://localhost:8000/about">О нас</a></div>'
    '<div><a href="http://localhost:8000/contact">Контакт</a></div>')

def about(request):
    return HttpResponse("О сайте")

def contact(request):
    return HttpResponse("Контакты")