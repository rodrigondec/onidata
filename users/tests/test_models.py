from django.test import TestCase

from users.factories import UserFactory, User


class UserTestCase(TestCase):
    def test_create(self):
        UserFactory()
        self.assertEqual(User.objects.count(), 1)

    def test_update(self):
        user = UserFactory(first_name='original')
        self.assertEqual(User.objects.first().first_name, 'original')

        user.first_name = 'modificado'
        user.save()
        self.assertEqual(User.objects.first().first_name, 'modificado')

    def test_delete(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        user.delete()
        self.assertEqual(User.objects.count(), 0)
