from django.urls import path
from .views import home

# urlpatterns = [
#     path('', home, name= 'home'),
#
# ]

app_name = 'Home'

urlpatterns = [
    path('', home, name = 'Home'),
]

