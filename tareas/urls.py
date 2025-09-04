from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout_view, name='signout'),

    path('tareas/', views.lista_tareas, name='tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:pk>/', views.detalles_tarea, name='detalles_tarea'),
    path('tareas/<int:pk>/editar/', views.actualizar_tarea, name='actualizar_tarea'),
    path('tareas/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tareas/<int:pk>/toggle/', views.toggle_completada, name='toggle_completada'),
    path('tareas/completadas/', views.tareas_completadas, name='tareas_completadas'),

]
