from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('', views.listar_pacientes, name='listar_pacientes'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),
    
    path('api/login/', views_api.LoginAPIView.as_view(), name='api_login'),
    path('api/pacientes/', views_api.PacienteListCreateAPIView.as_view(), name='api_pacientes_list_create'),
    path('api/pacientes/<int:pk>/', views_api.PacienteDetailAPIView.as_view(), name='api_pacientes_detail'),
]