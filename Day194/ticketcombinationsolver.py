def ticketcombinationsolver():
    print("Ticket Combination Solver :")

    try:
        total_amount = int(input("Enter the total number of tickets: "))
        ticket_types = int(input("Enter the number of ticket types: "))

        if total_amount <= 0 or ticket_types <= 0:
            print("Ticket quantities and ticket types must be greater than zero.")
            return

        prices = []
        names = []

        for i in range(ticket_types):
            name = input("\nEnter ticket type " + str(i + 1) + ": ")
            price = int(input("Enter price of " + name + ": "))

            if price <= 0:
                print("Ticket price must be greater than zero.")
                return

            names.append(name)
            prices.append(price)

        budget = int(input("\nEnter the total budget: "))

        if budget < 0:
            print("Budget cannot be negative.")
            return

    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return

    combinations = []

    def find_combinations(index, remaining_tickets, remaining_budget, current):
        if index == ticket_types:
            if remaining_tickets == 0 and remaining_budget == 0:
                combinations.append(current.copy())
            return

        price = prices[index]

        for quantity in range(remaining_tickets + 1):
            cost = quantity * price

            if cost <= remaining_budget:
                current.append(quantity)
                find_combinations(
                    index + 1,
                    remaining_tickets - quantity,
                    remaining_budget - cost,
                    current
                )
                current.pop()

    find_combinations(0, total_amount, budget, [])

    print("\nTicket Combination Results :")

    if combinations:
        for number, combination in enumerate(combinations, start=1):
            print("\nCombination", number)
            total_cost = 0

            for i in range(ticket_types):
                quantity = combination[i]
                cost = quantity * prices[i]
                total_cost += cost

                print(
                    names[i],
                    "- Quantity:", quantity,
                    ", Cost:", cost
                )

            print("Total Tickets:", sum(combination))
            print("Total Cost:", total_cost)

        print("\nTotal Valid Combinations:", len(combinations))
    else:
        print("No combination satisfies the given ticket count and budget.")

    print("\nSummary :")
    print("Required Tickets:", total_amount)
    print("Available Budget:", budget)
    print("Ticket Types:", ticket_types)
    print("Valid Combinations Found:", len(combinations))

ticketcombinationsolver()