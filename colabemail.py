import smtplib
import email.message

def enviar_email():
  corpo_email = """

https://github.com/alanmmartins
  teste teste 

"""
  msg = email.message.Message()
  msg['Subject'] = "meu git"
  msg['From'] = 'alanmunozmartins@gmail.com'
  msg['To'] = 'ricardoorrico@gmail.com'
  password = "dmsinbbqvhoclbif"
  msg.add_header('content-Type','text/html')
  msg.set_payload(corpo_email)

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()

  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print('email enviado')

enviar_email()  