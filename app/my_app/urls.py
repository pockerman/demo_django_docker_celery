from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_result/', views.get_result_view, name='get_result_view'),
]