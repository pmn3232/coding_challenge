Python code that utilizes the GitHub API to retrieve a summary of opened, closed, and draft pull requests from a specified repository within the last week and sends the summary via email using the smtplib library.

Prerequisites:

Before executing the code, ensure that you have the necessary libraries installed, such as requests, smtplib, and email. 
```
pip install requests
```
Also, enable "Less Secure Apps" in your sender email account settings if using Gmail as the SMTP server.


Make sure to replace the placeholders with your own GitHub token, repository details, email credentials, and recipient email address:
```python
# GitHub API endpoint and authentication
base_url = 'https://api.github.com'
repo_owner = 'freeCodeCamp'
repo_name = 'freeCodeCamp'
github_token = 'your-token'

# Send email with summary
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = f"Pull Request Summary for {repo_owner}/{repo_name}"
msg.attach(MIMEText(summary, 'plain'))
```

If you don't want to send an email, you can comment the email sending section and simply print the details of the email that would be sent, like so:

```python
# Print on screen
print(f"From: {sender_email}")
print(f"To: {recipient_email}")
print(f"Subject: Pull Request Summary for {repo_owner}/{repo_name}")
print(f"Body:\n{summary}")
```

Remember to replace the placeholder values with your own repository details, email credentials, and recipient email address.


Sample Output: Printing the email summary on screen

```
❯ python3 GithubAPI.py
From: 13934@anoffice.vip
To: pmn3232@gmail.com
Subject: Pull Request Summary for freeCodeCamp/freeCodeCamp
Body:
Summary of pull requests in the last week for freeCodeCamp/freeCodeCamp:

Title: chore(deps) upgrade eslint
State: open

Title: chore(deps): update required pnpm version
State: open

Title: chore(deps): update dependency webpack to v5.85.0
State: closed

Title: chore(deps): update dependency dotenv to v16.1.4
State: closed

Title: chore(deps): update dependency @types/node to v18.16.16
State: closed

Title: fix(deps): update prisma monorepo to v4.15.0
State: closed

Title: fix(deps): update dependency @stripe/stripe-js to v1.54.0
State: closed

Title: chore(deps): update dependency webpack-bundle-analyzer to v4.9.0
State: closed

Title: chore(deps): update dependency mongodb to v5.6.0
State: closed

Title: chore(deps): update dependency markdownlint to v0.29.0
State: open

Title: chore(deps): update dependency eslint to v8
State: open

Title: fix(deps): update dependency @headlessui/react to v1.7.15
State: closed

Title: fix: removed extra blank link between sections
State: closed

Title: chore(deps): update dependency @types/jest to v29.5.2
State: closed

Title: chore(deps): update babel monorepo
State: closed

Title: chore(deps): update github/codeql-action digest to 83f0fe6
State: closed

Title: chore(deps): replace dependency babel-eslint with @babel/eslint-parser ^7.11.0
State: open

Title: Update 5dc24614f86c76b9248c6ebd.md
State: closed

Title: fix: removed extra blank link between sections
State: closed

Title: chore(i18n,learn): processed translations
State: closed

Title: chore(i18n,client): processed translations
State: closed

Title: chore(i18n,docs): processed translations
State: closed

Title: Resolve #50578
State: closed

Title: Resolve  #50311, book recommendation
State: closed

Title: Resolve  #50311, book recommendation
State: closed

Title: fix: removed extra blank space between lines
State: closed

Title: chore(i18n,learn): processed translations
State: closed

Title: chore(i18n,docs): processed translations
State: closed

Title: Test
State: closed

Title: fix(curriculum) require creating store
State: closed
```
