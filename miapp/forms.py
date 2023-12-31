from django import forms
from django.core import validators


class form_con_class(forms.Form): #forms.Form ES OTRA CLASE DE LA QUE VAMOS A HEREDAR EL HTML PARA ESTA CLASE
    id=forms.IntegerField(
        label="ID",
        required=True #CON ESTO LE INDICO QUE NO LO PUEDEN DEJAR EN BLANCO
    )
    title= forms.CharField(#PUEDO BUSCAR MAS formfields en LA PAGINA DE django
        label="Title"
    )

    content= forms.CharField(
        label="Content"
        
    )
    
    street= forms.CharField(
        label="Street"
    )
    
    house_number= forms.IntegerField(
        label="House Number"
    )
#ESTO ES PORQUE LE PUSIMOS DIRECTAMENTE TEXTAREA EN VEZ DE CharField  Y VOTABA ERROR 
    house_description= forms.CharField(
        label="House Description",
        max_length=100,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': " add any description of the house if you think its necesary  ",
            'class':'descripcion-de-la-casa'}
    )
    )

    public_options=[
        (1,'Yes'),
        (0,'No')
    ]
    public=forms.TypedChoiceField(
        label="Publico?",
        choices=public_options
    )


   
    