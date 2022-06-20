from django.urls import path
from django.views.generic import TemplateView
from .views import (
    EventsListView, EventDetailView, EventCreateView, EventDeleteView, DashboardView, VideoView
)

app_name = "customer-portal"
urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),

    path('event/', EventsListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('event/add/', EventCreateView.as_view(), name='event-add'),
    path('video/',  VideoView.as_view(), name='view-video'),

]
