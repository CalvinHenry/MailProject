import argparse
import smtplib
import imaplib



global fromaddr, username, password, server, inbox, readServer


def intializeGlobals():
    global fromaddr, username, password, server
    fromaddr = 'Person'
    username = 'pythonemailprogramtest@gmail.com'
    password = 'Isitameatpieorafruitpie?'
    server = smtplib.SMTP('smtp.gmail.com:587')
    readServer = imaplib.IMAP4_SSL\
                 ('imap.gmail.com',993)
    readServer.login(username,password)

    inbox,cnt = readServer.select('Inbox')

    inbox, dta = readServer.fetch\
                 (cnt[0],\
                  '(UID BODY[TEXT])')

    print dta[0][1]

    readServer.close()
    readServer.logout()
    
    return;

def sendEmail(recipient, subject, email):
    global fromaddr, username, password, server
        
    toaddrs = recipient
    msg = email
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return;

def checkMail():

    return;


intializeGlobals()
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--recipient', '-r', type=str)
parser.add_argument('--subject', '-s')
parser.add_argument('--email', '-m')
args = parser.parse_args()
#print(inbox)
#sendEmail(args.recipient, args.subject, args.email)

