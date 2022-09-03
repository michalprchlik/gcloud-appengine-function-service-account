from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required(login_url='user_login')
def index(request):

	return render(request, 'index.html', {})


def user_login(request):

	response = None

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		request.session['user_name'] = username

		if user:
			if user.is_active:
				login(request, user)
				response = redirect('/?message_ok=Welcome to the Shitcoin sniper tool')
			else:
				response = HttpResponse("Account not active")
		else:
			response = render(request, 'login.html', {})
	else:
		response = render(request, 'login.html', {})

	return response


@login_required(login_url='user_login')
def user_logout(request):

	logout(request)

	return HttpResponseRedirect(reverse('login'))
