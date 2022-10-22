from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList
# Create your views here.


def home(response):
    return render(response, 'main/home.html')

def v1(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    print('c' + str(item.id), item.complete, response.POST.get('c' + str(item.id)))
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        print('aa')
                        item.complete = False
                    print(item.complete)
                item.save()
        elif response.POST.get('NewItem'):
            txt = response.POST.get('new')
            if len(txt) > 2:
                ls.item_set.create(text = txt, complete = False)
            else:
                print('invalid')


    return render(response, 'main/list.html', {'ls':ls})


def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            t = ToDoList(name = form.cleaned_data['name'])
            t.save()

            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html',{"form":form})