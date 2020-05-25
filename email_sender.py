import smtplib  # Protocol standard for email sending
from email.message import EmailMessage
from string import Template  # This can substitute variables inside text using the $ sign
from pathlib import Path  # They are similar to os.path module. Allows us to access paths

from_email = input('Inform your email: ')
from_email_password = input('Inform your email password: ')
smtp_host = input('Inform the smpt host for your email (you can google it): ')
html_document = Template(Path('index.html').read_text())  # Reads the text of the html document and using the Template
# on the text acquired so that we can convert text into variables
email = EmailMessage()  # Email object
email['from'] = 'Bruno Mileto'
email['to'] = 'brunomileto@outlook.com'
email['subject'] = 'You won R$ 1.000.000,00'

# email.set_content('I am a Python Master!')  # text, html, image etc
email.set_content(html_document.substitute(name='TinTin'), 'html')  # Where name is the variable in the $

with smtplib.SMTP(host=smtp_host, port=587) as smtp:  # smpt is a protocol, port is part of protocol (wikipedia)
    smtp.ehlo()  # part of the protocol
    smtp.starttls()  # encrypt mechanism for the protocol
    smtp.login(from_email, from_email_password)
    # For gmail you will need to allow acesse to app less security by going in:
    # https://myaccount.google.com/lesssecureapps?pli=1
    smtp.send_message(email)
    print('All good boss!')
