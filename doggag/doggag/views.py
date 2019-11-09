from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


def upload(request):
    context = {} #this line if want to display name of uploaded file
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        #to display uploaded file name in html view
        context['url'] = fs.url(name)
    return render(request,'upload.html',context)
