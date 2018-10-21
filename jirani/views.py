from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,EditProfileForm,PostForm,BusinessForm,CommentsForm
from .models import Profile,Post,Neighborhood,Business
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
#
# # Create your views here.
# @receiver(post_save,sender=User)
# def create_profile(sender, instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save,sender=User)
# def save_profile(sender, instance,**kwargs):
#     instance.profile.save()


@login_required(login_url='/login')
def index(request):
    # posts = Post.objects.all()

    return render(request,'index.html')


def home(request,location_id):
    location = Neighborhood.objects.get(id=location_id)

    try:
        location_details=Post.objects.filter(location=location)
    except:
        location_details = Neighborhood.filter(location.id)
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
            return redirect('auth_login')

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
            upload.location = request.user.profile.neighborhood
            upload.save()
            return redirect('profile',username=request.user)
    else:
        form = PostForm()

    return render(request, 'profile/upload_post.html', {'form': form})



def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.neighborhood = request.user.profile.neighborhood
            upload.save()
            return redirect('profile',username=request.user)
    else:
        form = BusinessForm()

    return render(request, 'add_business.html', {'form': form})


def business(request,neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)

    try:
        neighborhood_details=Business.objects.filter(neighborhood=neighborhood)
    except:
        neighborhood_details = Neighborhood.filter(location.id)
    business = Business.get_neighborhood_business(neighborhood.id)

    return render(request, 'business.html', {"business": business, "location_details":neighborhood_details, "neighborhood":neighborhood})


0

def occupants(request,location_id):
    location = Neighborhood.objects.get(id=location_id)

    try:
        location_details=Neighborhood.objects.filter(location=location)
    except:
        location_details = Neighborhood.filter(location.id)
    occupants = Profile.objects.all()

    return render(request, 'home.html', {"occupants": occupants, "location_details":location_details, "location":location})



def search_business(request):
    if 'name' in request.GET and request.GET['name']:
        search_term = request.GET.get('name')
        business = Business.search_business(search_term)

        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'business':business})
    else:
        message = 'Type business name'
        return render(request, 'search.html', {'message':message})


@login_required(login_url='/login')
def add_comment(request,post_id):
    posts = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = request.user.profile
            comment.post = posts
            comment.save()
    return redirect('home',request.user.profile.neighborhood.id)







