__author__ = 'Brian M Anderson'
# Created on 2/5/2020

import smtplib, ssl


class Send_Email_Class(object):
    def __init__(self, email_address, password, port=465):
        # Create a secure SSL context
        self.port = port
        self.email_address = email_address
        self.password = password
        self.context = ssl.create_default_context()
        self.login()

    def set_outbound_email(self, email_address):
        self.outbound_email = email_address

    def login(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context)
        self.server.login(self.email_address, self.password)

    def send_email(self, message,outbound_email=None):
        self.login()  # Login each time in case you have timeout issues
        if outbound_email is None:
            outbound_email = self.outbound_email
        self.server.sendmail(self.email_address,outbound_email,message)


def main():
    pass


if __name__ == '__main__':
    main()

    # email_class_object = Send_Email_Class('email@gmail.com', 'password')
    # email_class_object.set_outbound_email('phonenumber@vtext.com')
    #
    # try:
    #     for i in range(10):
    #         print(i)
    #     email_class_object.send_email('Finished!')
    # except:
    #     email_class_object.send_email('Failed!')