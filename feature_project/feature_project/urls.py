from django.urls import path
from feature.views import ProtectedDataView

urlpatterns = [
    path('api/data/', ProtectedDataView.as_view()),
]
