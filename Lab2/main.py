import click
from Model.Office import Office
from Services.OfficeService import OfficeService


def print_main_menu():
    click.clear()
    print("1. Create office\n")
    print("2. Print offices\n")
    print("3. delete office\n")
    print("4. Exit")
    choice = input("Selected operation: ")
    return choice


def print_create_office_menu():
    office_service = OfficeService()
    name = input("Please enter name")
    new_office = Office(name)
    office_service.create_office(new_office)


def delete_office():
    office_service = OfficeService()
    office_id = input("Please enter office id")
    office_service.remove_office(office_id)


def print_offices():
    office_services = OfficeService()
    offices = office_services.get_offices()
    print(offices)

    for office in offices:
        print(f"Office id: {office[0]}\n")
        print(f"Office name: {office[1]}\n")
        print("=========================\n")


def main():
    while True:
        choice = print_main_menu()
        if choice == "1":
            print_create_office_menu()
        elif choice == "2":
            print_offices()
        elif choice == "3":
            delete_office()
            print_main_menu()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("please enter valid choice")


main()
