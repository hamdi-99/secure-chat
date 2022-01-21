import smtplib, ssl
import os
from dotenv import load_dotenv
from phase12.random_string import randomSring

load_dotenv()


def sendMail(receiver_email, message):
    port = os.getenv('smtp_port')  # For SSL
    password = os.getenv('smtp_password')
    sender_email = os.getenv('smtp_sender')
    receiver_email = "hamdiharaketi@insat.u-carthage.tn"
    smtp_server = os.getenv('smtp_server')

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        # server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, format_message(message, sender_email))
    print("email sent successfuly")


def format_message(content: str, sender: str):
    email_text = """\
    Subject: Verification from python app

    use this code to authenticate
    """ + content
    return email_text
