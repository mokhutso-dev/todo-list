from django.shortcuts import render
from django.http import HttpResponse, 	HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

# def index(request, id):
# 	ls = ToDoList.objects.get(id=id)
# 	return render(request, "list.html", {"ls":ls})

"""
    Add items
"""
def index(request, id):
    ls = ToDoList.objects.get(id=id)
    
    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                if "text" + str(item.id) in request.POST:
                    item.text = request.POST.get("text" + str(item.id))
                item.save()
                
        elif request.POST.get("add"):
            newItem = request.POST.get("new")
            if newItem != "":
                ls.item_set.create(text=newItem, complete=False)
            else:
                print("invalid")
                
        # elif request.POST.get("newItem"):
        #     txt = request.POST.get("new")
        #     if len(txt) > 2:
        #         ls.item_set.create(text=txt, complete=False)
        #     else:
        #         print("invalid")
    # return render(request, "list.html", {"ls":ls})
    return render(request, "index.html", {"ls": ls})


def create(request):
    """
    Create a new todo list
    """
    # request.user
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(request, "create.html", {"form":form})
    
def home(request):
    """            
        Welcome to the amazing list
    """
    return render(request, "home.html", {})

def viewId(request):
    """_summary_
        Get list by username or id
    """
    list = ToDoList.objects.all()
    return render(request, "viewId.html", {"lists":list})

def viewAll(request):
    """_summary_
        Get all the list
    """
    list = ToDoList.objects.all()
    return render(request, "viewAll.html", {"lists":list})
