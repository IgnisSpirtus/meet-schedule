import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import json 
import schedule
import time
load_dotenv()
SENDER = os.getenv("GMAIL_USER")
PASSWORD = os.getenv("GMAIL_PASSWORD")
RECVER = os.getenv("GMAIL_REC")

f=open('meet-links.json',)
data = json.load(f)


def send_meet(meet_link):

    body = "Navigate to {} to join the class.".format(meet_link)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Attend this Class Now"
    msg['From'] = SENDER
    msg['To'] = RECVER
    body1 = MIMEText(body,'plain')
    msg.attach(body1)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(SENDER, PASSWORD)
    mail.sendmail(SENDER, RECVER,msg.as_string())
    print("Mail sent Succesfully ")
    mail.quit()

def monday_seires(time,meet):
    schedule.every().monday.at("{}".format(time)).do(send_meet,meet_link=meet)
    schedule.every().wednesday.at("{}".format(time)).do(send_meet,meet_link=meet)
    schedule.every().friday.at("{}".format(time)).do(send_meet,meet_link=meet)

def tuesday_seires(time,meet):
    schedule.every().tuesday.at("{}".format(time)).do(send_meet,meet_link=meet)
    schedule.every().thursday.at("{}".format(time)).do(send_meet,meet_link=meet)
    schedule.every().saturday.at("{}".format(time)).do(send_meet,meet_link=meet)


monday_seires(time="08:50",meet=data["CE-F231-LEC"])
monday_seires(time="10:50",meet=data["ECON-F312-LEC"])
monday_seires(time="11:50",meet=data["ECON-F311-LEC"])
schedule.every().monday.at("13:50").do(send_meet,meet_link=data["ECON-F312-TUT"])
monday_seires(time="14:50",meet=data["CE-F230-LEC"])
monday_seires(time="15:50",meet=data["CE-F211-LEC"])
schedule.every().tuesday.at("07:50").do(send_meet,meet_link=data["CE-F211-TUT"])
schedule.every().tuesday.at("08:50").do(send_meet,meet_link=data["CE-F230-PRAC"])
schedule.every().tuesday.at("15:50").do(send_meet,meet_link=data["ECON-F311-TUT"])
tuesday_seires(time="10:50",meet=data["ECON-F313-LEC"])
tuesday_seires(time="11:50",meet=data["CE-F213-LEC"])
schedule.every().thursday.at("07:50").do(send_meet,meet_link=data["CE-F231-TUT"])
schedule.every().thursday.at("08:50").do(send_meet,meet_link=data["CE-F213-PRAC"])
schedule.every().thursday.at("15:50").do(send_meet,meet_link=data["CE-F213-TUT"])
schedule.every().saturday.at("07:50").do(send_meet,meet_link=data["CE-F230-TUT"])



while True:
    schedule.run_pending()
    time.sleep(1)
