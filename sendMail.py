import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Outlook email and password
writer_email = "brian_anderson@unch.unc.edu"
receiver_email = "brian_anderson@med.unc.edu"
# outlook_email = "mdance@ad.unc.edu"
msg = MIMEText("A test of automated emails")


msg['Subject'] = "test3"
msg['From'] = writer_email
msg['To'] = receiver_email

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.unch.unc.edu')
s.sendmail(writer_email, [receiver_email], msg.as_string())
s.quit()
