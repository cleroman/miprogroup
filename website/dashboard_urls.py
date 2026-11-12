from django.urls import path
from . import dashboard_views

urlpatterns = [
    path('', dashboard_views.DashboardIndexView.as_view(), name='dashboard_index'),
    
    # Parametres
    path('parametres/', dashboard_views.SettingsUpdateView.as_view(), name='dashboard_settings'),
    
    # Services
    path('services/', dashboard_views.ServiceListView.as_view(), name='dashboard_services'),
    path('services/ajouter/', dashboard_views.ServiceCreateView.as_view(), name='dashboard_service_add'),
    path('services/modifier/<int:pk>/', dashboard_views.ServiceUpdateView.as_view(), name='dashboard_service_edit'),
    path('services/supprimer/<int:pk>/', dashboard_views.ServiceDeleteView.as_view(), name='dashboard_service_delete'),
    
    # Partenaires
    path('partenaires/', dashboard_views.PartnerListView.as_view(), name='dashboard_partners'),
    path('partenaires/ajouter/', dashboard_views.PartnerCreateView.as_view(), name='dashboard_partner_add'),
    path('partenaires/modifier/<int:pk>/', dashboard_views.PartnerUpdateView.as_view(), name='dashboard_partner_edit'),
    path('partenaires/supprimer/<int:pk>/', dashboard_views.PartnerDeleteView.as_view(), name='dashboard_partner_delete'),
    
    # Demandes
    path('demandes/', dashboard_views.RequestListView.as_view(), name='dashboard_requests'),

    # Equipe
    path('equipe/', dashboard_views.TeamListView.as_view(), name='dashboard_team'),
    path('equipe/ajouter/', dashboard_views.TeamCreateView.as_view(), name='dashboard_team_add'),
    path('equipe/modifier/<int:pk>/', dashboard_views.TeamUpdateView.as_view(), name='dashboard_team_edit'),
    path('equipe/supprimer/<int:pk>/', dashboard_views.TeamDeleteView.as_view(), name='dashboard_team_delete'),
]
