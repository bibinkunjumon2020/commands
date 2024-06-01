"""
This method generate a unique id for each application.
"""
def generate_application_id():
    timestamp = int(time.time()) % 100000
    random_number = random.randint(100, 999)
    application_id = f"{timestamp}{random_number}"
    # Convert the application ID to uppercase and replace any non-alphanumeric characters with an empty string
    application_id = "".join(c for c in application_id if c.isalnum()).upper()
    return application_id
"""