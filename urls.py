import django
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
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
    url(r'^login/$', auth_views.LoginView.as_view(),
        {'template_name': 'login.html.django'}, name="login"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),

    url(r'^', include('post.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
