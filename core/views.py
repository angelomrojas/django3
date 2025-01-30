from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Features
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        features_total = Features.objects.all()
        context['featuresLeft'] = features_total[:3]
        context['featuresRight'] = features_total[3:]
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super().form_invalid(form, *args, **kwargs)