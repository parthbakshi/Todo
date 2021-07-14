from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "registration/dashboard.html")

def register(request):
    if request.method == 'GET':
        return render()
    elif request.method == 'POST':