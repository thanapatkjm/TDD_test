from django.urls import path
from . import views

urlpatterns = [path('<int:q_num>/', views.index, name='index'),
               path('home/', views.home, name='home'),]
