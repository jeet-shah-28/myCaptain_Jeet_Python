import csv

def storing_info(info_list):
    with open('student_info.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact", "Email-ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    studentNo = 1

    while condition:
        student_info = input(f"\nEnter student information for student #{studentNo} in the following format(Name, Age, Contact No, Email ID) : \n")
        details_list = student_info.split(', ')
        print(f"\n{'='*8}Student #{studentNo} details{'='*8} \nName : {details_list[0]}\nAge : {details_list[1]}\nContact number : {details_list[2]}\nEmail-ID : {details_list[3]}\n")
        choice_check = input("Is the entered information correct ? (YES/NO) : ").upper()
        if choice_check == "YES":
            storing_info(details_list)
            condition_check = input("\nDo you want to enter information for another student? (YES/NO) : ").upper()
            if condition_check == "YES":
                condition = True
                studentNo += 1
            elif condition_check == "NO":
                condition = False
        elif choice_check == "NO":
            print("Please re-enter the values!")