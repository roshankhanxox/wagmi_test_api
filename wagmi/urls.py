from django.urls import path
from .views import wagmi_view

urlpatterns = [
    path('wagmi', wagmi_view),
]
