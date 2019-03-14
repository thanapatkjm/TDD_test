from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
def index(request, q_num):
    quest = Question.objects.get(id=q_num)
    ch = Choice.objects.filter(question = quest)
    return  render(request, 'blog/home.html',{'quest':quest,"ch":ch})

def home(request):

    return render(request, 'blog/home.html')
