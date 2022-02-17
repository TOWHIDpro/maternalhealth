from django.shortcuts import render, redirect
from . import calculator_func
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .utils import lastusers_id
from . models import Healthdata

# Show tge index page
def index(request):
    if request.user.is_authenticated:
        logout(request)
    else:pass
    
    return render(request, 'index/index.html')

# Main calculator
def check_health(request):

    # Create and login user autoomatically
    if not request.user.is_authenticated:
        name = f"user{lastusers_id()+1}"
        usr = User.objects.create(username=name)
        login(request, usr)

    # after clicking submit button this run
    if request.method == 'POST':
        # Retriv data from html form
        age = request.POST.get('age')
        systolicbp = request.POST.get('systolicbp')
        diastolicbp = request.POST.get('diastolicbp')
        bs = request.POST.get('bs')
        heartRate = request.POST.get('heartRate')

        # Result
        all_data = [age, systolicbp, diastolicbp, bs, heartRate]
        k = calculator_func.Forest.predict([all_data])
        if(k==2):
            message = "You are in High Risk"
        elif(k==1):
            message = 'You are in Mid Risk'
        else:
            message = "You are in Low Risk"

        # Save to database
        Healthdata.objects.create(
            user=request.user,
            age=age,
            systolicbp=systolicbp,
            diastolicbp=diastolicbp,
            bs=bs,
            heartRate=heartRate,
            message=message
            )
        return redirect('result')

    if request.method == 'GET': 
        return render(request, 'index/health_chacker.html',)

# To log in with a user id
def user_login(request):
    if request.method == 'POST':
        userid = (request.POST.get('userid')).lower()
        try:
            usr = User.objects.get(username=userid)
            login(request, usr)
            return redirect('check_health')
        except:
            pass
        return render(request, 'index/user_login.html')

    if request.method == 'GET':
        return render(request, 'index/user_login.html')

# To show the submitied datas and result
def result(request):
    data = Healthdata.objects.filter(user=request.user).last()
    return render(request, 'index/result.html', {
        'data': data
    })

# retrive current user's all data and show them
def all_result(request):
    data = Healthdata.objects.filter(user=request.user).order_by("-date")
    return render(request, 'index/all_result.html', {
        'datas': data
    })

# just simplly show about page
def about(request):
    return render(request, 'index/about.html')

def chart(request):
    return render(request, 'index/result_chart.html')
