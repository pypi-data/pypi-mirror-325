# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from django.core.files.storage import default_storage
from django.template import Context, Template
from PIL import Image, ImageDraw
from initial_avatars.generator import AvatarGenerator
from initial_avatars.utils import AvatarShapeException
from datetime import datetime


class TestAvatarGenerator(TestCase):

    TEMPLATE = Template("{% load initialavatar %} {% get_initial_avatar user %}")

    def setUp(self):
        self.userA = User.objects.create_user(
            username='Stéphane',
            email='admin@axiome.io',
            password='top_secret'
        )
        self.genA = AvatarGenerator(
            self.userA,
            80
        )
        self.userB = User.objects.create_user(
            username='matt',
            first_name='matt',
            last_name='something',
            email='matt@automattic.com',
            password='top_secret'
        )
        self.genB = AvatarGenerator(
            self.userB,
            80
        )
        self.userC = User.objects.create_user(
            username='carlotta',
            first_name='carlotta',
            last_name='da Silva',
            email='cs@automattic.com',
            password='top_secret'
        )
        self.genC = AvatarGenerator(
            self.userC,
            80
        )
    def test_text(self):
        self.assertEqual(
            self.genA.text(),
            'S'
        )
        self.assertEqual(
            self.genB.text(),
            'MS'
        )
        self.assertEqual(
            self.genC.text(),
            'CS'
        )

    def test_font_size(self):
        self.assertEqual(
            self.genA.font_size(),
            720
        )
        self.assertEqual(
            self.genB.font_size(),
            640
        )

    def test_brightness(self):
        self.assertEqual(
            int(self.genA.brightness()),
            219
        )
        self.assertEqual(
            int(self.genB.brightness()),
            200
        )

    def test_background(self):
        self.assertEqual(
            self.genA.background(),
            (3, 254, 229)
        )
        self.assertEqual(
            self.genB.background(),
            (208, 207, 63)
        )

    def test_foreground(self):
        self.assertEqual(
            self.genA.foreground(),
            (0, 0, 0)
        )
        self.assertEqual(
            self.genB.foreground(),
            (0, 0, 0)
        )

    def test_name(self):
        self.assertEqual(
            self.genA.name(),
            "80x80_square.jpg"
        )
        self.assertEqual(
            self.genB.name(),
            "80x80_square.jpg"
        )

    def test_path(self):
        self.assertEqual(
            self.genA.path(),
            "avatars\\8ac609169cd18386d2e1800b253511ce\\80x80_square.jpg"
        )
        self.assertEqual(
            self.genB.path(),
            "avatars\\a777f9544392312fd067b7d4762ea083\\80x80_square.jpg"
        )

    def test_get_avatar_url(self):
        self.assertEqual(
            self.genA.get_avatar_url(),
            "http://django-initial-avatars.py/avatars/8ac609169cd18386d2e1800b253511ce/80x80_square.jpg"
        )
        self.assertIn(
            self.genB.get_avatar_url(),
            [
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;r=g&amp;d=mm",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;d=mm&amp;r=g",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=80&amp;d=mm",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=80",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=80&amp;r=g",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=80"
            ]
        )

    def test_get_avatar(self):
        default_storage.delete('avatars/8ac609169cd18386d2e1800b253511ce/80x80_square@2x.jpg')
        default_storage.delete(self.genA.path())

        self.assertFalse(default_storage.exists(self.genA.path()))

        self.assertEqual(
            self.genA.get_avatar(),
            '<img class="initial-avatar" src="http://django-initial-avatars.py/avatars/8ac609169cd18386d2e1800b253511ce/80x80_square.jpg" width="80" height="80"/>'
        )
        self.assertIn(
            self.genB.get_avatar(),
            [
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;r=g&amp;d=mm" width="80" height="80"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;d=mm&amp;r=g" width="80" height="80"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=80&amp;d=mm" width="80" height="80"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=80" width="80" height="80"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=80&amp;r=g" width="80" height="80"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=80" width="80" height="80"/>'
            ]
        )
        self.assertTrue(default_storage.exists(self.genA.path()))

    def test_last_modified(self):
        self.assertIsInstance(
            self.genA.last_modification(),
            datetime
        )
        self.assertIsInstance(
            self.genB.last_modification(),
            datetime
        )

    def test_template_tags(self):
        renderedA = self.TEMPLATE.render(Context({'user': self.userA}))
        renderedB = self.TEMPLATE.render(Context({'user': self.userB}))
        renderedAnon = self.TEMPLATE.render(Context({'user': AnonymousUser()}))

        self.assertEqual(
            renderedA,
            u' <img class="initial-avatar" src="http://django-initial-avatars.py/avatars/8ac609169cd18386d2e1800b253511ce/80x80_square.jpg" width="80" height="80"/>'
        )
        self.assertIn(
            renderedB,
            [
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;r=g&amp;d=mm" width="80" height="80"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=80&amp;d=mm&amp;r=g" width="80" height="80"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=80&amp;d=mm" width="80" height="80"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=80" width="80" height="80"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=80&amp;r=g" width="80" height="80"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=80" width="80" height="80"/>'
            ]
        )
        self.assertEqual(
            renderedAnon,
            u' <img src="" width="80" height="80"/>'
        )

    def test_view(self):
        responseA = self.client.get('/1/')
        responseB = self.client.get('/2/')
        responseAnon = self.client.get('/anon/')

        self.assertEqual(
            responseA.status_code,
            302
        )
        self.assertEqual(
            responseB.status_code,
            302
        )
        self.assertEqual(
            responseAnon.status_code,
            404
        )


class TestAvatarGeneratorNotDefault(TestCase):

    TEMPLATE = Template("{% load initialavatar %} {% get_initial_avatar user 150 'circle' %}")

    def setUp(self):
        self.userA = User.objects.create_user(
            username='JAB',
            email='admin@axiome.io',
            password='top_secret'
        )
        self.genA = AvatarGenerator(self.userA, size=150, shape='circle')
        self.userB = User.objects.create_user(
            username='matt',
            first_name='matt',
            last_name='something',
            email='matt@automattic.com',
            password='top_secret'
        )
        self.genB = AvatarGenerator(self.userB, size=150)

    def test_text(self):
        self.assertEqual(
            self.genA.text(),
            'J'
        )
        self.assertEqual(
            self.genB.text(),
            'MS'
        )

    def test_font_size(self):
        self.assertEqual(
            self.genA.font_size(),
            1350
        )
        self.assertEqual(
            self.genB.font_size(),
            1200
        )

    def test_brightness(self):
        self.assertEqual(
            int(self.genA.brightness()),
            222
        )
        self.assertEqual(
            int(self.genB.brightness()),
            200
        )

    def test_background(self):
        self.assertEqual(
            self.genA.background(),
            (157, 242, 216)
        )
        self.assertEqual(
            self.genB.background(),
            (208, 207, 63)
        )

    def test_foreground(self):
        self.assertEqual(
            self.genA.foreground(),
            (0, 0, 0)
        )
        self.assertEqual(
            self.genB.foreground(),
            (0, 0, 0)
        )

    def test_name(self):
        self.assertEqual(
            self.genA.name(),
            "150x150_circle.png"
        )
        self.assertEqual(
            self.genB.name(),
            "150x150_square.jpg"
        )

    def test_path(self):
        self.assertEqual(
            self.genA.path(),
            "avatars\\963f42f411a171630625f6163ef581c3\\150x150_circle.png"
        )
        self.assertEqual(
            self.genB.path(),
            "avatars\\a777f9544392312fd067b7d4762ea083\\150x150_square.jpg"
        )

    def test_get_avatar_url(self):
        self.assertEqual(
            self.genA.get_avatar_url(),
            "http://django-initial-avatars.py/avatars/963f42f411a171630625f6163ef581c3/150x150_circle.png"
        )
        self.assertIn(
            self.genB.get_avatar_url(),
            [
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;r=g&amp;d=mm",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;d=mm&amp;r=g",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=150&amp;r=g",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=150",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=150&amp;d=mm",
                "https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=150",
            ]
        )

    def test_get_avatar(self):
        default_storage.delete(self.genA.path())
        default_storage.delete('avatars/963f42f411a171630625f6163ef581c3/150x150_circle@2x.png')
        self.assertFalse(default_storage.exists(self.genA.path()))

        self.assertEqual(
            self.genA.get_avatar(),
            '<img class="initial-avatar" src="http://django-initial-avatars.py/avatars/963f42f411a171630625f6163ef581c3/150x150_circle.png" width="150" height="150"/>'
        )
        self.assertIn(
            self.genB.get_avatar(),
            [
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;r=g&amp;d=mm" width="150" height="150"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;d=mm&amp;r=g" width="150" height="150"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=150&amp;d=mm" width="150" height="150"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=150" width="150" height="150"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=150&amp;r=g" width="150" height="150"/>',
                '<img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=150" width="150" height="150"/>'
            ]
        )
        self.assertTrue(default_storage.exists(self.genA.path()))

    def test_last_modified(self):
        self.assertIsInstance(
            self.genA.last_modification(),
            datetime
        )
        self.assertIsInstance(
            self.genB.last_modification(),
            datetime
        )

    def test_template_tags(self):
        renderedA = self.TEMPLATE.render(Context({'user': self.userA}))
        renderedB = self.TEMPLATE.render(Context({'user': self.userB}))
        renderedAnon = self.TEMPLATE.render(Context({'user': AnonymousUser()}))

        self.assertEqual(
            renderedA,
            u' <img class="initial-avatar" src="http://django-initial-avatars.py/avatars/963f42f411a171630625f6163ef581c3/150x150_circle.png" width="150" height="150"/>'
        )
        self.assertIn(
            renderedB,
            [
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;r=g&amp;d=mm" width="150" height="150"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?s=150&amp;d=mm&amp;r=g" width="150" height="150"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;s=150&amp;d=mm" width="150" height="150"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?r=g&amp;d=mm&amp;s=150" width="150" height="150"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;s=150&amp;r=g" width="150" height="150"/>',
                u' <img class="gravatar" src="https://secure.gravatar.com/avatar/c0ccdd53794779bcc07fcae7b79c4d80.jpg?d=mm&amp;r=g&amp;s=150" width="150" height="150"/>',
            ]
        )
        self.assertEqual(
            renderedAnon,
            u' <img src="" width="150" height="150"/>'
        )

    def test_non_default_template_tags(self):
        TEMPLATE = Template("{% load initialavatar %} {% get_initial_avatar user 200 'square' %}")
        renderedA = TEMPLATE.render(Context({'user': self.userA}))

        self.assertEqual(
            renderedA,
            u' <img class="initial-avatar" src="http://django-initial-avatars.py/avatars/963f42f411a171630625f6163ef581c3/200x200_square.jpg" width="200" height="200"/>'
        )

    def test_view(self):
        responseA = self.client.get('/1/150/')
        responseB = self.client.get('/2/150/')
        responseAnon = self.client.get('/3/150/')

        self.assertEqual(
            responseA.status_code,
            302
        )
        self.assertEqual(
            responseB.status_code,
            302
        )
        self.assertEqual(
            responseAnon.status_code,
            404
        )


class TestAvatarGeneratorBadSettings(TestCase):

    def setUp(self):
        self.userA = User.objects.create_user(
            username='JAB',
            email='admin@axiome.io',
            password='top_secret'
        )

    def test_exception(self):
        self.assertRaises(
            AvatarShapeException,
            AvatarGenerator, self.userA, size=150, shape='triangle'
        )
