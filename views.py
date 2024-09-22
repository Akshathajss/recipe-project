from ssl import AlertDescription
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .models import Recipe,commentbox

def home(request):
    return render(request,'home.html')

def recipe_detail(request):
    if request.method == "GET":
        query = request.GET.get('dish_name')
        recipe = None
        if query:
            try:
                recipe = Recipe.objects.get(name__iexact=query)
            except Recipe.DoesNotExist:
                pass
        if query == None or recipe == None:
            return render(request, 'recipe_detail.html', {'recipe': recipe, 'query': query})
        else:
            dish_list=list()
            dish_list=recipe.procedure.split("\n")
            dish_list1=list()
            dish_list1=recipe.ingredients.split("\n")
            return render(request, 'recipe_detail.html', {'recipe': recipe, 'query': query,'dish_list':dish_list,'dish_list1':dish_list1})
    if request.method == "POST":
        comm=request.POST.get("commtext")
        uname=request.POST.get("uname")
        star=request.POST.get("star")
        record=commentbox(
            com_name=uname,
            com_content=comm,
            rating=star,
        )
        record.save()
        list1=commentbox.objects.all()
        return HttpResponse("<h1>comment is recorded</h1>")
    
def comment(request):
    if request.method == "POST":
        star=request.POST.get("star1")
        comm=request.POST.get("commtext")
        uname=request.POST.get("uname")
        record=commentbox(
            com_name=uname,
            com_content=comm,
            rating=star,
        )
        record.save()
        return redirect(request, 'recipe_detail.html',)
    else:
        commen=commentbox.objects.all()
        return render(request,"comment_list.html",{"commen":commen})
        
def dishes(request,num):
    recipe = Recipe.objects.get(id=num)
    dish_list=list()
    dish_list=recipe.procedure.split("\n")
    dish_list1=list()
    dish_list1=recipe.ingredients.split("\n")
    return  render(request, 'recipe_detail.html', {'recipe': recipe,'dish_list':dish_list,'dish_list1':dish_list1})

def southIndian(request,num1):
        foods=Recipe.objects.all()
        food_list=list()
        for food in foods:
            if food.cuisine_number == num1:
                food_list.append(food)
        return render(request,"food_menu.html",{"food_list":food_list,"num1":num1})