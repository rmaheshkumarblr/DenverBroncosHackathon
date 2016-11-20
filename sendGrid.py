import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("rmaheshkumarblr@gmail.com")
to_email = Email("mara0940@colorado.edu")
subject = "Sending with SendGrid is Fun"
content = Content("text/HTML", "<table><thead><tr>Question</tr><tr>Answer</tr></thead></table> and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

