import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, data):
        message = MIMEMultipart()
        message["Subject"] = "Epack Staus"
        message["From"] = "p.garg@dell.com"
        to_addresses = ["prankur.garg1@emc.com", "Ravi.Bhat@Dell.com", "PavitraH.Gadagi@dell.com", "Swarajya.K.Parida@Dell.com", "Suhas.Sathyanarayana@Dell.com"]
        message['To'] = ','.join(to_addresses)
        modified_html = f""" <html><body><p>Hi Team,.</p> 
        <p>Please find below list of Epacks/Pre Epacks which are in assigned state. For 
        any issues with automation script, please contact p.garg@dell.com</p> 
                {data} 
                <p>Regards,</p>
                <p>Prankur Garg</p>
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



