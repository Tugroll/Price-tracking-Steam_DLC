import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_MAIL = os.getenv("SMTP_ADDRESS")
TO_MAIL = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


class MailManager:




    def sending_mail(self, price_lower):

           if price_lower:
               print("BUYYYY")
               with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                   connection.starttls()
                   connection.login(MY_MAIL, EMAIL_PASSWORD)
                   connection.sendmail(from_addr=MY_MAIL, to_addrs=TO_MAIL,
                                       msg=f"The Price is lower than 100$. Hurry up!")

