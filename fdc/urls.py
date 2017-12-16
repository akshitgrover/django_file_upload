from django.conf.urls import include, url
from django.contrib import admin
from uploads import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fdc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/',views.upload),
    url(r'^home/',views.home)
]
