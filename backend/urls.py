from django.urls import path
from .views import CorePrinciplesView, PropositionsView

urlpatterns = [
    path('core-principles/', CorePrinciplesView.as_view(), name='core-principles'),
    path('propositions/', PropositionsView.as_view(), name='propositions'),
]
