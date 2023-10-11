from http.client import HTTPResponse
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password 
from django.contrib import messages

from django.contrib.auth import get_user_model

from polls.models import Question
User = get_user_model() 

from accounts.forms import AccountSignupForm 

class AccountCreateView(CreateView):
    model = User 
    template_name = 'registration/signup_form.html' 
    form_class = AccountSignupForm
    success_url = reverse_lazy('login') 
    success_message = 'Usuário criado com sucesso!'
    
    def form_valid(self, form): 
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(AccountCreateView, self).form_valid(form)

@login_required 
def sobre(request):return HTTPResponse("Este é um app de enquete!")

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_form.html'
    fields = ('first_name', 'email', 'imagem', ) # incluir os campos que deseja liberar a edição
    success_url = reverse_lazy('polls_all') # rota para redirecionar após a edição
    success_message = 'Perfil atualizado com sucesso!'
    def get_queryset(self): # método que altera o objeto recuperado pela view
        user_id = self.kwargs.get('pk') # recupera o argumento vindo na URL / rota
        user = self.request.user
        if user is None or not user.is_authenticated or user_id != user.id:
            return User.objects.none()

        return User.objects.filter(id=user.id) # apenas o usuário do perfil logado pode editar
    def form_valid(self, form): # executa quando os dados estiverem válidos
        messages.success(self.request, self.success_message)
        return super(AccountUpdateView, self).form_valid(form)
