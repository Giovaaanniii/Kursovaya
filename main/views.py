
import statistics
from django.shortcuts import redirect, render, get_object_or_404

from .models import Task
from .models import Events
from .models import Excursions
from .models import Master
from .models import Contacts
from .models import Graduation
from .forms import YourForm
# from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer,ExcursionsSerializer
# from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

def home(request):
    tasks_home = Task.objects.all()
    paginator = Paginator(tasks_home,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return  render(request, 'main/home.html',{'page_obj': page_obj, 'title': 'Главная страница','tasks': tasks_home})


class ExcursionsFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Реализуйте здесь вашу логику фильтрации данных
        return queryset.filter(short_task='c автобусом')  # Пример фильтрации по полю 'short_task'


class ExcursionsViewSet(viewsets.ModelViewSet):
    queryset = Excursions.objects.all()
    serializer_class =ExcursionsSerializer
    filter_backends = [ExcursionsFilter]
    
#---------------------------------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['short_task']

    
    @action(methods=['GET'], detail=False)
    def custom_action(self, request):
        queryset = self.get_queryset()  # Получаем queryset объектов
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    @action(methods=['POST'], detail=True)
    def custom_action(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=statistics.HTTP_201_CREATED)
#---------------------------------------------


def events(request):
     # Получаем ключевое слово из запроса (например, из GET параметра)
    keyword = request.GET.get('keyword', 'Новогодняя программа')  # Предположим, что ключевое слово передается в GET параметре 'keyword'
    # Создаем Q-запрос для поиска записей по ключевому слову
    q_query = Q(task__icontains=keyword)  # Найти записи, у которых поле description содержит ключевое слово (без учета регистра)
    # Фильтруем события используя Q-запрос по ключевому слову
    tasks_events = Events.objects.filter(q_query)
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


def edit_form(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        # Обработка данных из формы
        form = YourForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление после успешного обновления
    else:
        # Отображение формы для редактирования
        form = YourForm(instance=task)
    
    return render(request, 'main/edit_form.html', {'task': task, 'form': form})









# class TaskAPIListPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100000


# class TaskAPIList(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     pagination_class = TaskAPIListPagination
