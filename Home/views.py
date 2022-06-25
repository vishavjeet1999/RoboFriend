from django.http import JsonResponse
from django.shortcuts import redirect, render

from Home.models import Robots

# Create your views here.
def index(request):
    return render(request,'index.html')

def robo_api(request):
    robots = Robots.objects.all()

    data = {
        'robots':[]
    }
    for robot in robots:
        data['robots'].append(
            {
                'id': robot.id,
                'name': robot.name,
                'username': robot.username,
                'email': robot.email
            }
        )
    return JsonResponse(data)

def new(request):
    name = request.POST['name'].title()
    username = request.POST['username']
    email = request.POST['email']

    obj = Robots()
    obj.name = name
    obj.username = username
    obj.email = email
    obj.save()
    return redirect(index)