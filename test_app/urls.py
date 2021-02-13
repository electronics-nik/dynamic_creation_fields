from django.urls import path
from .views import index
from .views import my_view1
from .views import temp_page

urlpatterns = [
    path('', temp_page),
    path('add/', my_view1, name='my_view'),
]
