from django.shortcuts import render
from django.http import HttpResponse


def savefile(f):
    file_write=open('C:/Users/shiva/Desktop/College/project/faceMaskUpdated/intelligent_faceMask_detecton/FaceMask_v1/static/img/'+f.name, 'wb')
    for chunk in f.chunks():
        file_write.write(chunk)
    file_write.close()
    return True


def index(request):
    return render(request, 'index.html')

def processing(request):
    img = request.FILES['imgFile']
    if savefile(img):
        msg = "uploaded and processing!"
    else:
        msg = "could't upload!"
    return render(request, "view.html", {'msg':msg, 'file_name':img.name})