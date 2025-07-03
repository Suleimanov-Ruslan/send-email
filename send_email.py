import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_login =os.environ.get('LOGIN')
email_password =os.environ.get('TOKEN')

from_address = "@yandex.ru"
to_address = "@yandex.ru"
subject = "Приглашение!"

template = """Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!"""

friend_name = "Темирлан"
my_name = "Руслан"
website = ""

invitation = template.format(friend_name=friend_name, my_name=my_name, website=website)

email_headers = (
    "From: {}\n"
    "To: {}\n"
    "Subject: {}\n"
    "Content-Type: text/plain; charset=\"UTF-8\";\n"
).format(from_address, to_address, subject)

letter = "{}\n{}".format(email_headers, invitation)

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(email_login, email_password)
server.sendmail(from_address, to_address, letter.encode('utf-8'))
server.quit()
