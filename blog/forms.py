from django import forms

class ContactForm(forms.Form):
    nama_lengkap    = forms.CharField(
        label='Nama Lengkap',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nama Lengkap Anda',
            }
        )
    )
    jenis_kelamin   = forms.ChoiceField(
        choices= [
            ('P', 'Pria'),
            ('W', 'Wanita'),
        ],
        widget= forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
    )
    tanggal_lahir   = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1945,2021),
            attrs={
                'class':'form-control col-sm-2',
            }
        )
    )
    email           = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email anda',
            }
        ),
    )
    alamat          = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
            }
        )
    )
    agree           = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input',
            }
        )
    )