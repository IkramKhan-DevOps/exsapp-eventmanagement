from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    AddonListView, AddonCreateView, AddonUpdateView, AddonDeleteView,
    EventTypeListView, EventTypeCreateView, EventTypeUpdateView, EventTypeDeleteView,
    VenueListView, VenueCreateView, VenueUpdateView, VenueDeleteView,
    EventListView, EventDetailView, EventUpdateView, EventDeleteView,
    PaymentVerificationEasyPaisa, DashboardView)

app_name = "admin-portal"
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('addon/', AddonListView.as_view(), name='addon-list-view'),
    path('addon/add/', AddonCreateView.as_view(), name='addon-create-view'),
    path('addon/<int:pk>/change/', AddonUpdateView.as_view(), name='addon-update-view'),
    path('addon/<int:pk>/delete/', AddonDeleteView.as_view(), name='addon-delete-view'),

    path('eventtype/', EventTypeListView.as_view(), name='eventtype-list-view'),
    path('eventtype/add/', EventTypeCreateView.as_view(), name='eventtype-create-view'),
    path('eventtype/<int:pk>/change/', EventTypeUpdateView.as_view(), name='eventtype-update-view'),
    path('eventtype/<int:pk>/delete/', EventTypeDeleteView.as_view(), name='eventtype-delete-view'),

    path('venue/', VenueListView.as_view(), name='venue-list-view'),
    path('venue/add/', VenueCreateView.as_view(), name='venue-create-view'),
    path('venue/<int:pk>/change/', VenueUpdateView.as_view(), name='venue-update-view'),
    path('venue/<int:pk>/delete/', VenueDeleteView.as_view(), name='venue-delete-view'),

    path('event/', EventListView.as_view(), name='event-list-view'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail-view'),
    path('event/<int:pk>/change/', EventUpdateView.as_view(), name='event-update-view'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete-view'),

    path(
        'payment/verification/easypaisa/',
        PaymentVerificationEasyPaisa.as_view(),
        name='payment-verification-easypaisa'
    )

]
