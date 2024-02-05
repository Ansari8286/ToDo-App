from django.shortcuts import render
from django.http import JsonResponse
from .models import ToDo
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.
def Todolist(request):
    allTodo = ToDo.objects.all()
    return render(request, 'todolist.html', {'allTodo':allTodo})
    
def TodoForm(request):
    if request.method == 'POST' and request.FILES['file']:
        pid = request.POST.get('pid')
        todo = request.POST.get('todo')
        uploaded_file = request.FILES['file']
        file_path = default_storage.save('files/' + uploaded_file.name, ContentFile(uploaded_file.read()))

        if (pid == ''):
            form = ToDo(name=todo, file=file_path)
        else:
            form = ToDo(id=pid, file=file_path, name=todo)

        form.save()
        allTodo = list(ToDo.objects.values())
        return JsonResponse({'data':'save','todo':allTodo})

    return render(request, 'todolist.html')

def Delete(request):
    if request.method == 'POST':
        did = request.POST.get('did')
        data = ToDo.objects.get(id=did)
        data.delete()
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})

def Update(request):
    if request.method == 'POST':
        did = request.POST.get('uid')
        data = ToDo.objects.get(id=did)
        FormData = {"uid":data.id, "name":data.name, "disc":data.disc}
        return JsonResponse(FormData)

def search(request):
    search = request.GET['search']
    name = ToDo.objects.filter(name__icontains=search)
    disc = ToDo.objects.filter(disc__icontains=search)
    edit = ToDo.objects.filter(edit__icontains=search)
    is_verifed = ToDo.objects.filter(is_verifed__icontains=search)

    allTodo = name.union(disc, edit, is_verifed)
    return render(request, 'todolist.html', {'allTodo':allTodo})