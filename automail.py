import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("your email", "your password")

# sent the mail
yag.send(
    to='jaswinders.ic.18@nitj.ac.in',
    subject=sub, # email subject
    contents='Please find the attachments',  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
