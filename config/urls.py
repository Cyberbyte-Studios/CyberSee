# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework import routers

from cybersee.base.views import HomeView, DashboardView
from cybersee.metrics.views import MetricViewSet, ReadingViewSet
from cybersee.servers.views import ServerViewSet, GameViewSet, ServerLogViewSet, ServerView, NewServerView, EditServerView
from cybersee.payments.views import PlanViewSet

router = routers.DefaultRouter()
router.register(r'metrics', MetricViewSet)
router.register(r'readings', ReadingViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'server-logs', ServerLogViewSet)
router.register(r'games', GameViewSet)
router.register(r'plans', PlanViewSet)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^table/', include('table.urls')),
    url(r'^server/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$', ServerView.as_view(), name='server-detail'),
    url(r'^server/new/$', NewServerView.as_view(), name='add-server'),
    url(r'^server/edit/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$', EditServerView.as_view(), name='edit-server'),


    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('cybersee.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^api/v1/', include(router.urls, namespace='v1')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
