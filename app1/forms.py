from django import forms

class LikeForm(forms.Form):
    tutor_id = forms.IntegerField()