from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('prompt/', views.prompt_endpoint, name='prompt_endpoint')
] 