from django.shortcuts import render, redirect
from lists.models import Item
#from django.http import HttpResponse

# Create your views here.
def home_page (request):
    # # return HttpResponse("<html><title>To-Do lists</title><h1>To-Do</h1></html>")
    # if request.method == "POST":
    # #     return HttpResponse("You submitted: " + request.POST["item_text"])
    #     # item = Item()
    #     # item.text = request.POST["item_text"]
    #     # item.save()

    #     Item.objects.create(text=request.POST["item_text"])
    #     return redirect("/lists/the-only-list-on-the-world/")

    # items = Item.objects.all()
    return render(request, "home.html")

def view_list (request):
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})

def new_list(request):
    Item.objects.create(text=request.POST["item_text"])
    return redirect("/lists/the-only-list-on-the-world/")