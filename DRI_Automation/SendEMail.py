import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, data):
        message = MIMEMultipart()
        message["Subject"] = "DRI Bundle Status"
        message["From"] = "p.garg@dell.com"
        message["To"] = "prankur.garg1@emc.com"
        modified_html = f"""
                <html><body><p>Hello, Friend.</p>
                <p>Below is the list of unreserved bundles. We will be reserving them now</p>
                {data}
                <p>Regards,</p>
                <p>Prankur Garg</p>
                <p>For any issues with automation script, please contact p.garg@dell.com </p>
                </body></html>
                """
        message.attach(MIMEText(modified_html, "html"))
        msg_body = message.as_string()
        sender = "p.garg@dell.com"
        receiver = "prankur.garg1@emc.com"
# Send the message via our own SMTP server.
        server = smtplib.SMTP('mailhub.emc.com')
        server.starttls()
        server.sendmail(sender, receiver, msg_body)
        server.quit()



