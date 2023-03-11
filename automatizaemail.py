import yagmail

# Credenciais do remetente
email_de = 'alanmunozmartins@gmail.com'
senha = 'Alan.jade4'

# Configuração do e-mail
destinatario = 'equipealanmartins@gmail.com'
assunto = 'Assunto do e-mail'
corpo = 'Conteúdo do e-mail'

# Conexão com o servidor de e-mail do Gmail
yag = yagmail.SMTP(email_de, senha)

# Envio do e-mail
yag.send(to=destinatario, subject=assunto, contents=corpo)

# Encerramento da conexão com o servidor de e-mail
yag.close()