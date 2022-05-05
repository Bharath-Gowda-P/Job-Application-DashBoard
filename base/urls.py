from django.urls import path
from . import views

urlpatterns  = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('candidate/<int:id>', views.candidate, name="candidate"),
    path('download/<int:id>', views.download, name="download"),
    path('edit/<int:id>', views.edit, name="edit"),
]