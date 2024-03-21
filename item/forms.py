from django import forms

from .models import Item

INPUT_CLASSES = 'py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets = {
                'category': forms.Select(attrs={
                    'class': INPUT_CLASSES
                }),
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES
                })
            }   
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES
                })
            }   