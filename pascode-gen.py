import random

def generate_passcode():
    passcode = ""
    for _ in range(12):
        passcode += str(random.randint(0, 9))
    return passcode

# Function to save passcodes to a file
def save_passcodes(passcodes):
    with open("passcodes.txt", "a") as file:
        for passcode in passcodes:
            file.write(passcode + "\n")
    print("Passcodes saved successfully.")

# Generate passcodes
passcodes = [generate_passcode() for _ in range(2)]

print("Generated Passcodes:")
for i, passcode in enumerate(passcodes, 1):
    print(f"Passcode {i}: {passcode}")

save_more = input("Do you want to generate and save more passcodes? (yes/no): ")

while save_more.lower() == 'yes':
    num_passcodes = int(input("How many more passcodes do you want to generate and save? "))
    new_passcodes = [generate_passcode() for _ in range(num_passcodes)]
    passcodes.extend(new_passcodes)
    print("Generated Passcodes:")
    for i, passcode in enumerate(new_passcodes, len(passcodes) - num_passcodes + 1):
        print(f"Passcode {i}: {passcode}")
    save_more = input("Do you want to generate and save more passcodes? (yes/no): ")

# Save passcodes to file
save_passcodes(passcodes)

