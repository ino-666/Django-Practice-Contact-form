from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
 
class AccountCreateView(generic.CreateView):
    Model = User
    form_class = UserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create"
 
class AccountCreateViewUsingMyForm(generic.CreateView):
    Model = User
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create_with_form"
