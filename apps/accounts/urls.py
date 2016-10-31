from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from audiencias_publicas.decorators import anonymous_required

urlpatterns = [
    url(r'^login/$', anonymous_required(auth_views.login), name='login'),
    url(r'^logout/$', login_required(auth_views.logout_then_login),
        name='logout'),
    url(r'^password_change/$', auth_views.password_change,
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset,
        name='password_reset'),
    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^social/', include('social.apps.django_app.urls',
        namespace=settings.SOCIAL_AUTH_URL_NAMESPACE)),
]
