from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import OrderPosition
from .models import UserProfile, Recipe, RecipeList


class UserInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['rezept_bezeichnung']


class RecipeListForm(forms.ModelForm):
    class Meta:
        model = RecipeList
        exclude = ['recipe']


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderPosition
        fields = ['rezept', "menge", "als_teig"]




# class RenewBookForm(forms.Form):
#     """
#     Form for a librarian to renew books.
#     """
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
#
#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#
#         #Check date is not in past.
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#         #Check date is in range librarian allowed to change (+4 weeks)
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         # Remember to always return the cleaned data.
#         return data
