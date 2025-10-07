from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class AccountsAuthTests(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_register_creates_user_and_profile(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'ComplexPwd123',
            'password2': 'ComplexPwd123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        new_user = User.objects.get(username='newuser')
        self.assertTrue(UserProfile.objects.filter(user=new_user).exists())

    def test_login_logout_flow(self):
        # Login
        login_resp = self.client.post(self.login_url, {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(login_resp.status_code, 302)
        # Access profile
        profile_resp = self.client.get(self.profile_url)
        self.assertEqual(profile_resp.status_code, 200)
        # Logout
        self.client.get(reverse('logout'))
        # Profile should redirect to login now
        profile_resp2 = self.client.get(self.profile_url)
        self.assertNotEqual(profile_resp2.status_code, 200)

    def test_profile_update_email_bio_and_image(self):
        self.client.login(username='testuser', password='password123')
        profile = self.user.userprofile
        response = self.client.post(self.profile_url, {
            'bio': 'New bio content',
            'email': 'newemail@example.com'
        })
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.user.refresh_from_db()
        self.assertEqual(profile.bio, 'New bio content')
        self.assertEqual(self.user.email, 'newemail@example.com')
