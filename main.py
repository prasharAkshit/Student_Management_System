from Student_manage import Student_Management as SM
import time
sms = SM()

def main():
    while True:
        print("Wellcome to Student Management System.")
        print("1) Add Student")
        print("2) View Students")
        print("3) Search Students")
        print("4) Update Marks")
        print("5) Delete Students")
        print("6) Display Topper")
        user_choice = int(input("What operations would you like to do:"))

        if user_choice == 1:
            sms.add_student()
        elif user_choice == 2:
            sms.view_Student()
        elif user_choice == 3:
            sms.search_Student()
        elif user_choice == 4:
            sms.update_marks()
        elif user_choice == 5:
            sms.delete_Student()
        elif user_choice == 6:
            sms.display_topper()
        elif user_choice == 7:
            print("Closing...")
            time.sleep(3)
            return
        else:
            print("Invalid Operations...\nTry again...")

if __name__  == "__main__":
    main()
