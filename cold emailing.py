import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@gmail.com'  # Your email
sender_password = 'your_password'     # Your email password
recipient_email = 'publisher_email@example.com'  # Publisher's email
subject = 'Submission of My Novel'
message = """
Dear [Publisher's Name],

I hope this email finds you well. My name is [Your Name], and I am writing to inquire about the possibility of publishing my novel, titled "[Novel Title]". I believe my work aligns with your publishing interests, and I am excited to share more about it.

[Provide a brief introduction about yourself and your novel here]

I have attached the synopsis of my novel for your reference. If you are interested, I can provide the full manuscript for your review.

Thank you for considering my submission. I look forward to hearing from you. Please feel free to contact me at [Your Phone Number] or [Your Email Address] for any further information or discussion.

Sincerely,
[Your Name]
"""

# Create and send the email
try:
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the email server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print("An error occurred while sending the email:", str(e))
