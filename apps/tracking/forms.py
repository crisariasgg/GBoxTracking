from django import forms


class TrackingForm(forms.Form):
	tracking_number = forms.CharField(max_length=100 , 
		widget=forms.TextInput(
		attrs={"placeholder":"Ingresa tu número de tracking","class": "form-control"}
	))