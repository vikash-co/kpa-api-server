from django.urls import path
from . import views

urlpatterns = [
    path('api/forms/bogie-checksheet', views.bogie_checksheet_create),
    path('api/forms/wheel-specifications', views.wheel_specifications),

]
