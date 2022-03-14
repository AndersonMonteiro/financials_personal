from django.urls import path
from api.views import (
    access_group_participants_views, access_groups_views, accounts_views, address_views,
    auxiliar_views, budgets_views, cards_views, comments_views, goals_views, movements_views, profiles_views,
    invoice_views
)

urlpatterns = [
    path('currencies', auxiliar_views.MoedaList.as_view()),
    path('movement-types', auxiliar_views.TipoMovimentacaoList.as_view()),
    path('methods-payments', auxiliar_views.FormaPagamentoList.as_view()),
    path('movement-status', auxiliar_views.StatusMovimentacaoList.as_view()),
    path('categories', auxiliar_views.CategoriaList.as_view()),
    path('account-types', auxiliar_views.TipoContaList.as_view()),
    path('financial-institutions', auxiliar_views.InstituicaoFinanceiraList.as_view()),
    path('brands', auxiliar_views.BandeiraList.as_view()),
    path('movment-priorities', auxiliar_views.PrioridadeMovimentacaoList.as_view()),
    path('addresses', address_views.AddressCreateListView.as_view()),
    path('addresses/<int:pk>', address_views.AddressRetrievelUpdateView.as_view()),
    path('accounts', accounts_views.AccountCreateList.as_view()),
    path('accounts/<int:pk>', accounts_views.AccountUpdateRetrieve.as_view()),
    path('movements', movements_views.MovementCreateList.as_view()),
    path('movements/<str:pk>', movements_views.MovementUpdateRetrieve.as_view()),
    path('profiles', profiles_views.ProfileCreateListView.as_view()),
    path('profiles/<int:pk>', profiles_views.ProfileRetrieveUpdateView.as_view()),
    path('comments', comments_views.CommentCreateList.as_view()),
    path('comments/<int:pk>', comments_views.CommentUpdateRetrieve.as_view()),
    path('cards', cards_views.CardCreateList.as_view()),
    path('cards/<int:pk>', cards_views.CardUpdateRetrieve.as_view()),
    path('goals', goals_views.GoalCreateListView.as_view()),
    path('goals/<int:pk>', goals_views.GoalUpdateView.as_view()),
    path('budgets', budgets_views.BudgetCreateListView.as_view()),
    path('orcamentos/<int:pk>', budgets_views.BudgetUpdateView.as_view()),
    path('sheet_sync', movements_views.MovementSyncSheet.as_view()),
    path('sheet-movements', movements_views.MovementSheetList.as_view()),
    path('access-group-types', auxiliar_views.TipoGrupoAcessoList.as_view()),
    path('access-group', access_groups_views.AccessGroupCreateList.as_view()),
    path('access-group/<int:pk>', access_groups_views.AccessGroupUpdate.as_view()),
    path('access-group-participant', access_group_participants_views.AccessGroupParticipantViewsCreateList.as_view()),
    path('access-group-participant/<int:pk>', access_group_participants_views.AccessGroupParticipantViewsUpdate.as_view()),
    path('invoices', invoice_views.InvoiceCreateList.as_view()),
    path('invoices/<int:pk>', invoice_views.InvoiceUpdateRetrieve.as_view()),
]
