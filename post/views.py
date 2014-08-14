from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from post.models import Post, Category

class IndexView(TemplateView):
    template_name = 'index.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(is_published=True).order_by('-publish_date')[0:3]
        context['category_list'] = Category.objects.order_by('name')
        return context


class AddView(CreateView):
    template_name = 'post.html.django'
    model = Post
    fields = ['title', 'text', 'category']

    def form_valid(self, form):
        """
        Current user is the author of the post
        """
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(AddView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddView, self).dispatch(*args, **kwargs)


class EditView(UpdateView):
    template_name = 'post.html.django'
    model = Post
    fields = ['title', 'text', 'category']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditView, self).dispatch(*args, **kwargs)


class AuthorView(TemplateView):
    template_name = 'user.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorView, self).get_context_data(**kwargs)
        username = self.kwargs.get('username', '')
        get_object_or_404(User, username=username)
        context['post_list'] = Post.objects.filter(is_published=True, author__username=username).order_by('-publish_date')[0:3]
        context['category_list'] = Category.objects.order_by('name')
        return context


class CategoryView(TemplateView):
    template_name = 'category.html.django'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id', '')
        get_object_or_404(Category, category__id=category_id)
        context['category'] = Category.objects.filter(category__id=category_id).first()
        context['post_list'] = Post.objects.filter(category__id=category_id).order_by('-publish_date')[0:3]
        context['category_list'] = Category.objects.order_by('name')
        return context