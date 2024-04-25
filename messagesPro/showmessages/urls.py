from django.urls import path
from showmessages.views import user
urlpatterns = [
    path("",user,name="userform")
]