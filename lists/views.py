from django.shortcuts import render, redirect
from lists.models import Item
#from django.http import HttpResponse

# Create your views here.
def home_page (request):
    # return HttpResponse("<html><title>To-Do lists</title><h1>To-Do</h1></html>")
    if request.method == "POST":
    #     return HttpResponse("You submitted: " + request.POST["item_text"])
        # item = Item()
        # item.text = request.POST["item_text"]
        # item.save()

        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")

    items = Item.objects.all()
    return render(request,
                  "home.html",
                  {"items": items})