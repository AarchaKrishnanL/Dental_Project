from datetime import timezone, timedelta

# import Payment as Payment
from django.contrib.auth import authenticate, login,logout
import subprocess
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.template.loader import render_to_string
from django.views import View

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas

from reportlab.pdfgen import canvas
from reportlab.platypus import Table

from django.shortcuts import get_object_or_404
from datetime import datetime

from django.conf import settings



from tkinter import *
import os

from django.views.generic import CreateView
from reportlab.platypus import TableStyle
from scipy.optimize._tstutils import description
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas

from dental_project import settings
from .forms import BookingForm, Details_UserForm, Details_DoctorForm, RegisterUserForm, Update_BookingForm, \
    PrescriptionForm, ReviewForm
# from .forms import PatientForm, MedicalHistoryForm, GeneralHealthForm
from .models import Services, Doctors, Booking, Time_slot, Details_User, Update_Booking, Details_Doctor, Prescription, \
    CustomUser, Patients, Review, ReviewRating
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientsForm
# from .forms import DentalForm

# Create your views here.

from django.urls import reverse
import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY

# from home_app.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def demo(request):
    return render(request, "doctor_patient.html")

#
# def additional(request):
#     return render(request, "consultation_form.html")

def details_successfull(request):

    return render(request, "details_successfull.html")




def predict(request):
    # print('haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    subprocess.run(['python', 'home_app/disease_prediction.py'])
    return redirect("index")






def payment(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1MjGEeSA2phBeRUBBCL7Zaog',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('front')),
    )

    context = {
        'session_id':session.id,
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY
    }
    return render(request,'payment.html',context)


def thanks(request):
    return render(request, "thanks.html")


def front(request):
    return render(request, "front.html")

def prescription(request):
    return render(request, "prescription.html")

def about(request):
    return render(request, "about.html")

def doctor_page(request):
    return render(request, "doctor_page.html")

def update_booking(request):
    return render(request, "update_booking.html")

def loginn(request):
    return render(request, "registration/loginn.html")

def doctor_patient(request):
    return render(request, "doctor_patient.html")

def consultation_view(request):
    return render(request, "consultation_view.html")



def doctor_register(request):
    return render(request, "doctor_register.html")

def bonding(request):
    return render (request,"bonding.html")

def crown(request):
    return render (request,"crown.html")

def veeners(request):
    return render (request,"veeners.html")


def cleaning(request):
    return render (request,"cleaning.html")

def filling(request):
    return render (request,"filling.html")


def time_slot(request):
    dict_timeslot={
        'time_slot':Time_slot.objects.all()
    }
    return render(request, "time_slot.html",dict_timeslot)


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            doc_name=form.cleaned_data['doc_name']
            booking_date = form.cleaned_data['booking_date']
            time_slot = form.cleaned_data['time_slot']
            description = form.cleaned_data['description']
            booking = Booking(doc_name=doc_name, booking_date=booking_date, time_slot=time_slot,
                              description=description)
            booking.save()
            send_confirmation_email(booking)
            messages.info(request, 'New booking added successfully')
            booking_info=Booking.objects.filter()
            return render(request, 'my_bookings.html',{
                'info':booking_info,
                'doc_name':doc_name,
                'booking_date':booking_date,
                'time_slot':time_slot,
                'description':description,
            })
    else:
        form=BookingForm
    return render(request,'booking.html',{'form':form})


def send_confirmation_email(booking):
    # Render the email template with appointment details

    email_html = render_to_string('appointment_confirmation_email.html', {'booking': booking})
    # Create the email message
    email = EmailMessage(
        subject='Appointment Confirmation',
        body=email_html,
        from_email=settings.EMAIL_HOST_USER,
        to=['archakrishnan22@gmail.com']
        # to=[booking.user.email]
    )

    # Send the email
    email.content_subtype = 'html'
    email.send()


def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_docs)


def contact(request):
    return render(request, "contact.html")


def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'services.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('indexx')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def doctorlogin(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor_page')
            else:
                error_message = "Invalid username or password"
                return render(request, 'doctorlogin.html', {'error_message': error_message})
        else:
            return render(request, 'doctorlogin.html')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return render(request, 'register_confirmation.html')
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request,'register.html',{'form':form,})

def index(request):
    return render (request,"index.html")

def indexx(request):
    return render (request,"indexx.html")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')


def toconsult_form(request):
    return render(request, "toconsult_form.html")


def user(request):
    if request.user.is_authenticated:
        return render(request, "indexx.html")
    return redirect('login')


def my_bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        doc_name = form.cleaned_data['doc_name']
        booking_date = form.cleaned_data['booking_date']
        time_slot = form.cleaned_data['time_slot']
        description = form.cleaned_data['description']
        booking = Booking(doc_name=doc_name, booking_date=booking_date, time_slot=time_slot,
                              description=description)
        booking.save()
        messages.info(request, 'New booking added successfully')
        booking_info = Booking.objects.filter()
        return render(request, 'my_bookings.html', {
                'info': booking_info,
                'doc_name': doc_name,
                'booking_date': booking_date,
                'time_slot': time_slot,
                'description': description,
            })
    if request.user.is_authenticated:
        booking_info = Booking.objects.all()
        # booking_info = Booking.objects.filter(user=request.user)
        return render(request, "my_bookings.html",{
            'info':booking_info,
        })
    return redirect('booking')

# CRUD OPERATIONS
def Delete(request,id):
    booking_info = Booking.objects.filter(id=id)
    booking_info.delete()
    messages.info(request, "Appointment Deleted!!!")
    return redirect("my_bookings")

#
# def Update(request,id):
#     if request.method == 'POST':
#         result=Booking.objects.get(id=id)
#         form = BookingForm(request.POST, instance=result)
#         if form.is_valid():
#             form.save()
#     else:
#         result = Booking.objects.get(id=id)
#         form = BookingForm(instance=result)
#         messages.info(request, "Updated!!!")
#     return render(request,'update_booking.html', {'form':form})



def update_details(request, id):
    if request.method == 'POST':
        us = Details_User.objects.get(id=id)
        form = Details_UserForm(request.POST,instance=us)
        if form.is_valid():
            form.save()
    else:
        us = Details_User.objects.get(id=id)
        form = Details_UserForm(request.POST, instance=us)
    return render(request,'update_details.html',{'form':form})

# def view_user(request):
#     if request.user.is_authenticated:
#         user_info = Details_User.objects.filter(user=request.user)
#         return render(request, "update_user.html",{
#             'info':user_info,
#         })


# def update_userdetails(request):
#     if request.user.is_authenticated:
#         user_info = Details_User.objects.filter(user=request.user)
#         return render(request, "update_user.html",{
#             'info':user_info,
#         })


# def details_doctor(request):
#     submitted = False
#     if request.method == "POST":
#         form = Details_DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/details_doctor?submitted=True')
#     else:
#         form = Details_DoctorForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request,'details_doctor.html', {'form':form, 'submitted':submitted})

def details_doctor(request):
    submitted = False
    if request.method == "POST":
        form = Details_DoctorForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            year_of_experience = form.cleaned_data['year_of_experience']
            details_dtr=Details_Doctor(gender=gender,age=age,address=address,year_of_experience=year_of_experience)
            details_dtr.save()
            form = Details_DoctorForm
    else:
        form = Details_DoctorForm
    doctordetails = Details_Doctor.objects.all()
    return render(request,'details_user.html', {'form':form,'doctordetails':doctordetails})

def update_doctor(request, id):
    if request.method == 'POST':
        dr = Details_Doctor.objects.get(id=id)
        form = Details_UserForm(request.POST,instance=dr)
        if form.is_valid():
            form.save()
    else:
        us = Details_Doctor.objects.get(id=id)
        form = Details_DoctorForm(request.POST, instance=us)
    return render(request,'update_doctor.html',{'form':form})

def update_booking(request):
    if request.method == "POST":
        form = Update_BookingForm(request.POST)
        if form.is_valid():
            doc_name=form.cleaned_data['doc_name']
            booking_date = form.cleaned_data['booking_date']
            time_slot = form.cleaned_data['time_slot']
            description = form.cleaned_data['description']
            booking = Update_Booking(doc_name=doc_name,booking_date=booking_date,time_slot=time_slot,description=description)
            booking.save()
            messages.info(request,'New booking added successfully')
            booking_info=Update_Booking.objects.filter()
            return render(request, 'my_bookings.html',{
                'info':booking_info,
                'doc_name':doc_name,
                'booking_date':booking_date,
                'time_slot':time_slot,
                'description':description,
            })
    else:
        form=BookingForm
    return render(request,'booking.html',{'form':form})


def services_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            services = Services.objects.filter(ser_name__icontains=query)
            context = {'services': services, 'query': query}
            return render(request, 'services_search.html', context)

    return redirect('services')

def doctors_search(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctors.objects.filter(
            Q(doc_name__icontains=query)
            # Q(doc_spec__icontains=query) |
            # Q(service__ser_name__icontains=query)
        )
    else:
        doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
        'query': query
    }
    return render(request, "doctors_search.html", context)







def doctor_bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        booked_user = form.cleaned_data['booked_user']
        # doc_name = form.cleaned_data['doc_name']
        booking_date = form.cleaned_data['booking_date']
        time_slot = form.cleaned_data['time_slot']
        description = form.cleaned_data['description']
        booking = Booking(booked_user=booked_user, booking_date=booking_date, time_slot=time_slot,
                              description=description)
        booking.save()
        messages.info(request, 'New booking added successfully')
        booking_info = Booking.objects.filter()
        return render(request, 'doctor_bookings.html', {
                'info': booking_info,
                'booked_user': booked_user,
                # 'doc_name': doc_name,
                'booking_date': booking_date,
                'time_slot': time_slot,
                'description': description,
            })
    if request.user.is_authenticated:
        current_doctor = request.user.is_authenticated
        current_user = request.user
        booking_info = Booking.objects.filter(doc_name=current_doctor )
        return render(request, "doctor_bookings.html",{
            'info':booking_info,
        })
    return redirect('booking')



def view_receipt(request, booking_id):
    data = Booking.objects.get()
    # Get the booking details from the request
    doc_name_id = data.doc_name_id
    booking_date = data.booking_date
    booked_on = data.booked_on
    time_slot_id = data.time_slot_id
    description = data.description
    print(doc_name_id )
    doctor=Doctors.objects.get(id=doc_name_id)
    time_slot = Time_slot.objects.get(id=time_slot_id)

    # Create a booking object with the details
    booking = Booking(doc_name_id=doctor,booked_on =booked_on,
                      booking_date=booking_date, time_slot_id=time_slot,
                      description=description)

    dataa = Prescription.objects.get()
    # Get the booking details from the request
    medications = dataa.medications
    dosage = dataa.dosage
    oral_findings =dataa.oral_findings
    diagnosis = dataa.diagnosis
    treatment_plan=dataa.treatment_plan
    duration=dataa.duration
    post_treatment=dataa.post_treatment
    dietary_restrictions=dataa.dietary_restrictions
    remarks=dataa.remarks
    # medications=Prescription.objects.get()

    # Create a booking object with the details
    prescription = Prescription(medications=medications,dosage =dosage,oral_findings=oral_findings,diagnosis=diagnosis,
                                treatment_plan=treatment_plan,duration=duration,post_treatment=post_treatment,
                                dietary_restrictions=dietary_restrictions,remarks=remarks)

    # Create a PDF file object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="booking.pdf"'

    # Create a canvas object and write the PDF content
    p = canvas.Canvas(response, pagesize=letter)

    # Set background color
    p.setFillColorRGB(0.5, 0.5, 1)  # Set background color to light blue
    p.rect(0, 0, 612, 792, fill=True)  # Draw a rectangle to fill the entire page

    # Set font type and size for the title
    p.setFont("Helvetica-Bold", 36)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(100, 750, "Receipt")

    # Set font type and size for the table headings and content
    p.setFont("Helvetica-Bold", 12)

    # Draw the table for booking details
    booking_table_data = [
        ["Booking Details"],  # Add the booking details heading
        ["Patient Name", "Maaya Krishna"],
        ["Doctor", str(booking.doc_name_id)],
        ["Booking date", str(booking.booking_date)],
        ["Time slot", str(booking.time_slot_id)],
        ["Description", str(booking.description)],
        ["Fee", "120/-"],
        ["Payment Status", "Success"]
    ]
    booking_table = Table(booking_table_data, colWidths=[150, 150])
    booking_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    booking_table.wrapOn(p, 400, 200)
    booking_table.drawOn(p, 100, 600)

    # Draw the table for prescription details
    prescription_table_data = [
        ["Prescription Details"],  # Add the prescription details heading
        ["Medications", prescription.medications],
        ["Dosage", prescription.dosage],
        ["Oral Findings", prescription.oral_findings],
        ["Diagnosis", prescription.diagnosis],
        ["Treatment Plan", prescription.treatment_plan],
        ["Duration", prescription.duration],
        ["Post Treatment", prescription.post_treatment],
        ["Dietary Restrictions", prescription.dietary_restrictions],
        ["Follow Update", prescription.follow_up_date],
        ["Remarks", prescription.remarks]
    ]
    prescription_table = Table(prescription_table_data, colWidths=[150, 150])
    prescription_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    prescription_table.wrapOn(p, 400, 200)
    prescription_table.drawOn(p, 100, 350)

    # Save the PDF document
    p.showPage()
    p.save()

    return response






#
#
# def view_receipt(request, booking_id):
#     # Retrieve the booking object
#     booking = Booking.objects.get(id=booking_id)
#
#     # Retrieve the related prescription object for the booking
#     prescription = get_object_or_404(Prescription, booking_id=booking_id)
#
#     # Get the booking details
#     doc_name_id = booking.doc_name_id
#     booking_date = booking.booking_date
#     booked_on = booking.booked_on
#     time_slot_id = booking.time_slot_id
#     description = booking.description
#
#     # Rest of the code...
#
#     # doctor = Doctors.objects.get(id=doc_name_id)
#     # time_slot = Time_slot.objects.get(id=time_slot_id)
#
#     # Get the prescription details
#     medications = prescription.medications
#     dosage = prescription.dosage
#     date_of_prescription = prescription.date_of_prescription
#     oral_findings = prescription.oral_findings
#     diagnosis = prescription.diagnosis
#     treatment_plan = prescription.treatment_plan
#     duration = prescription.duration
#     post_treatment = prescription.post_treatment
#     dietary_restrictions = prescription.dietary_restrictions
#     follow_up_date = prescription.follow_up_date
#     remarks = prescription.remarks
#
#     # Create a PDF file object
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="booking.pdf"'
#
#     # Create a canvas object and write the PDF content
#     p = canvas.Canvas(response)
#
#     p.setFillColorRGB(0.5, 0.5, 1)  # Set background color to light blue
#     p.rect(0, 0, 612, 1000, fill=True)  # Draw a rectangle to fill the entire page
#
#     p.setFont("Helvetica-Bold", 36)  # Set font type and size
#     p.setFillColorRGB(0, 0, 0)  # Set text color to red
#     p.drawString(100, 750, "Receipt")  # Draw the "Receipt" text
#     p.setFont("Helvetica-Bold", 12)  # Set font type and size for the remaining text
#     p.setFillColorRGB(0, 0, 0)  # Set text color to black
#     p.drawString(100, 700, f"Patient Name: Maaya Krishna")
#     p.drawString(100, 650, f"Doctor: {doc_name_id}")
#     p.drawString(100, 600, f"Booking date: {booking_date}")
#     p.drawString(100, 550, f"Booked on: {booked_on}")
#     p.drawString(100, 500, f"Time slot: {time_slot_id}")
#     p.drawString(100, 450, f"Description: {description}")
#     p.drawString(100, 400, f"Fee: 120/-")
#     p.drawString(100, 350, f"Payment Status: Success")
#
#     # Include prescription fields
#     p.drawString(100, 300, f"Medications: {medications}")
#     p.drawString(100, 280, f"Dosage: {dosage}")
#     p.drawString(100, 260, f"Date of Prescription: {date_of_prescription}")
#     p.drawString(100, 240, f"Oral Findings: {oral_findings}")
#     p.drawString(100, 220, f"Diagnosis: {diagnosis}")
#     p.drawString(100, 200, f"Treatment Plan: {treatment_plan}")
#     p.drawString(100, 180, f"Duration: {duration}")
#     p.drawString(100, 160, f"Post Treatment: {post_treatment}")
#     p.drawString(100, 140, f"Dietary Restrictions: {dietary_restrictions}")
#     p.drawString(100, 120, f"Follow-up Date: {follow_up_date.strftime('%Y-%m-%d %H:%M')}")
#     p.drawString(100, 100, f"Remarks: {remarks}")
#
#     p.showPage()
#     p.save()
#
#     return response
#
#
#


class patient_form(View):
    def get(self,request):
        form = PatientsForm()
        return  render(request,'patient_form.html',{'form':form})
    def post(self, request):
        form = PatientsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'patient_form.html',{'form':form})

def patient_form(request):
    if request.method == "POST":
        form = PatientsForm(request.POST)
        if form.is_valid():
            gender=form.cleaned_data['gender']
            blood_group = form.cleaned_data['blood_group']
            date_of_birth = form.cleaned_data['date_of_birth']
            previous_report = form.cleaned_data['previous_report']
            supplements = form.cleaned_data['supplements']
            health_issues = form.cleaned_data['health_issues']
            allergies = form.cleaned_data['allergies']
            smoker = form.cleaned_data['smoker']
            beverages = form.cleaned_data['beverages']
            claustrophobic = form.cleaned_data['claustrophobic']
            pain = form.cleaned_data['pain']
            photo1 = form.cleaned_data['photo1']
            photo2 = form.cleaned_data['photo2']
            photo3 = form.cleaned_data['photo3']
            patient_form = Patients(gender=gender, blood_group=blood_group, date_of_birth=date_of_birth,
                                        previous_report=previous_report, supplements=supplements, health_issues=health_issues,
                                        allergies=allergies, smoker=smoker, beverages=beverages,claustrophobic=claustrophobic,
                                        pain=pain,photo1=photo1,photo2=photo2,photo3=photo3)
            patient_form.save()
            messages.info(request, 'Consultation form successfully')
            consultation_info=Patients.objects.filter()
            return render(request, 'consultation_view.html',{
                'info':consultation_info,
                'gender':gender,
                'blood_group':blood_group,
                'date_of_birth':date_of_birth,
                'previous_report': previous_report,
                'supplements': supplements,
                'health_issues': health_issues,
                'allergies': allergies,
                'smoker': smoker,
                'beverages': beverages,
                'claustrophobic': claustrophobic,
                'pain': pain,
                'photo1': photo1,
                'photo2': photo2,
                'photo3': photo3,

        })
    else:
        form=PatientsForm
    return render(request,'patient_form.html',{'form':form})


def prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_prescription')
    else:
        form = PrescriptionForm()
    return render(request, 'prescription.html', {'form': form})



def my_prescription(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'my_prescription.html', {'prescriptions': prescriptions})


from .models import Prescription
from .forms import PrescriptionForm

def edit_prescription(request, prescription_id):
    prescription = Prescription.objects.get(id=prescription_id)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('my_prescription')
    else:
        form = PrescriptionForm(instance=prescription)

    return render(request, 'edit_prescription.html', {'form': form})

def delete_prescription(request, prescription_id):
    prescription = Prescription.objects.get(id=prescription_id)
    prescription.delete()
    return redirect('my_prescription')



def service_detail(request, service_id):
    service = Services.objects.get(pk=service_id)
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        comment = request.POST['comment']
        Review.objects.create(service=service, rating=rating, comment=comment)
        return redirect('service_detail', service_id=service_id)
    return render(request, 'services.html', {'services': [service]})

def add_review(request):
    if request.method == 'POST':
        service_id = request.POST.get('service')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')

        service = Services.objects.get(id=service_id)
        review = Review.objects.create(service=service, comment=comment, rate=rate)

    return redirect('services')

def service_reviews_graph(request):
    services = Services.objects.all()

    service_names = []
    average_ratings = []

    for service in services:
        reviews = Review.objects.filter(service=service)

        if reviews:
            total_ratings = sum(review.rate for review in reviews)
            average_rating = total_ratings / len(reviews)
        else:
            average_rating = 0

        service_names.append(service.ser_name)
        average_ratings.append(average_rating)

    plt.bar(service_names, average_ratings)
    plt.xlabel('Services')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings for Services')
    plt.ylim(0, 5)
    plt.xticks(rotation=45)

    # Convert the plot to HTML
    import io
    import urllib, base64

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return render(request, 'service_reviews_graph.html', {'image_base64': image_base64})

    # Specify the file path for saving the chart image
    # file_path = os.path.join(settings.STATIC_ROOT, 'charts/chart.png')


import io
import urllib.parse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


from django.db.models import Count, Avg
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import tempfile
import os

def generate_service_reviews_report(request):
    services = Services.objects.annotate(num_bookings=Count('bookings')).all()

    service_names = []
    average_ratings = []
    num_bookings = []
    review_rate_percentages = []

    for service in services:
        reviews = Review.objects.filter(service=service)

        if reviews:
            total_ratings = sum(review.rate for review in reviews)
            average_rating = total_ratings / len(reviews)
            review_rate = (len(reviews) / service.num_bookings) * 100 if service.num_bookings > 0 else 0
        else:
            average_rating = 0
            review_rate = 0

        service_names.append(service.ser_name)
        average_ratings.append(average_rating)
        num_bookings.append(service.num_bookings)
        review_rate_percentages.append(review_rate)

    plt.bar(service_names, average_ratings)
    plt.xlabel('Services')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings for Services')
    plt.ylim(0, 5)
    plt.xticks(rotation=45)

    # Save the plot as an image file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        plt.savefig(temp_file.name)

    # Create a PDF report
    pdf_buffer = io.BytesIO()
    canvas_obj = canvas.Canvas(pdf_buffer, pagesize=letter)
    canvas_obj.drawImage(temp_file.name, 50, 50, width=500, height=300)
    canvas_obj.showPage()

    # Write the service details to the PDF report
    canvas_obj.setFont("Helvetica", 12)
    y = 500
    line_height = 20
    for i, service_name in enumerate(service_names):
        canvas_obj.drawString(50, y, f"Service: {service_name}")
        canvas_obj.drawString(50, y - line_height, f"Average Rating: {average_ratings[i]:.2f}")
        canvas_obj.drawString(50, y - line_height * 2, f"Number of Bookings: {num_bookings[i]}")
        canvas_obj.drawString(50, y - line_height * 3, f"Review Rate Percentage: {review_rate_percentages[i]:.2f}%")
        canvas_obj.drawString(50, y - line_height * 4, "-----------------------------")
        y -= line_height * 5

    canvas_obj.save()

    # Close and remove the temporary image file
    plt.close()
    os.remove(temp_file.name)

    # Set the response content type as PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="service_reviews_report.pdf"'

    # Write the PDF buffer to the response
    response.write(pdf_buffer.getvalue())
    pdf_buffer.close()

    return response



# def generate_service_reviews_report(request):
#     services = Services.objects.all()
#
#     service_names = []
#     average_ratings = []
#
#     for service in services:
#         reviews = Review.objects.filter(service=service)
#
#         if reviews:
#             total_ratings = sum(review.rate for review in reviews)
#             average_rating = total_ratings / len(reviews)
#         else:
#             average_rating = 0
#
#         service_names.append(service.ser_name)
#         average_ratings.append(average_rating)
#
#     plt.bar(service_names, average_ratings)
#     plt.xlabel('Services')
#     plt.ylabel('Average Rating')
#     plt.title('Average Ratings for Services')
#     plt.ylim(0, 5)
#     plt.xticks(rotation=45)
#
#     # Save the plot as an image file
#     with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
#         plt.savefig(temp_file.name)
#
#     # Create a PDF report
#     pdf_buffer = io.BytesIO()
#     canvas_obj = canvas.Canvas(pdf_buffer, pagesize=letter)
#     canvas_obj.drawImage(temp_file.name, 50, 50, width=500, height=300)
#     canvas_obj.showPage()
#     canvas_obj.save()
#
#     # Close and remove the temporary image file
#     plt.close()
#     os.remove(temp_file.name)
#
#     # Set the response content type as PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="service_reviews_report.pdf"'
#
#     # Write the PDF buffer to the response
#     response.write(pdf_buffer.getvalue())
#     pdf_buffer.close()
#
#     return response


def review_graph_admin(request):
    services = Services.objects.all()

    service_names = []
    average_ratings = []

    for service in services:
        reviews = Review.objects.filter(service=service)

        if reviews:
            total_ratings = sum(review.rate for review in reviews)
            average_rating = total_ratings / len(reviews)
        else:
            average_rating = 0

        service_names.append(service.ser_name)
        average_ratings.append(average_rating)

    plt.bar(service_names, average_ratings)
    plt.xlabel('Services')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings for Services')
    plt.ylim(0, 5)
    plt.xticks(rotation=45)

    # Convert the plot to HTML
    import io
    import urllib, base64

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return render(request, 'review_graph_admin.html', {'image_base64': image_base64})
