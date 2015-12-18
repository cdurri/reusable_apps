from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "blogtests.html",{'posts': posts})

def post_detail(request, id):

    post = get_object_or_404(Post, pk=id)

    post.views += 1 # clock up the number of post views

    post.save()

    return render(request, "blogdetail.html", {'post': post})

def top_posts(request):

    posts = Post.objects.filter().order_by('-views')

    return render(request, "blogtests.html", {'posts': posts})

def new_post(request):

    if request.method == "POST":

        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.published_date = timezone.now()

            post.save()

            return redirect(post_detail, post.pk)

    else:

        form = BlogPostForm()

        return render(request, 'blogpostform.html', {'form': form})

# Create your views here.
