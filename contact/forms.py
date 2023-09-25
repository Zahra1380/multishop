from django import forms


class ContactForm(forms.Form):
    neme = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'id': "name",
        'placeholder': "Your Name",
        'required': "required",
        'data-validation-required-message': "Please enter your name",
        'autocomplete': "off"

    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'id': "name",
        'placeholder': "Your email",
        'required': "required",
        'data-validation-required-message': "Please enter your email",
        'autocomplete': "off"

    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'id': "name",
        'placeholder': "Your subject",
        'required': "required",
        'data-validation-required-message': "Please enter your subject",
        'autocomplete': "off"

    }))
    massage = forms.CharField(widget=forms.Textarea(attrs={
        'type': "text",
        'class': "form-control",
        'id': "name",
        'placeholder': "Your massage",
        'required': "required",
        'data-validation-required-message': "Please enter your massage",
        'autocomplete': "off"

    }))
