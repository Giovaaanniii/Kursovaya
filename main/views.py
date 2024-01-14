from django.shortcuts import render
from .models import Task
from .models import Events
from .models import Excursions
from .models import Master
from .models import Contacts
from .models import Graduation


def home(request):
    tasks_home = Task.objects.all()
    return  render(request, 'main/home.html',{'title': 'Главная страница','tasks': tasks_home})

def events(request):
    tasks_events = Events.objects.all()
    return render(request, 'main/events.html',{'title': 'Мероприятия','tasks': tasks_events})

def contacts(request):
    tasks_contacts = Contacts.objects.all()
    return render(request, 'main/contacts.html',{'title': 'Контакты','tasks': tasks_contacts})

def excursions(request):
    tasks_excursions = Excursions.objects.all()
    return render(request, 'main/excursions.html',{'title': 'Экскурсии','tasks': tasks_excursions})

def master(request):
    tasks_master = Master.objects.all()
    return render(request, 'main/master-classes.html',{'title': 'Мастер-классы','tasks': tasks_master})

def graduation(request):
    tasks_graduation = Graduation.objects.all()
    return render(request, 'main/graduation.html',{'title': 'Выпускные','tasks': tasks_graduation})
