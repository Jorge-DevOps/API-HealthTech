from django import forms

class HorarioMedico(forms.Form):
    idHorario = forms.CharField(label='Id', max_length=80)
    horaInicio = forms.DateField(label='Hora Inicio')
    horaFin = forms.DateField(label='Hora Fin')

    def __str__(self):
        return self.horaFin
