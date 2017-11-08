from django.test import TestCase

from datetime import datetime

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Dieison Borges',
            cpf='12345678901',
            email='dieisoncomix@gmail.com',
            phone='41-995814222'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Dieison Borges', str(self.obj))