from django.contrib.auth.forms import UserCreationForm


# Create your models here.
class CustomerUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
