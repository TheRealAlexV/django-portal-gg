from django import forms
from django.utils.translation import gettext_lazy as _

from allauth.account.adapter import get_adapter
from allauth.account.forms import BaseSignupForm, SetPasswordField
from allauth.account.forms import ResetPasswordForm as AllAuthResetPasswordForm
from allauth.account.models import EmailAddress
from allauth.account.utils import setup_user_email

from allauth.socialaccount.forms import SignupForm

from .utils import social_user_display_name


class EmailUserSignupForm(BaseSignupForm):
    display_name = forms.CharField(
        label=_('Display name'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Display name')}))
    password1 = SetPasswordField(
        label=_('Password'), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If you want to remove placeholder
        # self.fields['email'].widget.attrs.pop('placeholder')
        # self.fields['password1'].widget.attrs.pop('placeholder')

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)

        user.display_name = self.cleaned_data['display_name']
        user.save()

        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class SocialUserSignupForm(SignupForm):
    password1 = SetPasswordField(
        label=_('Password'),
        required=True,
        help_text='Set a password you fuckin dunce.')
    display_name = forms.CharField(
        label=_('Display name'),
        max_length=100,
        required=True)

    def __init__(self, *args, **kwargs):
        super(SocialUserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].initial = self.sociallogin.user.email

        if self.sociallogin.user.email:
            self.fields['email'].widget.attrs['readonly'] = True

        self.fields['display_name'].initial = social_user_display_name(self.sociallogin.user)

    def save(self, request):
        # Check if user submitted different email we got from social network (fuckhead user)
        if self.sociallogin.user.email and self.sociallogin.user.email != self.cleaned_data.get('email'):
            self.cleaned_data['email'] = self.sociallogin.user.email

        user = super(SocialUserSignupForm, self).save(request)
        user.display_name = self.cleaned_data['display_name']
        user.save()


class ResetPasswordForm(AllAuthResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        # Check if user reset with unverified email
        mails = EmailAddress.objects.filter(email__iexact=email, verified=False)
        if mails.exists():
            raise forms.ValidationError(_('The e-mail address is not assigned to any user account'))

        return super(ResetPasswordForm, self).clean_email()
