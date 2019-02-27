from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import requests

token = '0fd35636dcmsh456f4676fdfddd9p17f0d0jsnec16eecfa825'


def add(request):
    # if request.method == 'POST': 
    #     form = DinnerForm(request.POST, request.FILES) 
    #     if form.is_valid(): 
    #         form.save() 
    #         return redirect('') 
    # else: 
    #     form = DinnerForm() 
    # return render(request, 'middager/add.html', {'form' : form}) 
  
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        dinner = Dinner(title=title, text=text)
        #place = request.POST['place']
        #todo = Todo(title=title, text=text, place=place
        dinner.save()

        return redirect('/')
    else:
        return render(request, 'middager/add.html')

  
def index(request):

    dinners = Dinner.objects.all()[::-1]
    context = {
        'dinners' : dinners
    }

    return render(request, 'middager/index.html', context)
    #return HttpResponse('successfuly uploaded') 
    # if request.method == 'GET':
    #     Dinners = Dinner.objects.all()
    #     context = {
    #         'dinner' : Dinners
    #     }
    #     return render ((request,'middager/index.html', context))



    #return render(request, 'middager/index.html')
    #return HttpResponse("Index")

def insp(request):
    r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=1", headers = {'X-Mashape-Key':token, "Content-Type": "application/json"})
    data = r.json()
    fetch = data['recipes'][0]
    return render(request, 'middager/insp.html', {
        'title' : data['recipes'][0]['title'],
        'instr' : fetch['instructions'],
        'src' : fetch['sourceUrl'],
        'img' : fetch['image']
    })
    
     
def ingrediens(request):
    r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=10&ranking=1&ingredients=chicken",headers = {'X-Mashape-Key':token, "Content-Type": "application/json"})
    data = r.json()
    context = {
        'middager' : data}
    return render(request, 'middager/ingrediens.html', context)


    # KALORIER:
    # r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate?targetCalories=2000&timeFrame=day", headers = {'X-Mashape-Key':token, "Content-Type": "application/json"})
    # data = r.json()
    # return render(request,'middager/ingrediens.html', {
    #     'planer' : data['meals']
    # })
   

def details(request, id):
    dinners = Dinner.objects.get(id=id)
    context = {
        'dinners' : dinners
    }
    
    return render(request, 'middager/details.html', context)
