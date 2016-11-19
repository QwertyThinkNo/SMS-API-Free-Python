# API for Free SMS using Python
 A piece of code to send an SMS to your mobile phone using the Free SMS API service.
 This example use Urllib3, so it's work fine with Python 3.

## Why use Free API ?

 You can use this API to notify you of an error, a news item or a notification. The possibilities are endless
 
## How to use Free API ?

 The API relies on a URL with this information in: the identification key, the user number and the message (with percent-encoding).
 
 To find your owns keys, go to your [Free account](https://mobile.free.fr/moncompte/) and enter your credentials to log in. (If you use your smartphone with data activated to connect to log into your accont, you will be automatically logged in.)
 
 Click on "manage your options" and search "SMS Notifications" option. If the option is disabled, click on "activated". Find and copy "Hello World !" link (like https://smsapi.free-mobile.fr/sendmsg?user=**12345678**&pass=**usb42qe7g2n8r**&msg=**Hello%20World%20!**.)
 
 For my example, I have **12345678** as user number, **usb42qe7g2n8r** as authentication key and **Hello%20World%20!** (Hello world) as message.
 
 Now, for use Python script, I have to inform **12345678** in USER_NUMBER variable, **usb42qe7g2n8r** in USER_KEY and your message in MSG. MSG will be a simple string (not in percent-encoding) because we use the POST method, that encodes the message for us.
 
 Now you can integrate this piece of code to send you SMS notifications. It is not amazing ?
 
### Things not so important
 
 The script has a conditional structure to perform actions based on how it sent the SMS. (If it was successfully sent (200) or with errors (400 < 500)). You can remove this part safely or add actions.
 
