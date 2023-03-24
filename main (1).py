import random
import string
import smtplib
import ssl
import re

# Replace with your own email credentials.
sender_email = "baigmassu535@gmail.com"
sender_password = "kuchyaadnahirehta"

# Replace with the recipient's email address.
recipient_email = "baigminaz720@gmail.com"

# Generate a random 12-digit OTP.
otp = "".join(
    random.choices(
        string.ascii_uppercase + string.ascii_lowercase + string.digits, k=12
    )
)

# Create an SSL context for secure email communication.
context = ssl.create_default_context()

# Send an email message with the OTP using SSL/TLS encryption.
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp_client:
    smtp_client.login(sender_email, sender_password)
    message = (
        f"Subject: Your One-Time Password\n\nHere is your one-time password:\n\n{otp}"
    )
    smtp_client.sendmail(sender_email, recipient_email, message)

# Prompt user email address.
recipient_email = input("Enter your email address: ")

# Validate email format.
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(pattern, recipient_email) == False:
    print("Enter a valid email address, terminating application.")
    exit()

# Prompt the user to enter the OTP received via email
user_input = input("Please enter the OTP received via email: ")

# Verify the OTP
if user_input == otp:
    print("OTP verification successful.")
else:
    print("OTP verification failed.")
