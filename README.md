Python code that utilizes the GitHub API to retrieve a summary of opened, closed, and draft pull requests from a specified repository within the last week and sends the summary via email using the smtplib library.
Make sure to replace the placeholders with your own GitHub token, repository details, email credentials, and recipient email address:

Before executing the code, ensure that you have the necessary libraries installed, such as requests, smtplib, and email. Also, enable "Less Secure Apps" in your sender email account settings if using Gmail as the SMTP server.
Example: pip install requests

If you don't want to send an email, you can comment the email sending section and simply print the details of the email that would be sent, like so:

print(f"From: {sender_email}")
print(f"To: {recipient_email}")
print(f"Subject: Pull Request Summary for {repo_owner}/{repo_name}")
print(f"Body:\n{summary}")

Remember to replace the placeholder values with your own repository details, email credentials, and recipient email address.
