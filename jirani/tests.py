from django.test import TestCase
from .models import Profile,Post

# Create your tests here.
class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.samsoluoch = Profile(bio = 'samsoluoch')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.samsoluoch,Profile))
    #testing save method
    def test_save_profile(self):
        self.samsoluoch.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)


    #testng for deleting method
    def test_delete_profile(self):
        self.samsoluoch.save_profile()
        self.samsoluoch.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)


class PostTestClass(TestCase):
    #set Up method
    def setUp(self):
        self.testpost = Post(post = 'testproject')
    #test  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testpost,Post))
    #testing for saving method
    def test_save_post(self):
        self.testpost.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)
    #testing for deleting method
    def test_delete_project(self):
        self.testpost.save_post()
        self.testpost.delete_project()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)
    #testing for update caption
    def test_update_caption(self):
        self.testpost.save_post()
        self.testpost.update_caption()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

