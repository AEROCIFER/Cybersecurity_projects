import re

def password_checker(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(criteria.values())
    strength = "Strong" if score == 5 else "Weak"
    feedback = []
    if not criteria["length"]:
        feedback.append("Password is Less than 8 characters.")
    if not criteria["uppercase"]:
        feedback.append("Password must contain atleast one uppercase character.")
    if not criteria["lowercase"]:
        feedback.append("Password must contain atleast one lowercase character.")
    if not criteria["digit"]:
        feedback.append("Password must contain atleast one digit.")
    if not criteria["special"]:
        feedback.append("Password must contain atleast one speacial character.")


    return strength, feedback

def main():
    print("Passowrd Complexity checker")
    password = input("Enter your password: ").strip()
    strength , feedback= password_checker(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Issues with your password:")
        for issue in feedback:
            print(f"- {issue}")


if __name__ == "__main__":
    main()