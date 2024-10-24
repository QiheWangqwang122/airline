from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    #通过flight的id来找到flight的信息1 = flight id 1
    path("<int:flight_id>",views.flight,name="flight-detail"),
    path("<int:flight_id>/book",views.book,name="book")
    
    
]