from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import sys
from PyQt5.uic import loadUi
import smtplib,ssl

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        loadUi("Email_Sender_UI.ui",self)
        self.send.clicked.connect(self.send_email)
    def send_email(self):
        recepient = self.recp_line.text()
        email = self.body.toPlainText()
        print(recepient,email)
        port = 465
        smtp_server = "smtp.gmail.com"
        sender="fasghar40@gmail.com"
        password = "wyqkrhafuaabdvub"
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server,port,context=context) as smtp:
                smtp.login(sender,password)
                smtp.sendmail(sender,recepient,email)
                QMessageBox.information(self,"Status","Your Email Has Been Sent!",QMessageBox.Ok)
            
        except:
                QMessageBox.information(self,"Status","Your Email is not sent!",QMessageBox.Ok)
def window():
    app = QApplication(sys.argv)
    win = my_app()
    win.setWindowTitle("Email Sender")
    win.show()
    sys.exit(app.exec_())
window() 