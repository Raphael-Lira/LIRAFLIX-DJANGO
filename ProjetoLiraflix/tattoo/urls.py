from django.urls import path
from .views import Homepage, home_tattoo, Detalheview
app_name = 'tattoo'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('tattoo/', home_tattoo, name= 'hometattoo'),
    path('tattoo/<int:pk>', Detalheview.as_view(), name='detalheview')
]