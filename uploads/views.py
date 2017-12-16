from .forms import uploadForm 
from .models import file
from django.shortcuts import render,redirect

def upload(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            inst = file(name=request.POST['name'],file=request.FILES['file'])
            inst.save()
            return redirect('/home/')
    else:
        form = uploadForm()
        print("Upload Form")
    return render(request, 'upload.html', {
        'form': form
    })

def home(request):
    return render(request,'home.html')