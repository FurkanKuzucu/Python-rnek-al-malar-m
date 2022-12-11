from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('search',views.search, name='search'),
    path('addbook',views.addbook),
    path('save',views.save,name='save'),
    path('find',views.findbook),
    path('update/<int:id>',views.delt),
    path('datetime',views.datetime),
]