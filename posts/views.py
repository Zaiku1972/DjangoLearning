from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if (form.is_valid()):
        instance = form.save(commit=False)
        instance.save()


    context = dict()
    context['form'] = form

    return render(request,"post_form.html",context)

def post_detail(request,id=None): #retrive
    instance = get_object_or_404(Post,id = id)
    context = dict()
    context['title'] = instance.title
    context['instance'] = instance
    return render(request,"post_detail.html",context)

def post_list(request): #list items

    context = dict()
    context['title'] = 'List'
    context['object_list'] = Post.objects.all()
    return render(request, "index.html", context)
    # return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
