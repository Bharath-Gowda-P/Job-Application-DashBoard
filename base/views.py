from cmath import phase
from unicodedata import name
from django.shortcuts import redirect, render
from . models import candidate_info
from django.http import FileResponse

# Create your views here.
def home(request):
    data = candidate_info.objects.all()
    context = {'data': data}
    return render(request, 'base/home.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        course = request.POST['course']
        degree = request.POST['degree']
        yoe = request.POST['yoe']
        pcompany = request.POST['pcompany']
        skills = request.POST['skills']
        resume = request.FILES['file']
        status = request.POST['status']
        newentry = candidate_info(name = name, phone = phone, address = address, course = course, degree = degree, yoe = yoe, pcompany = pcompany, skills = skills, resume = resume, status = status)
        newentry.save()
        return redirect('/')
    return render(request, 'base/add.html')


def candidate(request, id):
    obj = candidate_info.objects.get(id = id)
    context = {'obj': obj}
    return render(request, 'base/candidate.html', context)


def download(request, id):
    obj = candidate_info.objects.get(id=id)
    filename = obj.resume.path
    response = FileResponse(open(filename, 'rb'))
    return response


def edit(request, id):
    if request.method == 'POST':
        status = request.POST['status']
        new = candidate_info.objects.get(id = id)
        new.status = status
        new.save()
        return redirect('/')
