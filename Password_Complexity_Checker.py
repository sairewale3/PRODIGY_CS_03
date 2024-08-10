import re

def assess_password_strength(password):
    criteria = {
        'length': len(password) >= 15,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'number': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    score = sum(criteria.values())
    feedback = [
        "Password should be at least 8 characters long." if not criteria['length'] else "",
        "Password should contain at least one uppercase letter." if not criteria['uppercase'] else "",
        "Password should contain at least one lowercase letter." if not criteria['lowercase'] else "",
        "Password should contain at least one number." if not criteria['number'] else "",
        "Password should contain at least one special character." if not criteria['special'] else ""
    ]

    feedback = [line for line in feedback if line]
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_level = strength_levels[score]

    return strength_level, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    level, feedback = assess_password_strength(password)
    print(f"Password Strength: {level}")
    if feedback:
        print("Feedback:")
        for line in feedback:
            print(f"- {line}")
