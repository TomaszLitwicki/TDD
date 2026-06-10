from django.shortcuts import render
from lists.models import Item
#from django.http import HttpResponse

# Create your views here.
def home_page (request):
    # return HttpResponse("<html><title>To-Do lists</title><h1>To-Do</h1></html>")
    # if request.method == "POST":
    #     return HttpResponse("You submitted: " + request.POST["item_text"])
    item = Item()
    item.text = request.POST.get("item_text", "")
    item.save()

    return render(request,
                  "home.html",
                  {"new_item_text": request.POST.get("item_text","")})