from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Post

# from datetime import datetime

# ===> the form that we want to display to the user interface
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'myapp/home.html')


def blog(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'myapp/blog.html', context)


# we want to get each of the blogs by their slug
def detailsPage(request, slug):
    # the first slug is coming from our models.py file and the parameter above
    post_detail = Post.objects.get(slug=slug)
    # To get the recent posts without including the most of the text from the details page.
    # so we are excluding the current post that we are on when we are when we have click the details page
    # we also want to get the post id
    # [ post_id__exact ] this means that is the current post is equal to the current that we are on which is also inside the, so we want to make sure that post is excluded
    # it is going to list out the recent post, but excluding the current post that we are on
    recent_post_detail = Post.objects.exclude(post_id__exact = post_detail.post_id)[:5]
    
    context = {'post_detail' :post_detail,
               'recent_post_detail' : recent_post_detail           
               }
    return render(request, 'myapp/details.html', context)




def createPost(request):
    # ! you cannot create a post if you are not logged in.
    # ?  [request.user.userprofile] refers to the login user
    profile = request.user.userprofile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            # This post is an instance of the Post model
            post = form.save(commit=False)
            # ===> Anytime we create a title we want it to be prefiled so ( import slugify )
            # slugify the title 
            
            # * [post] will be equal to the logged in user.
            
            
            # Todo: [exclude writer in the forms.py]
            post.writer = profile
            
            post.slug = slugify(post.title)
            post.save()
            
            messages.info(request, 'Post created successfully')
            
            return redirect('create-blog')
        else:
            messages.error(request, 'Post not created')
    context = {'form' : form}
    return render(request, 'myapp/create.html', context)






# ===> ( slug ) we are gtting each post by their slug
def updatePost(request, slug):
    post = Post.objects.get(slug = slug)
    # we want to update the blog post
    # we want to make sure a blog is prefilled with the particular one we are requesting for
    form = PostForm(instance = post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post updated successfully')
            
            # After saving it, return to that particular post that you have updated.
            return redirect('detail', slug = post.slug)
    context = {'form' : form}
    return render(request, 'myapp/create.html', context)





def deletePost(request, slug):
    post = Post.objects.get(slug = slug)
    form = PostForm(instance = post)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Post deleted successfully')
        return redirect('create-post')
    context = {'form' : form}
    return render(request, 'myapp/delete.html', context)