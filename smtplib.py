import smtplib
from email.mime.text import MIMEText

# إعداد الرسالة
msg = MIMEText("Hello from Python!")
msg["Subject"] = "Reminder"
msg["From"] = "you@gmail.com"
msg["To"] = "friend@gmail.com"

# إرسال عبر Gmail SMTP
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@gmail.com", "your_app_password_here")  # استخدم App Password
    server.send_message(msg)

print("✅ Email sent successfully!")

