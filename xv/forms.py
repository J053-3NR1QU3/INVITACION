from django.forms import ModelForm
from xv.models import Invitado

class InvitadoForm(ModelForm):
    class Meta:
        model = Invitado
        fields = ['nombre', 'relacion', 'asistentes','dedicatoria']
