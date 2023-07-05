
from django.urls import path

from . import views

urlpatterns = [
    path('',views.test_scripts,name='test_scripts')
]