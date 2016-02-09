import argparse
import smtplib


def sendEmail(recipient, subject, email):
    fromaddr = 'calvinhenry60@gmail.com'
    toaddrs = recipient
    msg = email
    username = 'calvinhenry60@gmail.com'
    password = '500006176'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return;

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--recipient', '-r', type=str)
parser.add_argument('--subject', '-s')
parser.add_argument('--email', '-m')

args = parser.parse_args()
sendEmail(args.recipient, args.subject, args.email)
print(args.subject)
print(args.recipient)

