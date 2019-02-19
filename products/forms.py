from django import forms
from .models import Product
import re

class ProductForm(forms.ModelForm):
    title       = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Title",
                "class" : "title one",
                "id" : "title",
            }
        )
    )

    description = forms.CharField(
        label = '',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Description",
                "class" : "product-description",
                "id" : "description",
                "rows" : 10,
                "cols" : 30
            }
        )
    )

    price       = forms.DecimalField(initial = 0.0, label = '')

    email       = forms.EmailField(
        label = '',
        widget=forms.EmailInput(
            attrs={
                "class" : "email",
                "id" : "email",
                "placeholder" : "E-mail"
            }
        )
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'email',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not (regex.search(title) == None): 
            raise forms.ValidationError("Special symbol is not allowed")
        return title


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not ((email.endswith("com")) 
        and not (email.endswith("br")) 
        and not (email.endswith("ca"))):
            raise forms.ValidationError("Invalid E-mail")
        return email


class RawProductForm(forms.Form):
    title       = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Title"
            }
        )
    )
    description = forms.CharField(
        required=False,
        label = '',
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "id" : "my-id-for-textarea",
                "rows" : 10,
                "columns" : 30,
                "placeholder" : "Description"
            }
        )
    )
    price       = forms.DecimalField(initial=0.0, label = '')   


