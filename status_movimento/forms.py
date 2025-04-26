from django import forms
from .models import StatusMovimento
from django.core.exceptions import ValidationError


class StatusMovimentoForm(forms.ModelForm):
    class Meta:
        model = StatusMovimento
        fields = ['tipo_status']
        widgets = {
            'tipo_status': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        tipo_status = cleaned_data.get('tipo_status')

        if tipo_status:
            if StatusMovimento.objects.filter(
                tipo_status=tipo_status
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O tipo do status já está cadastrada no sistema.'
                )

        return cleaned_data
