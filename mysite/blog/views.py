from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse as HR
from .models import Post , Infodata
from .forms import Dataform

def post_list(request):
#    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    login_data = Infodata.objects.all()
#    return render(request, 'blog/post_list.html', {'posts' : posts})
    return render(request, 'blog/post_list.html', {'login_data' : login_data})

def login_data(request):
    if request.method == 'POST':
        form = Dataform(request.POST)
        obj = Infodata(info_id = form.data['info_id'] , info_pw = form.data['info_pw'] , login_date = timezone.now())
        obj.save()
        return HR('success')
    elif request.method == 'GET':
        form = Dataform()
        return render(request, 'blog/login_data.html', {'form':form})
    else:
        return HR('fail')

# Create your views here.
