from django.test import TestCase
from posts.models import Post
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


class BaseModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.User = get_user_model().objects.create_user(
            username='test',
            password='12test12',
            email='test@example.com'
        )
        cls.User.save()
        cls.post = Post(
            title='test title',
            slug='test-title',
            content='this is a test content',
            author=cls.User,
            status=1
        )
        cls.post.save()


class PostModelTest(BaseModelTestCase):

    def test_correct_title(self):
        self.assertEqual(self.post.title, 'test title')

    def test_title_label(self):
        field_label = self.post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_first_name_max_length(self):
        max_length = self.post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_post_has_slug(self):
        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.post.content, str)
        self.assertIsInstance(self.post.title, str)
