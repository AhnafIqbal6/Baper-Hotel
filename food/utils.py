import smtplib
from email.mime.text import MIMEText
#xujquawoqnsfppnv
#

def customSendMail(subject, message, receiver_email):
    try:
        # sender email with 2 step verification enable
        sender_email = "shahidfakeemai@gmail.com"
        # app password and also enable less secure. (while generating app password select app as "mail".)
        password = 'xujquawoqnsfppnv'
        msg = MIMEText(f'{message}')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print('otp send succesfully.')
    except Exception as e:
        print(e)
        print('uanble to send otp.')
