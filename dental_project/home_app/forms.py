from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.core import validators

from . import models
from .models import Booking, Details_User, Details_Doctor, Update_Booking, Prescription, Review
from django import forms
from django.forms.widgets import DateInput
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import Patients
# class CustomDateInput(DateInput):
#     input_type = 'date'
#     def __init__(self, *args, **kwargs):
#         super(CustomDateInput, self).__init__(*args, **kwargs)
#         self.attrs['min'] = timezone.now().strftime('%Y-%m-%d')
#
# class MyForm(forms.Form):
#     my_date = forms.DateField(widget=CustomDateInput())

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self, *args, **kwargs):
        super(CustomDateInput, self).__init__(*args, **kwargs)
        today = timezone.now().strftime('%Y-%m-%d')
        # self.attrs['min'] = today
        self.attrs['max'] = today

class MForm(forms.Form):
    my_date = forms.DateField(widget=CustomDateInput())

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
#
#         widgets = {
#             'dob': CustomDateInput()
#         }
#         # widgets = {
#         #     'dob': forms.DateInput(attrs={'type': 'date'}),
#         # }
#
#     def clean_records(self):
#         records = self.cleaned_data['records']
#         if records and not records.name.endswith('.pdf'):
#             raise forms.ValidationError('Only PDF files are allowed.')
#         return records



class DateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self, *args, **kwargs):
        super(DateInput, self).__init__(*args, **kwargs)
        self.attrs['min'] = timezone.now().strftime('%Y-%m-%d')

class MyForm(forms.Form):
    my_date = forms.DateField(widget=DateInput())

class TimeInput(forms.TimeField):
    input_type = 'time'

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=10,min_length=10)
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','password1','password2','phone_number')


class BookingForm(forms.ModelForm):
    # booked_user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Booking
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
             'doc_name': "Doctor Name: ",
             'booking_date': "Booking Date: ",
             'time_slot': "Slot:",
             'description' : "Description:",
        }



class Details_UserForm(ModelForm):
    class Meta:
        model = Details_User
        fields = '__all__'

        widgets = {
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blood Group'}),
            'gender': forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),
            'age': forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'allergies': forms.TextInput(attrs={'class':'form-control','placeholder':'Any Allergies'}),

        }


class Details_DoctorForm(ModelForm):
    class Meta:
        model = Details_Doctor
        fields = '__all__'

        widgets = {
            'doc_name': '',
            'gender': forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),
            'age': forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'year_of_experience': forms.TextInput(attrs={'class':'form-control','placeholder':'Year of Experience'}),
        }


class Update_BookingForm(forms.ModelForm):
    class Meta:
        model = Update_Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
             'doc_name': "Doctor Name: ",
             'booking_date': "Booking Date: ",
             'time_slot': "Slot:",
             'description' : "Description:",
        }

GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
]
BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'),
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('O-', 'O-'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
]

SUPPLIMENT_CHOICES = [
    ('Multivitamin', 'Multivitamin'),
    ('Omega3', 'Omega3'),
    ('Vitamin3', 'Vitamin3'),
    ('BComplex', 'BComplex'),
    ('Vitamin D/D3', 'Vitamin D/D3'),
    ('Zinc', 'Zinc'),
    ('Folic Acid', 'Folic Acid'),
    ('Melatonin', 'Melatonin'),
    ('Biotin', 'Biotin'),
    ('Coenzyme', 'Coenzyme'),
    ('None', 'None'),
    ('Other', 'Other'),
]

ISSUES_CHOICES = [
    ('Hormone Imbalance', 'Hormone Imbalance'),
    ('Asthma', 'Asthma'),
    ('Cancer/Systemic disease', 'Cancer/Systemic disease'),
    ('Epilepsy/Seizure', 'Epilepsy/Seizure'),
    ('High Blood Pressure', 'High Blood Pressure'),
    ('Diabetes', 'Diabetes'),
    ('Heart Problems', 'Heart Problems'),
    ('HIV/AIDS', 'HIV/AIDS'),
    ('Auto immune Disorder', 'Auto immune Disorder'),
    ('Depression', 'Depression'),
    ('HeadAches/Migrations', 'HeadAches/Migrations'),
    ('Other', 'Other'),
    ('None', 'None'),
]

ALLERGY_CHOICES = [
    ('Aspirin', 'Aspirin'),
    ('Shellfish', 'Shellfish'),
    ('Tree Nuts', 'Tree Nuts'),
    ('Iodine', 'Iodine'),
    ('Latex', 'Latex'),
    ('Dairy', 'Dairy'),
    ('Fruits', 'Fruits'),
    ('Vegetables', 'Vegetables'),
    ('Other', 'Other'),
    ('None', 'None'),
]

SMOKER_CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]
BEVARAGE_CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]
CLAUSTROPHOBIC_CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]
PAIN_CHOICES = [
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
]
class PatientsForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES,widget=forms.RadioSelect)
    supplements =forms.MultipleChoiceField(label='Do you take any of the following health/dietry supplements?',
                                           choices=SUPPLIMENT_CHOICES,widget=forms.CheckboxSelectMultiple)
    health_issues = forms.MultipleChoiceField(label='Have you ever experienced any of these health conditions in the past or present?',
                                           choices=ISSUES_CHOICES,widget=forms.CheckboxSelectMultiple)
    allergies = forms.MultipleChoiceField(label='Have any Allegies?',
                                           choices=ALLERGY_CHOICES,widget=forms.CheckboxSelectMultiple)
    smoker = forms.ChoiceField(choices=SMOKER_CHOICES,widget=forms.RadioSelect,label='Are you a Smoker?')
    beverages = forms.ChoiceField(choices=BEVARAGE_CHOICES,widget=forms.RadioSelect,label='Do you drink more than 4 caffeinated beverages a day?')
    claustrophobic = forms.ChoiceField(choices=CLAUSTROPHOBIC_CHOICES,widget=forms.RadioSelect,label='Have you ever experienced claustrophobic?')
    pain = forms.ChoiceField(choices=PAIN_CHOICES,widget=forms.RadioSelect,label='Rate your tolerence in pain?')

    class Meta:
        model = Patients
        fields =  ['date_of_birth','previous_report','photo1','photo2','photo3']
    labels = {'date_of_birth':'Dateof Birth','previous_report':"Previous Report",
              'photo1':"Photo1",'photo2':"Photo2",
              'photo3':"Photo3"
              }
    widgets = {
        'date_of_birth':forms.TextInput(attrs={'class':'form-control','id':'datepicker'}),
    }



class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

        # widgets = {
        #     'medicine': forms.TextInput(attrs={'class':'form-control','placeholder':'Medicine'}),
        #     'dose': forms.TextInput(attrs={'class':'form-control','placeholder':'Dosage'}),
        # }

# class Update_PrescriptionForm(forms.ModelForm):
#     class Meta:
#         model = Update_Prescription
#         fields = '__all__'
#
#         widgets = {
#             'medicine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine'}),
#             'dose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dosage'}),
#         }

# from django import forms
#
# class ReviewForm(forms.Form):
#     rating = forms.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['service', 'comment', 'rate']