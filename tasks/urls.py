
from django.urls import path
from . import views

app_name="tasks"

urlpatterns = [

    path('',views.taskview,name="taskview"),
    path('delete/<str:pk>/',views.delete,name="delete"),
    path('upgrade/<str:pk>/',views.upgrade,name="upgrade"),
]
