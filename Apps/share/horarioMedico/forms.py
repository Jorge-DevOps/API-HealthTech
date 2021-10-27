from django import forms

class HorarioMedico(forms.Form):
    idHorario = forms.CharField(label='Id', max_length=80)
    horaInicio = forms.CharField(label='Hora Inicio', max_length=100)
    horaFin = forms.CharField(label='Hora Fin', max_length=100)

    def __str__(self):
        return self.horaFin
