from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dests = Destination.objects.all()
    return render(request,"index.html",{"dests":dests})


# dest1 = Destination()
#     dest1.name = "Dhaka"
#     dest1.desc = "The city that never gets old"
#     dest1.img = "destination_1.jpg"
#     dest1.price = 700
#     dest1.offer = False
#
#     dest2 = Destination()
#     dest2.name = "Indonesia"
#     dest2.desc = "The city that never gets faded"
#     dest2.img = "destination_2.jpg"
#     dest2.price = 200
#     dest2.offer = True
#
#     dest3 = Destination()
#     dest3.name = "San Francisco"
#     dest3.desc = "The city that never gets bored"
#     dest3.img = "destination_3.jpg"
#     dest3.price = 800
#     dests = [dest1,dest2,dest3]
#     dest3.offer = False .