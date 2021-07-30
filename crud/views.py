from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import *
from .forms import ProductForm,CreateUserForm

def registerpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account created for ' + user)

				return redirect('login')

	context = {'form':form}
	return render(request, 'crud/register.html', context)


def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'crud/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def homepage(request):
	products =  Product.objects.all()
	return render(request, 'crud/index.html',{'products':products})

@login_required(login_url='login')
def detail(request,product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'crud/product_detail.html', {'product':product})


@login_required(login_url='login')
def add(request):
	
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, 'crud/add.html',{'form':form})


@login_required(login_url='login')
def update(request, product_id):
	products =  Product.objects.get(pk=product_id)
	form = ProductForm(instance=products)

	if request.method == 'POST':
		form = ProductForm(request.POST,instance=products)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, 'crud/update.html',{'form':form})

@login_required(login_url='login')
def delete(request,product_id):

    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context = {'item':product}
    return render(request, 'crud/delete.html', context)

