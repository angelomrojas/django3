from django.urls import path
from .views import IndexView #, TestView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('produto/<int:pk>', TestView.as_view(), name='produto')
]