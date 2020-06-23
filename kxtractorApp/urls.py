from django.urls import path
from . import views

urlpatterns = [
    # path('', views.func1, name='home-page'),
    # path('process', views.func2, name='process-page'),
    path('', views.home, name='home-page'),
    path('process', views.process, name='process-page')
]