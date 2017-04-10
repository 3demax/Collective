import django
from django.conf.urls import include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


from post.views import *
from people.views import *



# handler404 = custom404

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^login/$', django.contrib.auth.login,
        {'template_name': 'login.html.django'}, name="login"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^logout/$', django.contrib.auth.logout, name="logout"),

    url(r'^user/(?P<username>[\w]+)/$', AuthorView.as_view(), name="user_posts"),

    url(r'^', include('post.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
