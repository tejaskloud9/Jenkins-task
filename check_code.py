import subprocess
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender_email = "tejas.g@kloud9.nyc"  # Replace with your email address
    receiver_email = "tejas.g@kloud9.nyc"  # Replace with the developer's email address
    smtp_server = "smtp.example.com"  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port
    smtp_username = "your_smtp_username"  # Replace with your SMTP username
    smtp_password = "your_smtp_password"  # Replace with your SMTP password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body_text = MIMEText(body)
    msg.attach(body_text)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def check_syntax_and_indentation(files):
    # Run Flake8 to check syntax and indentation
    result = subprocess.run(["flake8", "--exit-zero"] + files, capture_output=True, text=True)

    return result.returncode, result.stdout

def main():
    # Get list of modified or staged files using GIT
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)

    # Split the list of files into a Python list
    files = result.stdout.strip().splitlines()

    if not files:
        print("No files to check. Exiting.")
        sys.exit(0)

    # check Syntax and Indentation for the modified or staged files
    returncode, output = check_syntax_and_indentation(files)

    if returncode != 0:
        error_message = "Errors found. Blocking the commit.\n" + output
        print(error_message)

        # send email notification to the Developer
        email_subject = "Code Validation Errors"
        send_email(email_subject, error_message)

        # exit with a non-zero status code to prevent the commit
        sys.exit(1)
    else:
        print("No syntax or indentation errors found. Committing.")

if __name__ == "__main__":
    main()
