from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.events, name='events'),
    path('excursions', views.excursions, name='excursions'),
    path('master-classes', views.master, name='master-classes'),
    path('contacts', views.contacts, name='contacts'),
    path('graduation', views.graduation, name='graduation'),
    path('edit_form/<int:task_id>/', views.edit_form, name='edit_form'),
]
