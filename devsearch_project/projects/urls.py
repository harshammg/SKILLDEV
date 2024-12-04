from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns=[
    path('', views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project'),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>/',views.updateProject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project")
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)