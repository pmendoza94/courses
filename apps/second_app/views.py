from django.shortcuts import render, redirect
from ..first_app.models import User
from .models import Friend
from django.contrib import messages


# Create your views here.
def home(request):
    print '*** home ***'
    if not request.session['user_id']:
        return redirect('/')
    context = {
        'friends' : Friend.objects.all().order_by('-created_at')[3:],
        'users' : User.objects.all()
    }
    return render(request, 'second_app/home.html', context)

def addpage(request):
    if not request.session['user_id']:
        return redirect('/')
    return render(request, 'second_app/add.html')

def add(request):
    print '*** add ***'
    if not request.session['user_id']:
        return redirect('/')
    friend = Friend.objects.create(first_name = request.POST['first_name'])
    return render(request, 'second_app/add.html')

def show(request):
    print '*** show ***'
    if not request.session['user_id']:
        return redirect('/')
    return render(request, 'second_app/friends.html')
