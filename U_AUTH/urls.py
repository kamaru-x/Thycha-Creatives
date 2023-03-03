from django.urls import path
from U_AUTH import views

urlpatterns = [
    path('',views.sign_in,name='sign-in'),
]