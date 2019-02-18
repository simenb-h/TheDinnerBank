from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

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
    return render(request, 'middager/insp.html')
    #return HttpResponse("Inspo")

def details(request, id):
    dinners = Dinner.objects.get(id=id)
    context = {
        'dinners' : dinners
    }
    
    return render(request, 'middager/details.html', context)
    