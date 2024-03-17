from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageBasedView.as_view(), name='home_page'),
]
