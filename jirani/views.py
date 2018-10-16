from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse,Http404
# from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # images = Image.objects.all()
    return render(request,'home.html')


def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Type profile'
        return render(request, 'search.html', {'message':message})