from django.urls import path
from CORE import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('leads-list/',views.leads_list,name='leads-list'),
    path('leads-add/',views.leads_add,name='leads-add'),
    path('leads-view/',views.leads_view,name='leads-view')
]