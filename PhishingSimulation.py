import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'naveen072005123@gmail.com'
sender_password = 'fzilhkarjkujhdop'  # Use an app password if 2FA is enabled

subject = 'Important Account Verification'

# Recipient email addresses and names
recipients = [{'email': 'workwithnaveen7@gmail.com', 'name': 'Naveen'}]

# Connect to the server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    for recipient in recipients:
        recipient_email = recipient['email']
        recipient_name = recipient['name']
        
        message = MIMEMultipart('alternative')
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Personalize the email body
        email_content = f"""
        <html>
        <body>
            <p>Hello {recipient_name},</p>
            <p>We have detected some unusual activity in your account and require your assistance to ensure its security. Please verify your account by clicking the link below:</p>
            <p><a href="https://workwithnaveen7.github.io/Phishy-LoginPage/" style="color: #007BFF; text-decoration: none; font-weight: bold;">Verify Your Account</a></p>
            <p>If you did not request this action, please disregard this email. Your security is our priority.</p>
            <p>Thank you,<br>The IT Support Team</p>
            <p><small>For any questions, please contact us</small></p>
        </body>
        </html>
        """
        message.attach(MIMEText(email_content, 'html'))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent successfully to {recipient_name} ({recipient_email})")

    server.quit()
except Exception as e:
    print(f"Failed to send email: {str(e)}")
