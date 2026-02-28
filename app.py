from email_generator import generate_email
print("=== Email Communication Assistant ===")

context = input("Enter email context:\n")
tone = input("Enter tone (formal/informal): ")

result = generate_email(context, tone)

print("\n--- Generated Output ---\n")
print(result)
