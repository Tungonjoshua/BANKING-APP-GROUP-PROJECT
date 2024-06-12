from subprocess import call


def welcome():
    call(["python", "welcome screen.py"])


def main():
    print("Login to TUNGON BANK ng")

    phone_number = input("Enter Your Phone Number: ")
    password = input("Enter Your Password: ")

    # Placeholder for actual authentication logic
    print("Authenticating...")

    # If authentication is successful, call the welcome screen
    welcome()


if __name__ == "__main__":
    main()
