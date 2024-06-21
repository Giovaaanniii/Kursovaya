from django.urls import include, path
from .views import ExcursionsViewSet,TaskViewSet
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register(r'excursions',ExcursionsViewSet)
router.register(r'task',TaskViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.events, name='events'),
    path('excursions', views.excursions, name='excursions'),
    path('master-classes', views.master, name='master-classes'),
    path('contacts', views.contacts, name='contacts'),
    path('graduation', views.graduation, name='graduation'),
    path('edit_form/<int:task_id>/', views.edit_form, name='edit_form'),
    path('api/', include(router.urls)),
]
