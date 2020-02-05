# Module for sending an email to your phone when code is done

## Note this only works with gmail, I highly recommend creating a 'burner' g-mail account as this will require reduced security measures on the account to send emails 
## Change settings at https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none to yes

### Example
    from Send_Email_To_Phone.Send_Email_Module import Send_Email_Class
    
    email_class_object = Send_Email_Class('email@gmail.com', 'password')
    email_class_object.set_outbound_email('phonenumber@vtext.com')

    try:
        for i in range(10):
            print(i)
        email_class_object.send_email('Finished!')
    except:
        email_class_object.send_email('Failed!')
