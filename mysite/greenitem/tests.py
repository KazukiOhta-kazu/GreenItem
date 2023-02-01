from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Wallet


User = get_user_model()


class CreateWalletAfterSignupTests(TestCase):
    def setUp(self):
        url = reverse('account_signup')
        data = {
            'email': 'example@example.com',
            'password1': 'Pass0101',
            'password2': 'Pass0101'
        }
        self.client.post(url, data)

    def test_wallet_creation(self):
        '''
        ユーザーが作成されると、Walletモデルのインスタンスが作成されるか
        '''
        self.assertIs(Wallet.objects.exists(), True)
        self.assertEqual(User.objects.first().id, Wallet.objects.first().user_id)
