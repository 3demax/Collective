from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from post.models import Post

class IndexView(TemplateView):
    template_name = 'index.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(is_published=True).order_by('-publish_date')[0:3]
        return context

    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class EditView(TemplateView):
    template_name = 'edit.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EditView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditView, self).dispatch(*args, **kwargs)

class AddView(TemplateView):
    template_name = 'add.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AddView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddView, self).dispatch(*args, **kwargs)