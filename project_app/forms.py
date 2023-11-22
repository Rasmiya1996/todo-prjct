from django import forms

from project_app.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'