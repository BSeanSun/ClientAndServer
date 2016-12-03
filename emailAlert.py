import smtplib
from email.mime.text import MIMEText
from email.header import Header
def alert():
    sender = 'sunboy_9037@163.com' #sent from this addr
    receivers = ['sunboy_9037@163.com', '9943489@qq.com'] #recver's addr

    #three para: content, format, code
    message = MIMEText('Current Temp Lower Than ZERO', 'plain', 'utf-8')
    message['subject'] = Header('Gardern Alert!', 'utf-8')
    message['from'] = 'sunboy_9037@163.com'
    message['to'] = 'sunboy_9037@163.com'
 
    smtpObj = smtplib.SMTP_SSL('smtp.163.com') #connect to 163 email
    smtpObj.login('sunboy_9037', 'sunboywhen11') #login to 163 email
    smtpObj.sendmail(sender, receivers, message.as_string()) #sent email from 163
    smtpObj.quit() #disconnect
    print 'sent successfully'

if __name__=="__main__":
    alert()
