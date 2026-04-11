from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Operator, Transaction, User


class RupayApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='student1',
            name='Student One',
            card_number='CARD-001',
        )
        self.operator = Operator.objects.create(username='operator1', name='Operator One')

    def test_online_recharge_creates_transaction(self):
        response = self.client.post(
            reverse('recharge-online'),
            data={'card_number': self.user.card_number, 'amount': '15.00'},
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Transaction.objects.filter(user=self.user).count(), 1)
        self.assertEqual(Decimal(str(response.json()['balance'])), Decimal('15.00'))

    def test_operator_recharge_rejects_online_method(self):
        response = self.client.post(
            reverse('recharge-operator'),
            data={
                'card_number': self.user.card_number,
                'operator_id': str(self.operator.id),
                'amount': '10.00',
                'recharge_method': 'ONLINE',
            },
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('recharge_method', response.json())

    def test_turnstile_denies_without_balance(self):
        response = self.client.post(
            reverse('turnstile-validate'),
            data={'card_number': self.user.card_number, 'meal_price': '5.00'},
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertFalse(payload['access_granted'])
        self.assertEqual(Decimal(str(payload['balance'])), Decimal('0.00'))

    def test_turnstile_debits_when_balance_is_enough(self):
        Transaction.objects.create(
            user=self.user,
            type=Transaction.TransactionType.RECHARGE,
            amount=Decimal('20.00'),
            recharge_method=Transaction.MethodType.ONLINE,
        )

        response = self.client.post(
            reverse('turnstile-validate'),
            data={'card_number': self.user.card_number, 'meal_price': '5.00'},
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload['access_granted'])
        self.assertEqual(Decimal(str(payload['balance'])), Decimal('15.00'))
        self.assertEqual(Transaction.objects.filter(user=self.user).count(), 2)
