from unittest import mock

from django.core.cache import cache
from django.test import TestCase

from wagtail.contrib.redirects.models import Redirect

from developerportal import context_processors

from ...topics.models import Topics


class ContextProcessorsTestCase(TestCase):

    fixtures = ["common.json"]

    def setUp(self):
        cache.clear()

    def tearDown(self):
        cache.clear()

    def test_topics_title(self):

        self.assertEqual(Topics.objects.get().title, "Products & Technologies")
        self.assertIsNone(cache.get(Topics.CACHE_KEY_TOPICS_TITLE))
        self.assertEqual(
            context_processors.topics_title(request=mock.Mock()),
            {"TOPICS_TITLE_LABEL": "Products & Technologies"},
        )
        self.assertEqual(
            cache.get(Topics.CACHE_KEY_TOPICS_TITLE), "Products & Technologies"
        )

    def test_topics_title__fallback(self):
        Topics.objects.all().delete()
        self.assertIsNone(cache.get(Topics.CACHE_KEY_TOPICS_TITLE))
        self.assertEqual(
            context_processors.topics_title(request=mock.Mock()),
            {"TOPICS_TITLE_LABEL": "Topics"},
        )
        self.assertIsNone(cache.get(Topics.CACHE_KEY_TOPICS_TITLE))

    def test_blog_link(self):

        TARGET_URL = "https://hacks.mozilla.org"
        PATH = "/blog"
        # Ensure there's a blog link/redirect set up
        redirect, created = Redirect.objects.get_or_create(
            old_path=PATH, redirect_link=TARGET_URL, is_permanent=False
        )

        self.assertEqual(
            context_processors.blog_link(request=mock.Mock()), {"BLOG_LINK": PATH}
        )

        # Now confirm behavior if the link is not there
        redirect.delete()
        self.assertEqual(
            context_processors.blog_link(request=mock.Mock()), {"BLOG_LINK": None}
        )
