import ssl
import smtplib 
import web_scraper
import json
from datetime import date
from bs4 import BeautifulSoup
from email.message import EmailMessage

with open("key.json", "r") as f:
        days = json.load(f)

if str(date.today()) not in list(days.keys()):
    title, text = web_scraper.scrape()

    email_sender = 'defnotanemailbot@gmail.com'
    email_password = "xjse eevc ptbw prms"
    email_reciever = "walkingtech43@gmail.com"

    subject = f"Painter of the Day: {title}"
    body = text

    em = EmailMessage()
    em['From'] = email_sender
    em["To"] = email_reciever
    em["Subject"] = subject
    em.set_content(body)

    ctext = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctext) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

    with open("key.json", "w") as f:
        days[str(date.today())] = str(title)
        json.dump(days, f, indent=4)

    print("sent")

else:
    print("Already sent today's artist of the day!")



