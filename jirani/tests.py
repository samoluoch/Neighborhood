from django.test import TestCase
from .models import Profile,Post,Business,Neighborhood
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.samsoluoch = Profile(name = 'samsoluoch')
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


class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.moringa = Neighborhood.objects.create(name="moringa")

        self.test_neighborhood = Neighborhood.objects.create(neighborhood_name='moringa',)
        self.test_neighborhood.save()

    def test_save_method(self):
        self.test_neighborhood.save()
        test_neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(test_neighborhood) > 0)

    # Testing save method
    def test_save_neighbourhood(self):
        self.assertEqual(len(Neighborhood.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_delete_neighbourhood(self):
        Neighborhood.delete_image_by_id(self.test_neighbourhood.id)
        self.assertEqual(len(Neighborhood.objects.all()), 0)

    def test_update_neighbourhood(self):
        self.testneighbourhood.save_post()
        self.testneighbourhood.update_neighbourhood()
        neighbourhood = Neighborhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_update_occupants(self):
        self.testoccupants.save_post()
        self.testoccupants.update_occupants()
        occupants = Neighborhood.objects.all()
        self.assertTrue(len(occupants) > 0)

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




class BusinessTestClass(TestCase):

    def setUp(self):
        self.user.profile = User.profile.objects.create(id=1, username='a')
        self.neighborhood = Neighborhood(name='moringa', location='daykio', user=self.user.profile)
        self.neighborhood.save_hood()
        self.business = Business(name="prestige-motors", email="pre@gmail.com", description="we sel cars", products="land-rover", user=self.user.profile, neighborhood=self.moringa)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_method(self):
        self.business.save_business()
        self.business.delete_business()


    def test_find_business_by_id(self):

        self.business.save_business()
        search_business = self.business.find_business_by_id(self.business.id)
        business = Business.objects.get(id=self.business.id)
        self.assertTrue(search_business, business)

    def test_update_method(self):
        self.business.save_business()
        new_business = Business.objects.filter(name='prestige-motors').update(name='prestige')
        business = Business.objects.get(name='prestige')
        self.assertTrue(business.name, 'prestige')