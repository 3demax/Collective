from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.models import User

from post.models import Post, Category


class IndexView(TemplateView):
    template_name = 'post_list.html.django'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(is_published=True).order_by('-publish_date')[0:3]
        context['category_list'] = Category.objects.order_by('name')
        return context


class AddView(CreateView):
    template_name = 'add_post.html.django'
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
    template_name = 'add_post.html.django'
    model = Post
    fields = ['title', 'text', 'category']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditView, self).dispatch(*args, **kwargs)


class AuthorView(TemplateView):
    template_name = 'post_list.html.django'

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        username = self.kwargs.get('username', '')
        get_object_or_404(User, username=username)
        context['post_list'] = Post.objects.filter(is_published=True, author__username=username).order_by('-publish_date')[:3]
        context['category_list'] = Category.objects.order_by('name')
        context['author_username'] = username
        return context


class CategoryView(TemplateView):
    template_name = 'post_list.html.django'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id', '')
        get_object_or_404(Category, category__id=category_id)
        context['category_name'] = Category.objects.filter(category__id=category_id).first()
        context['post_list'] = Post.objects.filter(category__id=category_id).order_by('-publish_date')[:3]
        context['category_list'] = Category.objects.order_by('name')
        return context


class SearchView(ListView):
    template_name = 'post_list.html.django'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q', '')
        context['category_list'] = Category.objects.order_by('name')
        return context

    def get_queryset(self):
        search_term = self.request.GET.get('q', '')
        terms = search_term.split(' ')
        q = Q()
        for term in terms:
            q = (q |
                 Q(title__icontains=term) |
                 Q(text__icontains=term) |
                 Q(category__name__icontains=term)
            )
        return Post.objects.filter(q)