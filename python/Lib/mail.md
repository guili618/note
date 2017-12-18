### 

```python

>>> import smtplib
>>> mail = smtplib.SMTP('smtp.qq.com',587)
>>> mail
<smtplib.SMTP object at 0x0000000002F49F28>
>>> mail.ehlo()
(250, b'smtp.qq.com\nPIPELINING\nSIZE 73400320\nSTARTTLS\nAUTH LOGIN PLAIN\nAUTH=LOGIN\nMAILCOMPRESS\n8BITMIME')
>>> mail.starttls()
(220, b'Ready to start TLS')
>>> mail.login(r'example@qq.com','password')
(235, b'Authentication successful')
>>> type(mail)
<class 'smtplib.SMTP'>
>>> mail.quit()
(221, b'Bye')
>>> 
```

```python

>>> from imapclient import IMAPClient
>>> server = IMAPClient('imap.qq.com', use_uid=True)
>>> server.login('username','password')
b'Success login ok'
>>> import pprint
>>> pprint.pprint(mail.list_folers())
```