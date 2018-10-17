from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse,Http404
# from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,EditProfileForm,PostForm
from .models import Profile,Post,Location

# Create your views here.

# def home(request):
#     posts = Post.objects.all()
#     return render(request,'home.html', {"posts":posts})


def home(request,location_id):
    location = Location.objects.get(id=location_id)

    try:
        location_details=Post.objects.filter(location=location)
    except:
        location_details = Location.filter(location.id)
    posts = Post.get_location_posts(location.id)

    return render(request, 'home.html', {"posts": posts, "location_details":location_details, "location":location})



def register(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # user.is_active = False
                user.save()
                # current_site = get_current_site(request)
                # to_email = form.cleaned_data.get('email')
                # activation_email(user, current_site, to_email)
                # return HttpResponse('Please confirm your email')
            return redirect('home.html')

        else:
            form = RegistrationForm()
        return render(request, 'registration/signup.html',{'form':form})



def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    posts = Post.get_profile_posts(profile.id)
    title = f'@{profile.username} Projects'


    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'posts':posts, 'profile_details':profile_details})



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile',username=request.user)
    else:
        form = EditProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})



def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('profile',username=request.user)
    else:
        form = PostForm()

    return render(request, 'profile/upload_post.html', {'form': form})

















def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Type profile'
        return render(request, 'search.html', {'message':message})

    # def home(request, location):
    #     location = Location.objects.get(name=location)
    #     try:
    #         location_details = Post.objects.filter(location=location)
    #     except:
    #         location_details = Location.filter_by_id(location.id)
    #     posts = Post.get_location_posts(location.id)
    #
    #     return render(request, 'home.html',
    #                   {"posts": posts, "location_details": location_details, "location": location})