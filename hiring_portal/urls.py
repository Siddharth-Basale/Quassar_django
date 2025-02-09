from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidate/', include('candidates.urls')),
    path('interviewer/', include('interviewers.urls')),
]