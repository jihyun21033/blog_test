from django import forms

class Dataform(forms.Form):
    info_id = forms.CharField(label = 'info_id' , max_length = 100)
    info_pw = forms.CharField(label = 'info_pw' , max_length = 100)