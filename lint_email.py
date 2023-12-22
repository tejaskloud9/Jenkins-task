import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_latest_commit_author():
    result = subprocess.run(["git", "log", "-1", "--pretty=format:%an <%ae>"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def lint_code():
    result = subprocess.run(["flake8", "--exclude=venv", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode, result.stdout, result.stderr

def send_email(to_email, subject, body):
    sender_email = os.environ.get("SMTP_USERNAME")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_password = os.environ.get("SMTP_PASSWORD")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, to_email, message.as_string())

if __name__ == "__main__":
    # Get the author of the latest commit
    author_info = get_latest_commit_author()

    # Run linting
    return_code, lint_output, lint_error = lint_code()

    if return_code != 0:
        # Lint validation failed, send an email to the author of the latest commit
        subject = "Lint Validation Failure"
        body = f"Lint validation failed with the following errors:\n\n{lint_output}\n{lint_error}"

        send_email(author_info, subject, body)
        print("Lint validation failed. Email notification sent to the developer.")
        exit(78)
    else:
        print("Lint validation passed. Code is ready for push.")
        exit(0)
