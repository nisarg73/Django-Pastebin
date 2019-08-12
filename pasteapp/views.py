from django.shortcuts import render
from django.http import HttpResponse
from .models import Paste
from django.template import loader
# Create your views here.
"""
def index(request):
    if request.method=="GET":
        return HttpResponse("Yo! I work")
"""
def ret_objects(request, paste_url):
    if request.method == "GET":
        obj = Paste.objects.get(url=paste_url)
        temp = 'Name is {0}, content is {1} and uploader is  {2}'.format(obj.name,obj.content,obj.uploader)
        return HttpResponse(temp)

def index(request):
    if request.method == "GET":
        paste_list = Paste.objects.all()
        template = loader.get_template('temp.html')
        context = {
                'paste_list' : paste_list,
        }
        return HttpResponse(template.render(context,request))
    if request.method == "POST":
        name = request.POST['name']
        content = request.POST['content']
        uploader = request.POST['uploader']
        url = request.POST['url']
        p = Paste.objects.create(name=name,content=content,uploader=uploader,url=url);
        paste_list = Paste.objects.all()
        template = loader.get_template('temp.html')
        context = {
                'paste_list' : paste_list,
        }
        return HttpResponse(template.render(context,request))
