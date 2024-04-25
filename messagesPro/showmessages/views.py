from django.shortcuts import render
from showmessages.forms import UserForm
from django.contrib import messages
#django messages framework


# Create your views here.
def user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Form is sucessfully submitted")
    form = UserForm()
    context = {"form":form}
    return render(request,"showmessages/index.html",context)