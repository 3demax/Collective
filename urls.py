from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from post.views import *

from django.conf import settings
from django.conf.urls.static import static

# handler404 = custom404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drwc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = urlpatterns + patterns('',
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html.django'}, name="login"),
    # url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/register/'}, name="logout"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add/$', AddView.as_view(), name="add_post"),
    url(r'^edit/(?P<pk>\d+)/$', EditView.as_view(), name="edit_post"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)