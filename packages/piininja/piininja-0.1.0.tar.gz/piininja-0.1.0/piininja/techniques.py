import re
import numpy as np
import hashlib

def mask_email(email):
    """
    Mask email addresses
    john.doe@example.com -> j***@e*****.com
    """
    if not isinstance(email, str) or '@' not in email:
        return email
    
    parts = email.split('@')
    masked_username = parts[0][0] + '***' + parts[0][-1]
    masked_domain = parts[1][0] + '***' + parts[1][-1]
    return f"{masked_username}@{masked_domain}"

def mask_phone(phone):
    """
    Mask phone numbers
    1234567890 -> ***-***-4890
    """
    if not isinstance(phone, str):
        phone = str(phone)
    
    # Remove non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    if len(digits) < 4:
        return phone
    
    return f"***-***-{digits[-4:]}"

def generalize_age(age):
    """
    Convert specific ages to age ranges
    """
    try:
        age = int(age)
        if age < 18:
            return "0-17"
        elif age < 30:
            return "18-29"
        elif age < 45:
            return "30-44"
        elif age < 60:
            return "45-59"
        else:
            return "60+"
    except (ValueError, TypeError):
        return age

def tokenize_names(name):
    """
    Convert names to unique tokens
    """
    if not isinstance(name, str):
        return name
    
    # Use hash for consistent tokenization
    return hashlib.md5(name.encode()).hexdigest()[:10]

def add_noise_to_numeric(value, noise_level=0.05):
    """
    Add controlled noise to numeric values
    """
    try:
        # Convert to float
        numeric_value = float(value)
        
        # Generate noise
        noise = np.random.normal(0, numeric_value * noise_level)
        
        return round(numeric_value + noise, 2)
    except (ValueError, TypeError):
        return value
    

def tokenize_name(name):
    # Replace actual names with unique tokens
    name_mapping = {}
    def get_token(original_name):
        if original_name not in name_mapping:
            name_mapping[original_name] = f"Person_{len(name_mapping) + 1}"
        return name_mapping[original_name]
    return get_token(name)