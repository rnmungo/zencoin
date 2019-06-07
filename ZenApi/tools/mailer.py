from flask_mail import Message


class ZenMail:

    FIRM      = "Atte. Equipo de ZenCoin"
    LINEBREAK = "</br></br>"

    @classmethod
    def send_welcome_message(cls, mail, user):
        (subject, html) = ZenMail.get_welcome_message(user.full_name)
        message = Message(subject=subject, html=html, recipients=[user.email])
        mail.send(message)

    @classmethod
    def get_welcome_message(cls, name):
        subject = 'Bienvenido a ZenCoin'
        html    = "%s, queremos darle la bienvenida y agradecerle " % name
        html    += "por elegirnos para formar parte de ZenCoin. "
        html    += "En ZenCoin, podrá realizar transacciones, llevar el "
        html    += "registro de todos sus movimientos, ver cotizaciones "
        html    += "y mucho más!" + ZenMail.LINEBREAK
        html    += "Apurate, el mañana es hoy, ingresá y comenzá a operar "
        html    += "con tu cuenta!" + ZenMail.LINEBREAK
        html    += ZenMail.FIRM
        return subject, html

    @classmethod
    def send_transfer_message(cls, mail, origin, destiny, total):
        ZenMail.send_origin(mail, origin, destiny, total)
        ZenMail.send_destiny(mail, destiny, total)

    @classmethod
    def send_origin(cls, mail, origin, destiny, total):
        (subject, html) = ZenMail.get_origin_transfer_message(
                            origin.user['first_name'],
                            destiny.user['first_name'],
                            destiny.user['last_name'],
                            total)
        recipient = origin.user['email']
        message = Message(subject=subject, html=html, recipients=[recipient])
        mail.send(message)

    @classmethod
    def send_destiny(cls, mail, destiny, total):
        (subject, html) = ZenMail.get_destiny_transfer_message(
                            destiny.user['first_name'],
                            total)
        recipient = destiny.user['email']
        message = Message(subject=subject, html=html, recipients=[recipient])
        mail.send(message)

    @classmethod
    def get_origin_transfer_message(cls, from_name, to_name, to_last_name, total):
        subject = 'Aviso de Transferencia'
        html = "%s, enviaste %.7f ZenCoins " % (from_name, total)
        html += "a %s %s." % (to_name, to_last_name)
        html += ZenMail.LINEBREAK
        html += "Por favor, si ocurrió algún problema con esta transferencia "
        html += "no dudes en contactarnos."
        html += ZenMail.LINEBREAK
        html += ZenMail.FIRM
        return subject, html

    @classmethod
    def get_destiny_transfer_message(cls, name, total):
        subject = 'Aviso de Transferencia'
        html = "%s, se acreditaron en tu cuenta %.7f ZenCoins." % (name, total)
        html += ZenMail.LINEBREAK
        html += "Para ver tus últimos movimientos, "
        html += "date una vuelta por nuestra página."
        html += ZenMail.LINEBREAK
        html += ZenMail.FIRM
        return subject, html
