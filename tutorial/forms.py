from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as lazy

class TodoListItemForm(forms.Form):
    text = forms.CharField(required=True, max_length=500)
    complete = forms.BooleanField(required=False, initial=False)
    due_date = forms.DateField(required=True)



