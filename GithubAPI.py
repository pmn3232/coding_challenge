import requests
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# GitHub API endpoint and authentication
base_url = 'https://api.github.com'
repo_owner = 'freeCodeCamp'
repo_name = 'freeCodeCamp'
github_token = 'your-token'

# Email configuration
smtp_server = 'smtp.office365.com'
smtp_port = 587
sender_email = 'your-email'
sender_password = 'your-password'
recipient_email = 'your-recipient-email'

# Date calculation for the last week
current_date = datetime.now()
week_ago = current_date - timedelta(days=7)
formatted_date = week_ago.strftime('%Y-%m-%dT%H:%M:%SZ')

# Retrieve pull requests from GitHub API
headers = {'Authorization': f'Token {github_token}'}
params = {
    'state': 'all',
    'sort': 'created',
    'direction': 'desc',
    'since': formatted_date
}
url = f'{base_url}/repos/{repo_owner}/{repo_name}/pulls'
response = requests.get(url, headers=headers, params=params)
pull_requests = response.json()

# Prepare summary message
summary = f"Summary of pull requests in the last week for {repo_owner}/{repo_name}:\n\n"
for pr in pull_requests:
    pr_title = pr['title']
    pr_state = pr['state']
    summary += f"Title: {pr_title}\nState: {pr_state}\n\n"

# Send email with summary
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = f"Pull Request Summary for {repo_owner}/{repo_name}"
msg.attach(MIMEText(summary, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
    
# Print on screen
# print(f"From: {sender_email}")
# print(f"To: {recipient_email}")
# print(f"Subject: Pull Request Summary for {repo_owner}/{repo_name}")
# print(f"Body:\n{summary}")

