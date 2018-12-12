from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from CreditCards.forms.credit_cards import *
from CreditCards.models import CreditCard


class CreditCardsListView(LoginRequiredMixin, ListView):
    login_url = 'CreditCards:login'
    model = CreditCard
    context_object_name = 'cards_data'
    template_name = 'CreditCards/cards.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(CreditCardsListView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Cards',
            'user_permissions': self.request.user.get_all_permissions,
        })
        return context


class CreditCardsDetailView(LoginRequiredMixin, DetailView):
    login_url = 'CreditCards:login'
    model = CreditCard
    template_name = 'CreditCards/card_detail.html'
    context_object_name = 'card_data'

    def get_object(self, queryset=None):
        return get_object_or_404(CreditCard, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreditCardsDetailView, self).get_context_data(**kwargs)
        card = context.get('card_data')
        context.update({
            'card': card,
            'title': 'Card Details',
            'user_permissions': self.request.user.get_all_permissions,
        })
        return context


class CreateCreditCardView(LoginRequiredMixin, CreateView):
    model = CreditCard
    login_url = 'CreditCards:login'
    form_class = AddCreditCardForm
    template_name = 'CreditCards/add.html'
    success_url = reverse_lazy('CreditCards:all_cards')

    def post(self, request, *args, **kwargs):
        form = AddCreditCardForm(request.POST)
        if form.is_valid():
            cc_object = form.save(commit=False)
            cc_object.owner_id = request.user.id
            cc_object.save()

        return redirect('CreditCards:all_cards')


class UpdateCreditCardView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'CreditCards:login'
    model = CreditCard
    form_class = UpdateCreditCardForm
    template_name = 'CreditCards/edit.html'
    success_url = reverse_lazy('CreditCards:all_cards')

    def has_permission(self):
        pk = self.kwargs['pk']

        user_id = self.request.user.id
        cc_object = CreditCard.objects.get(pk=pk)

        if cc_object and cc_object.owner_id == user_id:
            return True
        else:
            self.raise_exception = True
            return False

    def get_object(self, queryset=None):
        return get_object_or_404(CreditCard, **{'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super(UpdateCreditCardView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Edit College',
        })
        return context


class DeleteCreditCardView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'CreditCard:login'
    model = CreditCard
    template_name = 'CreditCards/delete.html'
    success_url = reverse_lazy('CreditCards:all_cards')

    def has_permission(self):
        pk = self.kwargs['pk']

        user_id = self.request.user.id
        cc_object = CreditCard.objects.get(pk=pk)

        if cc_object and cc_object.owner_id == user_id:
            return True
        else:
            self.raise_exception = True
            return False
