from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    '''
    This is the location class
        '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    '''
    This is the neighborhood class
    '''
    name = models.CharField(max_length =30)
    police = models.TextField(null=True)
    hospital = models.TextField(null=True)
    location = models.ForeignKey(Location, null=True)
    occupants = models.IntegerField(null=True)





    @classmethod
    def get_location_contacts(cls, location):
        contacts = Neighborhood.objects.get(location__id=location)
        return contacts

    @classmethod
    def get_location_posts(cls, location):
        posts = Post.objects.filter(location__id=location)
        return posts



    def __str__(self):
        return self.name





class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    email = models.CharField(max_length =30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    neighborhood = models.ForeignKey(Neighborhood, null=True)



    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    class Meta:
        ordering = ['email']

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

class Category(models.Model):
    '''
    This is the cetegories class
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name




class Post(models.Model):
    '''
    This is post class model
    '''
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Neighborhood, null=True)
    profile = models.ForeignKey(User, null=True)


    def save_post(self):
        self.save()

    def delete_image(self):
        self.delete()



    @classmethod
    def get_profile_posts(cls, profile):
        posts = Post.objects.filter(profile__id=profile)
        return posts

    @classmethod
    def get_location_posts(cls, location):
        posts = Post.objects.filter(location__id=location)
        return posts

    @classmethod
    def search_by_category(cls, search_term):
        # cat = category.objects.get(name=search_term)
        posts = cls.objects.filter(category__name__icontains=search_term)
        return posts

    @classmethod
    def search_by_location(cls, search_term):
        posts = cls.objects.filter(location__name__icontains=search_term)
        return posts


    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


class Business(models.Model):
    '''
    This is image class model
    '''
    name = models.CharField(max_length=60)
    description = models.TextField()
    products = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField(null=True)




    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    @classmethod
    def get_neighborhood_business(cls, neighborhood):
        business = Business.objects.filter(neighborhood__id=neighborhood)
        return business

    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def all_business(cls):
        business = cls.objects.all()
        return business

















