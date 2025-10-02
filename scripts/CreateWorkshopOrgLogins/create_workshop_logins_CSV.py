import csv

help_me_create_workshop_csv = input("Would you like help creating the CSV for your workshop orgs? Please enter 'Y' or 'N': ").lower()

if help_me_create_workshop_csv == 'y':
    data = []
    nbr_orgs = int(input("How many orgs do you need to create?: "))
    creator_email = input("What is your email address? ")
    domain = input("What domain should be used to create the user logins? ")
    csv_file = f"/users/msardello/desktop/{domain}.csv"
    user_number = 1
    for user in range(1, nbr_orgs):
        if user < 10:
            login = f"0{user_number}"
        else:
            login = user_number
        user_number += 1
        row = [f"user{login}@{domain}.org, {creator_email}"]
        data.append(row)
    with open(csv_file, mode="w", newline="") as file:
        for row in data:
            file.write(",".join(map(str, row)) + "\n")

    print(f"Data successfully written to {csv_file}")

else:
    print("OK, thank you. See you next time!")
