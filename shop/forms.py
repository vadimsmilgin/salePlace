from django import forms
from django.forms import TextInput, ModelChoiceField, FloatField, Textarea, FileInput

from shop.models import Item, Category


class CreationItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control',
                                                                                                  'required': True,
                                                                                                  'id': 'selectCat',
                                                                                                  'style': 'width: 79.5%;position: relative;left: 0.96em;'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                             'required': True,
                                                             'id': 'inputPrice'
                                                             }))
    #icon = forms.FileInput()

    class Meta:
        model = Item
        fields = ('name', 'icon', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'required': True,
                                     'placeholder': 'Название',
                                     'id': 'inputName'}),
            'icon': FileInput(attrs={'class': 'custom-file-input',
                                     'required': True,
                                     'id': 'customFile'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Описание',
                                           'id': 'inputTextarea',
                                           'rows': 3,
                                           'style': 'width: 79.5%;position: relative;left: 0.97em;'}),

                  }