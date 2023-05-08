from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200, label="Task Title", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    description = forms.CharField(widget=forms.Textarea, label="Task Description", required=False)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre del Proyecto", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    description = forms.CharField(label="Descripcion del Proyecto", required=False, widget=forms.Textarea(attrs={'class' : 'form-control'}))
    
    #done = forms.BooleanField(label="Terminado", required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))

    

    
