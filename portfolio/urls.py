from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),

    path('projects/', views.project_list, name='projects'),  # ✅ Corrected name
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit_project'),

    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),

    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


def health_check(request):
    return JsonResponse({"status": "ok"})