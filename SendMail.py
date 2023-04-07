import smtplib
from email.message import EmailMessage
import random

class gmail_sender:
    def __init__ (self, sender_email, receiver_email, sender_password, cc_email="", bcc_email=""):
        self.s_email = sender_email
        self.r_email = receiver_email
        self.pw = sender_password
        self.server_name = "smtp.gmail.com"
        # smtp서버의 포트번호
        # 465 : SSL암호화를 사용하는 포트번호
        # 587 : TLS암호화를 사용하는 포트번호
        # 암호화 수준은 SSL < TLS 이기에 TLS암호화 포트 사용
        self.server_port = 587

        # 객체 생성
        self.msg = EmailMessage()
        # 발신자 및 수신자 설정
        self.msg["From"] = self.s_email
        self.msg['To'] = self.r_email

        # 부가 발신자들은 있으면 보내고 없으면 무시
        if cc_email != "":
            self.cc_email = cc_email
            self.msg["Cc"] = self.cc_email
        if bcc_email != "":
            self.bcc_email = bcc_email
            self.msg['Bcc'] = self.bcc_email
        
        # 서버 이름과 포트번호 설정
        self.smtp = smtplib.SMTP(self.server_name, self.server_port)

    # 메세지 세팅(제목, 본문)
    def msg_set(self, msg_title, msg_body):
        self.msg['Subject'] = msg_title
        self.msg.set_content(msg_body)

    def smtp_connect_send(self):
        # 연결 확인
        self.smtp.ehlo()
        # TLS 활성화
        self.smtp.starttls()
        # 서버 로그인
        self.smtp.login(self.s_email, self.pw)
        # 세팅한 메세지 전송
        self.smtp.send_message(self.msg)

    # 연결 종료
    def smtp_disconnect(self):
        self.smtp.close()