# accounts/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile

class AccountsAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')
        self.username = 'testuser'
        self.password = 'testpass123'

    def test_register_creates_user_and_profile(self):
        resp = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        user_exists = User.objects.filter(username='newuser').exists()
        self.assertTrue(user_exists)
        user = User.objects.get(username='newuser')
        # profile should be created by signal
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_login_logout_flow(self):
        User.objects.create_user(username=self.username, password=self.password)
        login = self.client.post(self.login_url, {'username': self.username, 'password': self.password}, follow=True)
        self.assertTrue(login.context is not None or login.status_code == 200)
        # profile page requires login
        resp = self.client.get(self.profile_url)
        self.assertEqual(resp.status_code, 200)
        # logout
        self.client.get(self.logout_url, follow=True)
        resp = self.client.get(self.profile_url, follow=True)
        # should be redirected to login
        self.assertNotEqual(resp.status_code, 200)
        self.assertIn('/accounts/login', resp.redirect_chain[0][0] if resp.redirect_chain else '')

    def test_profile_update_email_and_bio_and_image(self):
        user = User.objects.create_user(username='u2', password='pass1234')
        self.client.login(username='u2', password='pass1234')
        # in-memory image
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x4C'
            b'\x01\x00\x3B'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        resp = self.client.post(self.profile_url, {
            'email': 'newemail@example.com',
            'bio': 'Hello bio',
            'profile_picture': uploaded,
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        user.refresh_from_db()
        profile = user.userprofile
        self.assertEqual(user.email, 'newemail@example.com')
        self.assertEqual(profile.bio, 'Hello bio')
        self.assertTrue(bool(profile.profile_picture))  # file saved

