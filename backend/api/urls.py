from django.urls import path
from .views import CorePrinciplesView, FundamentalTenetsView, PropositionsView, TheoreticalFoundationsView, PracticalApplicationsView

urlpatterns = [
    path('core-principles/', CorePrinciplesView.as_view(), name='core-principles'),
    path('fundamental-tenets/', FundamentalTenetsView.as_view(), name='fundamental-tenets'),
    path('propositions/', PropositionsView.as_view(), name='propositions'),
    path('theoretical-foundations/', TheoreticalFoundationsView.as_view(), name='theoretical-foundations'),
    path('practical-applications/', PracticalApplicationsView.as_view(), name='practical-applications'),
]
