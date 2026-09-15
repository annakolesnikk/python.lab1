from employee_manager.models import Employee
from employee_manager.services import (
    calculate_average_salary,
    calculate_total_payroll,
    filter_by_department,
    find_highest_paid_employee,
)


def create_demo_employees() -> list[Employee]:

    return [
        Employee(
            name="Anna Kolesnik",
            position="Manager",
            department="Sales",
            salary=1200.0,
        ),
        Employee(
            name="Oleh Ivanenko",
            position="Developer",
            department="IT",
            salary=2500.0,
        ),
        Employee(
            name="Iryna Petrenko",
            position="Accountant",
            department="Finance",
            salary=1800.0,
        ),
        Employee(
            name="Andrii Shevchenko",
            position="Designer",
            department="IT",
            salary=2000.0,
        ),
        Employee(
            name="Olena Kovalenko",
            position="Sales Representative",
            department="Sales",
            salary=1100.0,
        ),
    ]


def print_employees(
    employees: list[Employee],
) -> None:

    print("\nEmployees:")

    for employee in employees:
        print(
            f"{employee.name:20}"
            f"{employee.position:22}"
            f"{employee.department:12}"
            f"{employee.salary:10.2f}"
        )


def main() -> None:

    employees = create_demo_employees()

    print_employees(employees)

    department = "IT"

    department_employees = filter_by_department(
        employees,
        department,
    )

    print(
        f"\nEmployees in department {department}:"
    )

    print_employees(department_employees)

    average = calculate_average_salary(
        employees,
    )

    print(
        f"\nAverage salary (all employees): {average:.2f}"
    )

    best_paid = find_highest_paid_employee(employees)

    if best_paid is not None:
        print(
            "\nHighest paid employee:",
            best_paid.name,
            f"({best_paid.salary:.2f})",
        )

    total_payroll = calculate_total_payroll(
        employees,
    )

    print(
        f"\nTotal payroll fund: {total_payroll:.2f}"
    )


if __name__ == "__main__":
    main()