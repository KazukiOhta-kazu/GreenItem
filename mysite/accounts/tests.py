from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('account_signup')
        data = {
            'email': 'example@example.com',
            'password1': 'Pass0101',
            'password2': 'Pass0101'
        }
        self.response = self.client.post(url, data)

    def test_user_creation(self):
        '''
        ユーザーが作成できているか
        '''
        self.assertIs(User.objects.exists(), True)

    def test_redirection(self):
        '''
        ユーザーを作成すると、メールアドレスの確認ページにリダイレクトされているか
        '''
        redirect_url = reverse('account_email_verification_sent')
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, redirect_url)
