import argparse
import smtplib
import imaplib



global fromaddr, username, password, server, inbox, readServer, lastEmail


def intializeGlobals():
    global fromaddr, username, password, server, lastEmail
    fromaddr = 'Person'
    username = 'pythonemailprogramtest@gmail.com'
    password = 'Isitameatpieorafruitpie?'
    server = smtplib.SMTP('smtp.gmail.com:587')
    readServer = imaplib.IMAP4_SSL\
                 ('imap.gmail.com',993)
    readServer.login(username,password)

    sucess, mailboxes = readServer.list();
    sucess,inbox = readServer.select('PhoneStuff')
    #Note to self, make sure you test that this will not get mail from the inbox, just PhoneStuff
    sucess, dta = readServer.search(None, '(UNSEEN)')
    print sucess
    if sucess == 'OK' or  len(dta) < 1:
        print len(dta)
        for num in dta[0].split(' '):
            
            try :
                sucess, data = readServer.fetch(num,'(RFC822)')
                text = data[0][1]
                print parseString(text)
                typ, data = readServer.store(num,'+FLAGS','\\Seen')
            except:
                print 'No Unread Email'
            
            
    else:
        print "No read emails"
    #numOfMessages = dta[0][1]
    #print (numOfMessages)
#    text = dta[0]
#    print 'parsedVal'
#    print text
#    print 'parsed val length'
#    print len(text)
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


def parseString(inFrom):
    print(inFrom);
    front = 'Content-Location: text_0.txt'
    backExtraConst = -2;
    frontExtraConst = 4
    back = '--__CONTENT_64564_PART_BOUNDARY__33243242__--'
    
    parse = inFrom[inFrom.find(front)+ len(front)+ frontExtraConst:\
                   inFrom.find(back)+ backExtraConst]

    return parse;


intializeGlobals()
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--recipient', '-r', type=str)
parser.add_argument('--subject', '-s')
parser.add_argument('--email', '-m')
args = parser.parse_args()
#print(inbox)
#sendEmail(args.recipient, args.subject, args.email)


