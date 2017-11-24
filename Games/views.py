from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request,"main.html")

def allgames(request):
	return render(request, "Games/games.html",{"title":"Games"})

def resume(request):
	return render(request, "Resume.html")

def registration(request):
	return render(request,"Main/registration.html",{"title":"Registration"})

@csrf_protect
def register_in_site_post(request):
	username = request.POST.get("user_name")
	email = request.POST.get("e-mail")
	password = request.POST.get("password")
	print(username, email, password)
	user = User.objects.create_user(username, email, password)
	print (user)
	return HttpResponseRedirect("/Games/")

@csrf_protect
def login_in_site(request):
	
	user_name = request.POST.get("user_name")
	password = request.POST.get("password")
	user = authenticate(request, username = user_name, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect("/Games/")
	else: 
		return HttpResponse("false")




@csrf_protect
def send_message(request):
	email = request.POST.get("email")
	message = request.POST.get("message")
	name = request.POST.get("name")
	theme = email + " " + name
	send_mail(theme, message, 'testcafee2017@gmail.com',['konoval.denis@gmail.com'])
	print(email)
	return HttpResponseRedirect("/Resume/")


def gomoku(request):
	return render(request,"Games/gomoku.html",{"title":"Gomoku"})

def bowling(request):
	return render(request,"Games/bowling.html",{"title":"Bowling"})

def lines(request):
	return render(request,"Games/lines.html",{"title":"Lines"})


def login_site(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/Games/')

	return render(request,"Main/login.html",{"title":"Login"})

def logout_in_site(request):
	logout(request)
	return HttpResponseRedirect("/Games/")

@csrf_protect
def plus_gomoku_game(request):
	if request.POST:
		user = request.user
		print (user)
		winner = request.POST['winner']
		user.profile.gomokuGamesPlayed +=1
		if winner == "player":
			user.profile.gomokuWin +=1
		elif winner == "ai":
			user.profile.gomokuLose +=1
		user.profile.save()
		print(user.profile.gomokuGamesPlayed)
		
		print(winner)
		return HttpResponse(user.profile.gomokuGamesPlayed)

def show_gomoku_game(request):
	if request.GET:
		user = request.user
		print(user)
		return HttpResponse(user.profile.gomokuGamesPlayed)
		

@csrf_protect
def processing_bowling_throw(request):
	if request.POST:
		player = request.POST["player"]
		playerCountJS = request.POST["playerCount"]
		playerCount = json.loads(playerCountJS)
		currentAttempt = request.POST["currentAttempt"]
		currentThrow = request.POST["currentThrow"]
		value = request.POST["value"]

		print(player)
		print(playerCount)
		print(currentAttempt)
		print(currentThrow)
		print(value)

		changedCount = json.dumps(playerCount, sort_keys=True)
		return HttpResponse(playerCount)
		# return render(request,"Games/gomoku.html",{"title":"Gomoku"})



