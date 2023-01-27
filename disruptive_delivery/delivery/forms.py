from django import forms
from datetime import *


class OrderOfferForm(forms.Form):

    price = forms.IntegerField(
        required=True,
        min_value=0,
        widget=forms.NumberInput(
            attrs={'type': 'number', 'class': 'form-control'}),
        label="Price (in cents)"
    )

    date = forms.DateField(
        required=True,
        initial= date.today() + timedelta(days=1),
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}),
        label="Date"
    )

    time = forms.TimeField(
        required=True,
        initial=datetime.now().time(),
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
        label="Time"
    )

class OrderOfferFormID(forms.Form):

    id = forms.ChoiceField(
        required=True,
        choices=(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Order ID"
    )
    price = forms.IntegerField(
        required=True,
        min_value=0,
        widget=forms.NumberInput(
            attrs={'type': 'number', 'class': 'form-control'}),
        label="Price (in cents)"
    )

    date = forms.DateField(
        required=True,
        initial= date.today() + timedelta(days=1),
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}),
        label="Date"
    )

    time = forms.TimeField(
        required=True,
        initial=datetime.now().time(),
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
        label="Time"
    )

class GetDeliveryForm(forms.Form):
    id = forms.IntegerField(
        required=True,
        min_value=0,
        widget=forms.NumberInput(
            attrs={'type': 'number', 'class': 'form-control'}),
        label="Delivery ID"
    )

class UpdateDeliveryForm(forms.Form):

    id = forms.ChoiceField(
        required=True,
        choices=(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Delivery ID"
    )

    status = forms.ChoiceField(
        required=True,
        choices=(
            ('TRN', 'Transit'),
            ('DEL', 'Delivered')
        ),
        widget=forms.Select(attrs={'class':'form-control', 'onchange':'showDT()'})
    )

    date = forms.DateField(
        required=False,
        initial= None,
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}),
        label="Date"
    )

    time = forms.TimeField(
        required=False,
        initial=None,
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
        label="Time"
    )

class UpdateDeliveryFormNoID(forms.Form):

    status = forms.ChoiceField(
        required=True,
        choices=(
            ('TRN', 'Transit'),
            ('DEL', 'Delivered')
        ),
        widget=forms.Select(attrs={'class':'form-control', 'onchange':'showDT()'})
    )

    date = forms.DateField(
        required=False,
        initial= None,
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}),
        label="Date"
    )

    time = forms.TimeField(
        required=False,
        initial=None,
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
        label="Time"
    )
class UploadLabelForm(forms.Form):
  
    id = forms.ChoiceField(
        required=True,
        choices=(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Order ID"
    )

    label = forms.FileField(
        required=True,
        label='Select a label', widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'})
    )

class UpLoadLabelFormNoID(forms.Form):

    label = forms.FileField(
        required=True,
        label='Select a label', widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'})
    )
    