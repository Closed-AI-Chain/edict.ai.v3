
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# from .app import scraper ,coindeskVideo
# from .app import image_search
from .app import new_final
import json
from .models import VideoLinks
from .app import run_upload_video

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect('')
            else:
                return redirect('')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('/')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not same')
            return redirect('register')
    else:
        return render(request,"nikka/www.nikka.me/project/castofly-2/form.html")

def generateVideo(request):
    
    if request.method=="POST":
        url=request.POST['url']
        if url.find("www.hindustantimes.com") != -1:
            data=scraper.hindustanTimes(url)
            image_search.merged(data)
            return redirect('/video/')
        elif url=="https://www.coindesk.com/tag/news/" or "https://www.coindesk.com/":
            data=scraper.coinDesk()
            coindeskVideo.coindesk_merged(data)
            return redirect('/video/')
    
    return render(request,"createVideo.html")

def showVideo(request):
    return render(request,"video.html")

def index(request):
    return render(request, "nikka/www.nikka.me/index.html")

# def test(request):
#     return render(request, "test.html")

def form(request):
    if request.method=="POST":
        url=request.POST['url']
        new_final.edict_video(url)
        with open("data.json", "r") as file:
            variable = json.load(file)
        data=VideoLinks(link=variable)
        data.save()
        return redirect("https://www.youtube.com/watch?v={}".format(variable))
    return render(request, "nikka/css-grid-style-guide-ii/dist/form-grid.html")

def test(request):
    run_upload_video.upload_video("news_edicted_7.mp4")
    with open("data.json", "r") as file:
        variable = json.load(file)
        data=VideoLinks(link=variable)
        data.save()
    
    return HttpResponse("Video uploaded")