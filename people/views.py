from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.decorators import method_decorator

class LoginView(TemplateView):
    template_name = 'login.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context


class RegisterView(TemplateView):
    template_name = 'register.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['form'] = UserCreationForm()
        return context

