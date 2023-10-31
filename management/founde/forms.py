from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Username',
    }))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter First Name',
    }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Last Name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Email',
    }))
    password1 = forms.CharField(max_length=40, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Password',
        'autocomplete': 'off',
    }))
    password2 = forms.CharField(max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'autocomplete': 'on',
    }))

    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Add Photo (Optional)',
    }))

    is_lostuser = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))

    class Meta:
        model = MyCustomUsers
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo']


class Login_Form(forms.Form):
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control floating',
            'placeholder': 'Enter Password',
            'required': 'true',
        })
    )


class SingForm(forms.ModelForm):
    class Meta:
        model = Sing
        fields = ['name', 'fathername', 'Gfathername', 'ID', 'email', 'password', 'cofirmpassword', 'choosefile', 'phone_number']



class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ( 'sic', 'location', 'date', 'pd', 'image')
        widgets = {
            
            'sic': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pd': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem1
        fields = ( 'sic', 'location', 'date', 'pd', 'lost_img', 'reward')
        widgets = {
    
            'sic': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pd': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'reward': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PostNewsForm(forms.ModelForm):
    class Meta:
        model = PostNews
        fields = ['title', 'addressed_to', 'description']
        widgets = {
            
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'addressed_to': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['sing', 'name', 'description']


from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'selling_item': forms.TextInput(attrs={'class': 'form-control'}),
            'bid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'bid_date': forms.DateInput(attrs={'class': 'form-control', 'type' : 'date'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }




class BidForm(forms.Form):
    newprice = forms.IntegerField(label='Enter price')

class BidUpdateForm(forms.Form):
    bid_id = forms.CharField(widget=forms.HiddenInput())
    bid_amount = forms.DecimalField()   

