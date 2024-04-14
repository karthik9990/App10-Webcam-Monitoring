import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "hrus dzjr qboa lamk"
EMAIL_SENDER = "karthik.tadakapalli@gmail.com"
RECEIVER = "karthik.tadakapalli@gmail.com"


def send_email(image_path):
    print("send_email function started")
    emai_message = EmailMessage()
    emai_message["Subject"] = "New Customer Showed up!"
    emai_message.set_content("Hey, We just saw someone on the camera!")

    with open(image_path, "rb") as file:
        content = file.read()
    emai_message.add_attachment(content, maintype="image",
                                subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_SENDER, PASSWORD)
    gmail.sendmail(EMAIL_SENDER, RECEIVER, emai_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
