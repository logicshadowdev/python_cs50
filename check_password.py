passwords = input("Enter Password: ")

def check_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    length = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_special, length])
    
    print(f"Password: {password}")
    print(f"{'✅'if length else '❌'} At least 8 characters")
    print(f"{'✅'if has_upper else '❌'} Uppercase letter")
    print(f"{'✅'if has_lower else '❌'} Lowercase letter")
    print(f"{'✅'if has_digit else '❌'} Special character")
    
    if score == 5:
        print("Strong Password")
    elif score >= 3:
        print("Medium Password")
    else:
        print("Weak Password")

check_password(passwords)
print("-" * 30)