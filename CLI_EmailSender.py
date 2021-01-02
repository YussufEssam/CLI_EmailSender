import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from PySide2 import QtWidgets

def send_email(email, password, remail, subject, body):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = remail
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)

    server.sendmail(email,remail,text)
    server.quit()

    app = QtWidgets.QApplication()
    QtWidgets.QMessageBox.information(None, 'Email Sender', 'Email Send Successfully')

if __name__ == '__main__':

    parser =argparse.ArgumentParser(prog='Email Sender',
                                    usage='''
                                    Usage:
                                    Enter your email credentials and
                                    email data to send emails.
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    Send Email By this CLI Application
                                    -----------------------------------------------
                                    ''',
                                    epilog="Copyrights @ FCAI Helwan University",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )

    parser.add_argument("email", type=str, help="Enter your email. for example: example@gmail.com", metavar="SENDER_EMAIL")
    parser.add_argument("password", type=str, help="Enter your password.", metavar="SENDER_PASSWORD")
    parser.add_argument("remail", type=str, help="Enter The Recipient Email.", metavar="RECIPIENT_EMAIL")
    parser.add_argument("subject", type=str, help="Enter The Email Subject.", metavar="EMAIL_SUBJECT")
    parser.add_argument("body", type=str, help="Enter The Email Body.", metavar="EMAIL_BODY")

    arg = parser.parse_args()
    send_email(arg.email, arg.password, arg.remail, arg.subject, arg.body)
