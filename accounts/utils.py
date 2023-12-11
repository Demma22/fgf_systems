import random
from django.conf import settings
from django.core.mail import EmailMessage
from .models import User, OneTimePassword


def generate_otp():
    # Generate a 6-digit OTP
    return "".join(str(random.randint(1, 9)) for _ in range(6))


def send_code_to_user(email):
    # Subject for the email
    subject = "FGF OTP code for Email Verification"

    # Generate OTP and print for testing (you may remove the print statement in production)
    otp_code = generate_otp()
    print(otp_code)

    # Get user details from the database
    user = User.objects.get(email=email)

    # Set the appropriate value for your current site
    current_site = "https://your-website.com"

    # Email body with formatted string
    email_body = (
        f"Hello {user.first_name},\n\n"
        f"Thank you for signing up on {current_site}. We're thrilled to have you on board! "
        f"To complete the registration process, please verify your email by entering the following OTP: {otp_code}.\n\n"
        f"If you have any questions or need assistance, feel free to reach out to our support team.\n\n"
        "Welcome aboard!\n\nBest regards,\n[FGF-BIO-DIVERSITY]"
        
    )

    # Save OTP to the database
    OneTimePassword.objects.create(user=user, code=otp_code)

    # Configure and send the email
    from_email = settings.DEFAULT_FROM_EMAIL
    send_email = EmailMessage(
        subject=subject, body=email_body, from_email=from_email, to=[email]
    )
    send_email.send(fail_silently=True)

def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()