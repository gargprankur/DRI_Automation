import os
import time
import schedule

def run_automation():
    os.system('C:\\Users\\gargp6\\PycharmProjects\\Selenium_Testing\\Epack Report Automation\\Selenium\\Scripts\\activate')
    os.system('cd C:\\Users\\gargp6\\PycharmProjects\\Selenium_Testing\\Epack Report Automation')
    os.system('python EpackReportMain.py')


schedule.every().day.at("22:05").do(run_automation)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute


