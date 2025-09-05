def validate_email (email):
    email = email.strip()
    if not "@" in email or not "." in email:
        return False
    
    username, domain = email.split("@")
    if len(username) == 0 or len(domain) == 0:
        return 