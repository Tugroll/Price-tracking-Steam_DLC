from soup import SoupManager
from mail_manager import MailManager


sp = SoupManager()
mail_mng = MailManager()

sp.get_price()
mail_mng.sending_mail(sp.check_price())



