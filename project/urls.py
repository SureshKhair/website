from django.urls import path
from . import views

urlpatterns = [
    path('',views.project,name='project'),
    path('projects/<str:pk>/',views.projects,name='projects'),
    path('create-projects/',views.createproject,name='create-project'),
    path('update-projects/<str:pk>',views.updateproject,name='update-project'),
    path('delete-projects/<str:pk>',views.deleteproject,name='delete-project'),
   ]
