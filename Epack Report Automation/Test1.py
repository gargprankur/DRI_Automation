import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from pretty_html_table import build_table


class DataGeneration():
    def __init__(self):
        dict_1 = {}
        dict_1["Numbers"] = [1,2,3]
        dict_1["Status"] = ["Avaialble"]*3
        data_frame = pd.DataFrame(dict_1)
        print(data_frame)
        data = build_table(data_frame, "blue_light")
        SendEmail(data)

class SendEmail:
    def __init__(self, data):
        message = MIMEMultipart()
        message["Subject"] = "DRI Bundle Status"
        message["From"] = "p.garg@dell.com"
        message["To"] = "prankur.garg1@emc.com"
        body = "This is the text"
        modified_html = f"""
        <html><body><p>Hello, Friend.</p>
        <p>Here is your data:</p>
        {data}
        <p>Regards,</p>
        <p>Me</p>
        </body></html>
        """
        message.attach(MIMEText(modified_html, "html"))
        #message.attach(MIMEText(data, "html"))
        msg = message.as_string()

# Send the message via our own SMTP server.
        server = smtplib.SMTP('mailhub.emc.com')
        server.starttls()
        server.sendmail(message["From"], message["To"],  msg)
        server.quit()

        MIMEMultipart()

data_generation = DataGeneration()


