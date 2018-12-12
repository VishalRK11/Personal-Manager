from django.urls import path
from CreditCards.views.auth import *
from CreditCards.views.credit_cards import *

app_name = 'CreditCards'

urlpatterns = [
    path('view/', CreditCardsListView.as_view(), name='all_cards'),
    path('<int:pk>/', CreditCardsDetailView.as_view(), name='card_details'),
    path('signup/', SignUpController.as_view(), name='signup'),
    path('login/', LoginController.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', CreateCreditCardView.as_view(), name='add_card'),
    path('<int:pk>/edit/', UpdateCreditCardView.as_view(), name='edit_card'),
    path('<int:pk>/delete/', DeleteCreditCardView.as_view(), name='delete_card'),
]
