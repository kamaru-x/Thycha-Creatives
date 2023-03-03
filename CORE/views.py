from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def leads_list(request):
    return render(request,'leads-list.html')

def leads_add(request):
    return render(request,'leads-add.html')

def leads_view(request):
    return render(request,'leads-view.html')