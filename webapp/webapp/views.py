from django.http.response import HttpResponse


def HelloWorld(request):
    return HttpResponse("<h1>Helloworld  </h1> <h5>HelloWorld</h5>")

def Start(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/HelloWorld/'>HelloWorld</a>")
