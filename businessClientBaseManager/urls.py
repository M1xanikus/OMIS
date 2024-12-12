from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('clients/', views.clients_list, name='clients_list'),
    path('client/<int:id>/', views.client_details, name='client_details'),
    path('messages_history/', views.messages_history, name='messages_history'),
    path('campaigns/', views.campaigns_list, name='campaigns_list'),

    path('messages/<int:client_id>/', views.messages_history, name='messages_history'),

    path('campaigns/clients_select/', views.clients_select, name='clients_select'),
    path('campaigns/message_create/', views.campaign_message_create, name='campaign_message_create'),

    path('tasks/', views.tasks_list, name='tasks_list'),
    path('campaign/<int:id>/', views.campaign_details, name='campaign_details'),
]