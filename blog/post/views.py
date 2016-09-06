from django import template
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from . forms import PostForm
from .models import Post


def new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_form_data = form.save(commit=False)
            post_form_data.title = form.cleaned_data['title']
            post_form_data.post = form.cleaned_data['post']
            post_form_data.date = form.cleaned_data['date']
            post_form_data.author = form.cleaned_data['author']
            post_form_data.picture = form.cleaned_data['picture']


            post_form_data.save()
            return redirect(index)
    else:
        form = PostForm()
    return render(request, 'input_form.html', {'form':form})


def index(request):
    post = Post.objects.all()
    context = {'posts' : post}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

