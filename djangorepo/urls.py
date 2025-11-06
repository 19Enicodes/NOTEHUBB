from django.contrib import admin
from django.urls import path
from libraryrepo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard (protected page after login)
    path('dashboard/', views.create_view, name='dashboard'),

    # Optional: Home redirects to login
    path('', views.login_view, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
