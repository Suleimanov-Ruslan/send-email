import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_login =os.environ.get('LOGIN')
email_password =os.environ.get('TOKEN')

from_address = "RuslanSuleimonov@yandex.ru"
to_address = "RuslanSuleimonov@yandex.ru"
subject = "Приглашение!"

template = """Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

friend_name = "Темирлан"
my_name = "Руслан"
website = "https://dvmn.org/profession-ref-program/suleimanovrn/TTabC/"

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
print("Письмо успешно отправлено!")
server.quit()
