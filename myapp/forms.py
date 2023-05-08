from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description", required=False)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, label="Project Name")
