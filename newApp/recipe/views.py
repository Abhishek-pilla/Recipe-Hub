from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# Create your views here.
@login_required(login_url='/login')
def recipe(request):
    data = request.GET
    if request.method == "POST":
         data = request.POST
         Recipe_name = data.get('Recipe_name')
         print(Recipe_name)
         Recipe_description = data.get('Recipe_description')
         Recipe_Image = request.FILES.get('Recipe_Image')
         Recipes.objects.create(
         Recipe_name= Recipe_name, 
         Recipe_description= Recipe_description, 

        #  Recipe_Ingrediants= Recipe_Ingrediants,
         Recipe_Image=Recipe_Image
         )
         print(data)
         print(Recipe_Image)
         return redirect('/')   
    recipesList = Recipes.objects.all()
    if data.get('search'):
        recipesList = Recipes.objects.filter(Recipe_name__icontains= data.get('search'))
    context = {'recipesList':recipesList}
    return render(request, 'recipeHome.html' ,context)

@login_required(login_url='/login')
def updateRecipe(request,id):
    recipe = Recipes.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe.Recipe_name = data.get('Recipe_name')
        recipe.Recipe_description = data.get('Recipe_description')
        image = request.FILES.get('Recipe_Image')
        # recipe.Recipe_Image = request.FILES.get('Recipe_Image')
        if image != None:
            recipe.Recipe_Image = image
        recipe.save()
        return redirect('/recipe')
    context = {'recipe':recipe}
    return render(request, 'updateRecipe.html',context)
@login_required(login_url='/login')
def deleteRecipe(request, id):
    recipe = Recipes.objects.get(id=id)
    recipe.delete()
    return redirect('/recipe')
def AddRecipe(request):
    return render(request, 'AddRecipe.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('/recipe')
        else :
            messages.error(request, 'Invalid Credentials, please try again!')
            # return HttpResponse('Invalid Credentials')
            return redirect('/login')
        # User.objects.create_user(username=data.get('username'), password=data.get('password'))

    return render(request, 'LoginPage.html')


def register_page(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.create_user(username=data.get('username'),password = data.get('password'))
        user.save()

        return redirect('/login')
    return render(request, 'RegisterPage.html')


