from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import User, UserAddress
from django.core import validators
import random


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label="رمز", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار رمز", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone_number"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['phone_number', "password", "email", "is_active", "is_admin"]


def phone_start_with_0(value):
    if value[0] != '0':
        raise ValidationError('phone should start with 0!')


class SignIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': "Your username number",
                                                             'id': "username",
                                                             'required': "required",
                                                             'data-validation-required-message': "Please enter your phone number",
                                                             'autocomplete': "off"

                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': "password1",
                                                                 'placeholder': "Your password",
                                                                 'required': "required",
                                                                 'data-validation-required-message': "Please enter your password",
                                                                 'autocomplete': "off"

                                                                 }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 40:
            raise ValidationError(
                '%(value)s is invalid',
                params={'value': f'{username}'},
                code='invalid-username'

            )

        return username


class SetInfo(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': "email",
                                                           'placeholder': "Your email",
                                                           'required': "required",
                                                           'data-validation-required-message': "Please enter your email",
                                                           'autocomplete': "off"

                                                           }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': "password1",
                                                                  'placeholder': "Your password",
                                                                  'required': "required",
                                                                  'data-validation-required-message': "Please enter your password",
                                                                  'autocomplete': "off"

                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': "password2",
                                                                  'placeholder': "Your password",
                                                                  'required': "required",
                                                                  'data-validation-required-message': "Please enter your password",
                                                                  'autocomplete': "off"

                                                                  }))

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('your entry passwords must be same!', code='dont_same_pass')


class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': "Your phone number",
                                                          'autocomplete': "off",
                                                          'id': "phone",
                                                          'required': "required"}),
                            validators=[validators.MaxLengthValidator(11)])

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) > 11:
            raise ValidationError(
                '%(value)s is invalid',
                params={'value': f'{phone}'},
                code='invalid-phone'
            )
        if User.objects.filter(phone_number=phone):
            raise ValidationError(
                '%(value)s is exists',
                params={'value': f'{phone}'},
                code='exists-phone'
            )
        return phone


class CheckOTP(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': "Enter OTP codes",
                                                         'id': "code",
                                                         'required': "required",
                                                                  'autocomplete': "off"
                                                         }),
                           validators=[validators.MaxLengthValidator(4)])


class UpdateUserForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=100,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'autocomplete': "off"
                                                                 }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'autocomplete': "off"
                                                           }))
    full_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'autocomplete': "off"
                                                              }))

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'full_name']


class ForgetPasswordForm(forms.Form):
    phone_number = forms.CharField(max_length=100,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'autocomplete': "off"}))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'id': "old_password",
                                                                     'placeholder': "old password",
                                                                     'required': "required",
                                                                     'data-validation-required-message': "Please enter your old password",
                                                                     'autocomplete': "off"
                                                                     }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': "password1",
                                                                  'placeholder': "Enter your new password",
                                                                  'required': "required",
                                                                  'data-validation-required-message': "Please enter your password",
                                                                  'autocomplete': "off"
                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': "password2",
                                                                  'placeholder': "Repeat your new password",
                                                                  'required': "required",
                                                                  'data-validation-required-message': "Please enter your password",
                                                                  'autocomplete': "off"
                                                                  }))

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('your entry passwords must be same!', code='dont_same_pass')


class AddAddress(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = UserAddress
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'zip_code']
