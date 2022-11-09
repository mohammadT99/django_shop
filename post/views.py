from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Post , contact
# Create your views here.
def home(request):
    return HttpResponse("hello wellcome to my website !")



def index(request):
    post=Post.objects.filter(status="P").order_by('-publish')
    contex={'post':post}

    return render(request,'web2/index.html',contex)
#______________________________________________________________--

def detail(request , slug):
    details = get_object_or_404(Post , slug=slug , status="P")
    context={'detail':details}

    return render(request , 'web2/post.html' , context)

#______________________________________________________________
def about(request):

        return render(request,'web2/about.html',{})
#___________________________________________________________
def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        print(name,email,message,phone)
        contact.objects.create(name=name , email=email ,  phone= phone , masege=message )
        return redirect('web:index')
    else:
        return  render(request,'web2/contact.html',{})
#______________________________________________________




