from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import Flight,Passenger
# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        #return all the flights in the flights table by the keyword flights
        "flights":Flight.objects.all()
    })
def flight(request,flight_id):
    #pk =primary key
    flight = Flight.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        #because manytomany filed connected passengers and flights 
        #we can use the related name to find all the passengers in the flight
        #and in the flight.html we can use the passengers to find all the passengers in the flight
        "passengers": flight.passengers.all(),
        #exclude 如果flights = flight 也就是有flight就不显示。
        "un_passengers":Passenger.objects.exclude(flights=flight).all()
    })
def book(request,flight_id):
    #get = get message from the page post = send message to the page
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)   
        passenger = Passenger.objects.get(pk =int(request.POST["passenger"]))
        passenger.flights.add(flight)
        #repsonse direct 用户完成操作去哪个页面用的。
        #reverse flight 逆向到flight页面然后args = flight_id就是哪个flight。
        return HttpResponseRedirect(reverse("flight-detail",args=(flight_id,)))