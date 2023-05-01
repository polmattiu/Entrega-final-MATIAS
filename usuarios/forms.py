from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import  InfoExtra


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
        
        





class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)
    descripcion = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'rows': 5}))
    
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar' , 'descripcion']

    def save(self, commit=True):
        
        user = super().save(commit=commit)

        
        info_extra, created = InfoExtra.objects.get_or_create(user=user)

        
        info_extra.descripcion = self.cleaned_data['descripcion']
        if commit:
            info_extra.save()

        return user
