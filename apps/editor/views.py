from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm 

# Create your views here.
def index(request):
    return render(request, 'editor/index.html', {'object_list': Post.objects.all()})


def add_post(request): 
    form = PostForm() 
    if request.method == "POST": 
        form = PostForm(request.POST) 
        if form.is_valid(): 
            post_item = form.save(commit=False) 
            post_item.save() 
            return redirect('ckeditor') 
    return render(request, 'editor/post_form.html', {'form': form})


def edit_post(request, post_id=None): 
    # item = get_object_or_404(Post, id=post_id) 
    item = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=item) 
    if form.is_valid(): 
        form.save() 
        return redirect('ckeditor') 
    return render(request, 'editor/post_form.html', {'form': form}) 
