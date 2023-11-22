from django.shortcuts import render, redirect

# Create your views here.
from project_app.forms import TodoForm
from project_app.models import Todo


def home(request):
    return render(request,'example.html')


def index(request):
    return render(request,'index.html')
#create
def new(request):
    form = TodoForm()
    if request.method == "POST":
        data=TodoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("read")

    return render(request,"index.html",{'form1':form})
#read
def read(request):
    data = Todo.objects.all()
    return render(request,"read.html",{"data":data})

#delete
def delt(request,id):
    if request.method == 'POST':
        data=Todo.objects.get(id=id)
        data.delete()
        return redirect("read")
#update
def update(request,id):
    todo= Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    if request.method == 'POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('read')
    return render(request,'update.html',{'form':form})


