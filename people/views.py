from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse


class RegistrationView(CreateView):
    template_name = 'register.html.django'
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')
