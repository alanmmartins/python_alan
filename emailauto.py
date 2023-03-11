import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credenciais do remetente
email_de = 'alanmunozmartins@gmail.com'
senha = 'Alan.jade4'

# Configuração do e-mail
msg = MIMEMultipart()
msg['From'] = 'alanmunozmartins@gmail.com'
msg['To'] = 'equipealanmartins@gmail.com'
msg['Subject'] = 'Assunto do e-mail'

# Corpo da mensagem
mensagem = 'Conteúdo do e-mail'
msg.attach(MIMEText(mensagem, 'plain'))

# Conexão com o servidor de e-mail do Gmail
server = smtplib.SMTP('.gmail.com', 587)
server.starttls()
server.login(email_de, senha)

# Envio do e-mail
texto = msg.as_string()
server.sendmail(email_de, msg['To'], texto)

# Encerramento da conexão com o servidor de e-mail
server.quit()