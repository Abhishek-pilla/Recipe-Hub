from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    if request.method != 'POST':
        data = request.POST
        Recipe_name = data.get('Recipe_name')
        print(Recipe_name)
        Recipe_description = data.get('Recipe_description')
        Recipe_Ingrediants = data.get('Recipe_Ingrediants')
        Recipe_Image = data.get('Recipe_Image')
        console.log(Recipe_name)
        Recipe.objects.create(Recipe_name=Recipe_name, Recipe_description=Recipe_description, Recipe_Ingrediants=Recipe_Ingrediants, Recipe_Image=Recipe_Image)
    # function.sleep(5)
    # redirect('home')
        # return HttpResponse('Recipe added successfully')
        # return addRecipe(request)
    return render(request, 'homePage.html')

# def addRecipe(request):
#     data = request.POST
#     Recipe_name = data.get('Recipe_name')
   
#     print(Recipe_name)
#     function.sleep(5)
#     redirect('home')
#     return HttpResponse('Recipe added successfully')
#     return render(request, 'addRecipe.html')