from django import forms
from .models import Product

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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "title" in title.lower():
            raise forms.ValidationError("This is not a valid title")
        return title


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid title")
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


