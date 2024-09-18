from django.shortcuts import render, redirect
from .models import BlogPost, BirthdayWish
from .forms import BirthdayWishForm

def home(request):
    # Get all blog posts and birthday wishes from the database
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    wishes = BirthdayWish.objects.all().order_by('-created_at')  # Fetching all wishes

    if request.method == 'POST':
        form = BirthdayWishForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new wish
            return redirect('home')
    else:
        form = BirthdayWishForm()

    return render(request, 'home.html', {
        'blog_posts': blog_posts,
        'form': form,
        'wishes': wishes  # Passing wishes to the template
    })
