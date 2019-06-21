from django.test import TestCase

from users.factories import UserFactory, User


class UserTestCase(TestCase):
    def test_create(self):
        UserFactory()
        self.assertEqual(User.objects.count(), 1)

    def test_update(self):
        user = UserFactory(email='original@email.com')
        self.assertEqual(User.objects.first().email, 'original@email.com')

        user.email = 'modificado@email.com'
        user.save()
        self.assertEqual(User.objects.first().email, 'modificado@email.com')

    def test_delete(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        user.delete()
        self.assertEqual(User.objects.count(), 0)
