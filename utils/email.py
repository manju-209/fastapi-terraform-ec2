import re
import smtplib 
import dns.resolver

def email_notexist(email):
    try:
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        server = smtplib.SMTP(timeout=5)
        server.connect(mx_record)
        server.helo(server.local_hostname) 
        server.mail('check@example.com')
        code, message = server.rcpt(email)
        server.quit()
        return code == 250 
    except Exception:
        return False

def validate_email(email):
    if not email_notexist(email):
        return False, "Invalid Email Address"
    return True , "Valid Email"

