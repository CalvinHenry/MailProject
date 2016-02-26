import argparse
import smtplib
import imaplib



global fromaddr, username, password, server, inbox, readServer, lastEmail, readServer


def intializeGlobals():
    global fromaddr, username, password, server, lastEmail, readServer
    fromaddr = 'Person'
    username = 'pythonemailprogramtest@gmail.com'
    password = 'Isitameatpieorafruitpie?'
    server = smtplib.SMTP('smtp.gmail.com:587')
    readServer = imaplib.IMAP4_SSL\
                 ('imap.gmail.com',993)    
    return;
                                       


def sendEmail(recipient, subject, email):
    global fromaddr, username, password, server
    toaddrs = recipient
    msg = email
    server.sendmail(fromaddr, toaddrs, msg)
    return;

def writeServerLogin(localUsername, localPassword):
    global server
    server.ehlo()
    server.starttls()
    server.login(localUsername, localPassword)
    return;

def writeServerLogout():
    server.quit()
    return;
def readServerLogin(localUsername, localPassword):
    global readServer
    readServer.login(localUsername, localPassword)
    return;
def readServerLogout():
    readServer.close()
    readServer.logout()
    return;

def readMail():
    print 'Reading Mail'
    sucess, mailboxes = readServer.list();
    sucess,inbox = readServer.select('PhoneStuff')
    #Note to self, make sure you test that this will not get mail from the inbox, just PhoneStuff
    sucess, dta = readServer.search(None, '(UNSEEN)')
    if sucess == 'OK' or  len(dta) < 1:
        for num in dta[0].split(' '):
            try :
                sucess, data = readServer.fetch(num,'(RFC822)')
                text = data[0][1]
                print trimString(text)
                parseString(trimString(text))
                typ, data = readServer.store(num,'+FLAGS','\\Seen')
            except:
                print 'No Unread Email'    
    return;


def trimString(inFrom):
    #print(inFrom);
    front = 'Content-Location: text_0.txt'
    backExtraConst = -2;
    frontExtraConst = 4
    back = '--__CONTENT_64564_PART_BOUNDARY__33243242__--'
    
    parse = inFrom[inFrom.find(front)+ len(front)+ frontExtraConst:\
                   inFrom.find(back)+ backExtraConst]

    return parse;

def parseString(text):
    recipientIndex = rightIndex(text, '-r')
    iterationsIndex = rightIndex(text, '-i')
    messageIndex = rightIndex(text, '-m')
    zeroIndex = 0
    lastIndex = len(text)
    indexList = [recipientIndex, iterationsIndex, messageIndex, zeroIndex, lastIndex]
    indexList.sort()
    try:
        recipient = getItem(text, indexList, recipientIndex)
        print indexList
        iterations = getItem(text, indexList, iterationsIndex)
        message = getItem(text, indexList, messageIndex)
    except:
        print 'error'
    print recipient
    print iterations
    print message
    
    return;

def getItem(text, indexList, index):
    return text[index : getNextItem(indexList, index)]
                         
def getNextItem(tempList, item):
    return tempList[tempList.index(item) + 1]


                         

def rightIndex(string, character):
    try:
        return string.index(character)
    except ValueError:
        return -1


                

intializeGlobals()
readServerLogin(username, password)
readMail()
readServerLogout()

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--recipient', '-r', type=str)
parser.add_argument('--subject', '-s')
parser.add_argument('--email', '-m')
args = parser.parse_args()
#print(inbox)
#writeServerLogin(username, password)
#sendEmail(args.recipient, args.subject, args.email)
#writeServerLogout()

