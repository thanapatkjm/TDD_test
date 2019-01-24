from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Animal, Description

def test(request):
    return render(request, 'testInput.html')

def index(request):
    list_animal_name=Animal.objects.order_by("animal_name")
    return render(request, 'index.html', {'list_animal_name': list_animal_name})

def remov(request,page_number):
    Animal.objects.get(pk=page_number).delete()
    return HttpResponseRedirect(reverse('animal:index'))

def created(request):
    return render(request, 'create.html')

def creating(request):
    add = Animal(animal_name=request.POST['input_name'])
    add.save()
    add_des = Description(animal=add,food=request.POST['input_food'],habitat=request.POST['input_habitat'],legs=request.POST['input_legs'])
    add_des.save()
    return HttpResponseRedirect(reverse('animal:index'))

def page(request,page_number):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def edit_descript(request,page_number):
    animal_num = Animal.objects.get(pk=page_number)
    return render(request, 'edit_descript.html', {'animal_num': animal_num})

def editing(request,page_number):
    animal_edit = get_object_or_404(Animal, pk=page_number)
    # if(request.POST['check_food']=='on'):
    animal_edit.description.food=request.POST['input_food']
    # if(request.POST['check_habitat']=='on'):
    animal_edit.description.habitat = request.POST['input_habitat']
    # if(request.POST['check_legs']=='on'):
    animal_edit.description.legs = request.POST['input_legs']
    animal_edit.description.save()
    return HttpResponseRedirect(reverse('animal:detail', args=(page_number,)))

def detail(request,page_number):
    latest_animal_name = get_object_or_404(Animal, pk=page_number)
    # latest_animal_name=Animal.objects.order_by("animal_name")
    # output = ', '.join([q.animal_name for q in latest_detail])
    # template = loader.get_template('index.html')  # load template from app / template
    # context = {
    #     'latest_animal_name': latest_animal_name,
    # } # making a dictionary
    # return HttpResponse(template.render(context, request))
    return render(request, 'detail.html', {'latest_animal_name': latest_animal_name})
# Create your views here.