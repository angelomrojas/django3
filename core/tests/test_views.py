from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

from core.forms import ContatoForm
from model_mommy import mommy

class IndexViewTestCase(TestCase):

    def setUp(self):

        self.dados = {
            'nome' : 'Angelo',
            'email' : 'angelo@gmail.com',
            'assunto' : 'Assunto',
            'mensagem' : 'Minha MSG'
            }
        
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Angelo'
        }

        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
