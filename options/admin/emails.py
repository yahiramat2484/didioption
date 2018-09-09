from options.app import app
from options.extensions import mail
from flask_mail import Message as MailMessage
from flask import render_template

def send_options_data(data):
    """
    Function to send user an email on their account and new password.
    :param user: New User Created with Paypal Login or New Guest User
    :return: Send the user his new account
    """

    send_email(subject="Options",
               recipients=["5618096654@tmomail.net", "csahirad@gmail.com", "yahir.amat@gmail.com"],
               text_body=render_template("emails/options.txt",
                                         data=data),
               html_body=render_template("emails/options.html",
                                         data=data))

def send_async_email(msg):
    """

    :param msg: Message to send Async
    :return: Send an email
    """
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, text_body, html_body, sender=""):
    """
    Send an email
    :param subject: Subject of the message (password reset, verify email)
    :param recipients: Who is receiving this text
    :param text_body: The content of the message in Text
    :param html_body: The content of the message in HTML
    :param sender: User who sends the email
    :return: calls send async email
    """
    if not sender:
        msg = MailMessage(subject, recipients=recipients)
    else:
        msg = MailMessage(subject, recipients=recipients, sender=sender)

    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)