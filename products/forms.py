from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price', 
            'summary'
        ]


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


