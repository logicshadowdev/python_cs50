import sys

MASTER_PIN = "****"

def access_vault(pin):
    if len(pin) != 4:
        raise ValueError("🚨 Security Alert: Pin must be exactly 4 digits")
    
    if not pin.isdigit():
        raise ValueError("⚠️ Security Alert: Pin must contain numbers only")

    if pin == MASTER_PIN:
        return "🔓 Access Granted. Welcome"
    else:
        return "❌ Access Denied. Intruder Alert"

def main():
    attempts = 3
    while attempts > 0:
        try:
            user_input = input("Enter Secret Vault PIN: ")
            result = access_vault(user_input)
            print(result)

            if "Granted" in result:
                return
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

        except ValueError as e:
            sys.exit(f"System Lockdown: {e}")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

    sys.exit("System Lockdown: Too many failed attempts.")

if __name__ == "__main__":
    main()