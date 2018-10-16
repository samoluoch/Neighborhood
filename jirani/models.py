from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

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
    This is image class model
    '''
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location, null=True)

    def save_post(self):
        self.save()

    def delete_image(self):
        self.delete()

    # @classmethod
    # def todays_image(cls):
    #     today = dt.date.today()
    #     image = cls.objects.filter(pub_date__date=today)
    #     return image

    @classmethod
    def search_by_category(cls, search_term):
        # cat = category.objects.get(name=search_term)
        posts = cls.objects.filter(category__name__icontains=search_term)
        return posts

    @classmethod
    def search_by_location(cls, search_term):
        posts = cls.objects.filter(location__name__icontains=search_term)
        return posts

    # @classmethod
    # def days_image(cls, date):
    #     image = cls.objects.filter(pub_date__date=date)
    #     return image

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


















