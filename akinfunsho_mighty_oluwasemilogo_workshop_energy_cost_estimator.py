
# WORKSHOP ENERGY COST ESTIMATOR

# Function to calculate energy consumption in kWh
def calculate_energy(power, hours):
    energy = (power * hours) / 1000
    return energy


# Function to calculate electricity cost
def calculate_cost(energy, tariff):
    cost = energy * tariff
    return cost


# List to store machine information
machines = []

# Get electricity tariff from the user
try:
    tariff = float(input("Enter electricity tariff per kWh (N): "))

    if tariff <= 0:
        print("Error: Tariff must be greater than zero.")

    else:
        # Ask for the number of machines
        number = int(input("Enter number of machines: "))

        if number <= 0:
            print("Error: Enter at least one machine.")

        else:
            # Loop through each machine
            for i in range(number):
                print("\nMachine", i + 1)

                name = input("Enter machine name: ")

                power = float(input("Enter power in watts: "))
                hours = float(input("Enter hours used per day: "))

                # Validate machine information
                if power <= 0 or hours < 0 or hours > 24:
                    print("Invalid power or operating hours.")
                    continue

                else:
                    # Calculate daily energy
                    daily_energy = calculate_energy(power, hours)

                    # Calculate monthly energy (30 days)
                    monthly_energy = daily_energy * 30

                    # Calculate daily and monthly cost
                    daily_cost = calculate_cost(daily_energy, tariff)
                    monthly_cost = calculate_cost(monthly_energy, tariff)

                    # Store machine details in the list
                    machines.append([
                        name,
                        daily_energy,
                        monthly_energy,
                        daily_cost,
                        monthly_cost
                    ])

            # Display the results
            print("\n========== WORKSHOP ENERGY REPORT ==========")

            if len(machines) == 0:
                print("No valid machine information was entered.")

            else:
                total_daily = 0
                total_monthly = 0
                total_daily_cost = 0
                total_monthly_cost = 0

                for machine in machines:
                    print("\nMachine:", machine[0])
                    print("Daily Energy:", round(machine[1], 2), "kWh")
                    print("Monthly Energy:", round(machine[2], 2), "kWh")
                    print("Daily Cost: N", round(machine[3], 2))
                    print("Monthly Cost: N", round(machine[4], 2))

                    # Add machine values to the totals
                    total_daily += machine[1]
                    total_monthly += machine[2]
                    total_daily_cost += machine[3]
                    total_monthly_cost += machine[4]

                # Display total workshop consumption and cost
                print("\n========== TOTAL SUMMARY ==========")
                print("Total Daily Energy:", round(total_daily, 2), "kWh")
                print("Total Monthly Energy:", round(total_monthly, 2), "kWh")
                print("Total Daily Cost: N", round(total_daily_cost, 2))
                print("Total Monthly Cost: N", round(total_monthly_cost, 2))

except ValueError:
    print("Invalid input! Please enter numbers where required.")