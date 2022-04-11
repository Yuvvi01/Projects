from email_validator import validate_email, EmailNotValidError

email = str(input("Enter email: "))

try:
  # Validate.
  valid = validate_email(email)
  print("Valid email.")


  # Update with the normalized form.
  email = valid.email
except EmailNotValidError as e:
  print("Invalid email.")
    
  # email is not valid, exception message is human-readable
  print(str(e))