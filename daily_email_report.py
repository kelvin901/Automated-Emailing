import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    sender_email = "kelvinnyoike398@gmail.com"
    receiver_email = "wawerukelvin2019@gmail.com"
    password = "vic657yack"
    subject = "Daily Report"
    message = """
    Write your report here.
    This is a sample report.
    """

    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Create SMTP session for sending the mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change to your SMTP server
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully!')
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the job to run daily at a specific time
schedule.every().day.at("08:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
