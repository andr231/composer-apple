from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#FORMS DACIL
class RegistroF(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
                    'usuario',
                    'nombre',
                    'apellido',
                    'email',
                    ]

        labels = {
                    'usuario':'Nombre de Usuario',
                    'nombre':'Nombre',
                    'apellido':'Apellidos',
                    'email':'Correo electronico',
                    }