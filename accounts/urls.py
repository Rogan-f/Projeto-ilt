from django.urls import path
from accounts import views
urlpatterns = [
    path('accounts/signup', 
        views.AccountCreateView.as_view(),
        name="signup"
),
]

urlpatterns = [
    path('account/<int:pk>/edit',
        views.AccountUpdateView.as_view(),
        name="account_edit"
),
]
