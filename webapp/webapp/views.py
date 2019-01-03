from django.http.response import HttpResponse


def HelloWorld(request):
    return HttpResponse("<h1>This is </h1>")

def Start(request):
    return HttpResponse("<h1>This is Start</h1>")
