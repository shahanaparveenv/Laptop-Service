from django.contrib.auth.forms import UserCreationForm
from django import forms

from laptopservice_app.models import Login, Customer, Seller, Feedback, SellerFeedback, Product


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2', )


class CustomerRegister(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=('user',)

class SellerRegister(forms.ModelForm):
    class Meta:
        model=Seller
        fields=('__all__')
        exclude=('user',)
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('feedback',)

class SellerFeedbackForm(forms.ModelForm):
    class Meta:
        model=SellerFeedback
        fields=('feedback',)

class ReplyFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('reply',)



class ReplySellerFeedbackForm(forms.ModelForm):
    class Meta:
        model = SellerFeedback
        fields = ('feedback', 'reply',)


class ProductSellerForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('seller',)

