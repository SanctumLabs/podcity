from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Episode


class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title='Test Episode',
            description='Look Ma! I am awesome',
            pub_date=timezone.now(),
            link='http://example.com/podcast/test-episode.mp3',
            image='http://example.com/podcast/test-episode.jpg',
            podcast_name='Test Podcast',
            guid="i7wos89cruje89kfvyno7845yt7onjuvtm4"
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, 'Look Ma! I am awesome')
        self.assertEqual(self.episode.title, 'Test Episode')
        self.assertEqual(self.episode.link, 'http://example.com/podcast/test-episode.mp3')
        self.assertEqual(self.episode.image, 'http://example.com/podcast/test-episode.jpg')
        self.assertEqual(self.episode.podcast_name, 'Test Podcast')
        self.assertEqual(self.episode.guid, "i7wos89cruje89kfvyno7845yt7onjuvtm4")

    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), 'Test Podcast: Test Episode')

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Test Episode")
