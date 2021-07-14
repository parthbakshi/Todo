from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Todolist, items
from .forms import TodoListItemForm

def index(response):
    return render(response, "tutorial/base.html", {})

def v1(response, id):
    ls = Todolist.objects.get(id=id)
    return HttpResponse(f"<h1>{ls}</h1>")

def get_all_todo_list(request):
    """
    This gets all the todolist associated with the user
    :param request:
    :return:
    """
    pass


def get_list(request, id):
    if request.method == "POST":
        t = Todolist.objects.get(id=id)
        if t:
            if request.POST.get("save"):
                for item in t.items_set.all():
                    if request.POST.get(f"c{item.id}") == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            return render(request, "tutorial/index.html", {"items": t.items_set.all(), "name": t.name, "id": t.id})
        else:
            return render(request, "tutorial/404Notfound.html")

    else:
        try:
            t = Todolist.objects.get(id=id)
        except Exception as err:
            return render(request, "tutorial/404Notfound.html")
        if t:
             items = t.items_set.all()
             if items:
                return render(request, "tutorial/index.html", {"items":items, "name":t.name, "id":t.id})
        else:
            template = render(request, "tutorial/404Notfound.html")


def create_list(request, id):
    """
    Create todolist for the user
    :param response:
    :return:
    """
    if request.method == 'POST':
        t = Todolist.objects.get(id=id)

        if t:
            form = TodoListItemForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data["text"]
                complete = form.cleaned_data["complete"]
                due_date = form.cleaned_data["due_date"]
                status = t.items_set.create(text=text, complete=complete, due_date=due_date)
            return redirect('get_list', id=t.id)

        else:
            return render(request,"tutorial/404Notfound.html")
    else:
        form = TodoListItemForm()
        return render(request, 'tutorial/create.html', {"form":form})