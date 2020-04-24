from django import forms
from mainapp.models import SendContacts


class SendContactsForm(forms.ModelForm):
    class Meta:
        model = SendContacts
        fields = ['name', 'email', 'phone', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'steward_alex@yandex.ru'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '8 (999) 111 22 33'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Привет, хочу стать стюардом '
                                                                                       'в вашей дружной команде!'}),

        }
