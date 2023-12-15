
from django.urls import path
from . import views


app_name = 'notesync'
urlpatterns = [
    path('', views.band_list, name='band_list'),
    path('tour_dates/', views.tour_dates, name='tour_dates'),
    path('contact/', views.contact, name='contact'),
]
