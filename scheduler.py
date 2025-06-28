# Initialize an empty list to store exam records
exams = []


# Function to create and add a new exam
def create_exam():
    # Prompt user for exam details
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")

    # Add exam details as a dictionary to the exams list
    exams.append({"name": name, "date": date, "time": time, "room": room})
    print("Exam added successfully.\n")


# Function to display all scheduled exams
def read_exams():
    if not exams:
        # If the list is empty, inform the user
        print("No exams scheduled.\n")
    else:
        # Loop through each exam and display its details
        for idx, exam in enumerate(exams, start=1):
            print(f"{idx}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
        print()  # Add a blank line for readability


# Function to update an existing exam
def update_exam():
    read_exams()  # Show current exams first
    if exams:
        try:
            # Ask user which exam they want to update
            choice = int(input("Enter exam number to update: ")) - 1
            if 0 <= choice < len(exams):
                # Allow user to update fields; keep old values if left blank
                print("Leave blank to keep current value.")
                name = input(f"New name ({exams[choice]['name']}): ") or exams[choice]['name']
                date = input(f"New date ({exams[choice]['date']}): ") or exams[choice]['date']
                time = input(f"New time ({exams[choice]['time']}): ") or exams[choice]['time']
                room = input(f"New room ({exams[choice]['room']}): ") or exams[choice]['room']

                # Update the selected exam
                exams[choice] = {"name": name, "date": date, "time": time, "room": room}
                print("Exam updated successfully.\n")
            else:
                print("Invalid selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


# Function to delete an exam
def delete_exam():
    read_exams()  # Show current exams first
    if exams:
        try:
            # Ask user which exam to delete
            choice = int(input("Enter exam number to delete: ")) - 1
            if 0 <= choice < len(exams):
                # Remove the selected exam from the list
                deleted = exams.pop(choice)
                print(f"Deleted exam: {deleted['name']}\n")
            else:
                print("Invalid selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


# Function to display the main menu and handle user input
def menu():
    while True:
        # Display menu options
        print("Exam Management System")
        print("1. Create Exam")
        print("2. View Exams")
        print("3. Update Exam")
        print("4. Delete Exam")
        print("5. Exit")

        # Get user input
        choice = input("Select an option (1-5): ")

        # Call the appropriate function based on user choice
        if choice == '1':
            create_exam()
        elif choice == '2':
            read_exams()
        elif choice == '3':
            update_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting program.")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.\n")


# Entry point of the program
if __name__ == "__main__":
    menu()

