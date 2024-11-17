from concurrent.futures import ProcessPoolExecutor
from itertools import combinations, permutations


def get_user_preferences(destinations):
    """
    Prompt the user to assign preference points (1-10) for each destination,
    displaying recommended days and a description for each.

    Args:
        destinations (list): List of Destination objects.

    Returns:
        None: Updates the `preference_points` attribute of each destination.
    """
    print("Rate each destination from 1 to 10 based on your preference.")
    print("------------------------------------------------------------")
    for destination in destinations:
        print(f"Destination: {destination.title}")
        print(f"Recommended Days: {destination.estimated_time}")
        print(f"Description: {destination.description}")
        print("------------------------------------------------------------")
        while True:
            try:
                rating = int(
                    input(f"How much do you want to visit {destination.title}? (1-10): ")
                )
                if 1 <= rating <= 10:
                    destination.preference_points = rating
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
        print("\n")


def evaluate_subset(args):
    """
    Evaluate a subset of destinations for the best itinerary, including mandatory points and travel time.

    Args:
        args (tuple): A tuple containing:
            subset (list): Subset of destinations to evaluate.
            start_destination (Destination): Starting point of the itinerary.
            days_available (int): Total number of days available for the trip.
            mandatory_points (list): List of mandatory destinations to include in the itinerary.

    Returns:
        tuple: The best itinerary (list of Destination objects), total points, total cost, and total travel time.
    """
    subset, start_destination, days_available, mandatory_points = args
    best_itinerary = None
    max_points = 0
    min_cost = float("inf")

    # Ensure both `subset` and `mandatory_points` are lists
    full_subset = list(set(list(subset) + list(mandatory_points)))

    for perm in permutations(full_subset):
        itinerary = [start_destination] + list(perm) + [start_destination]
        total_time = 0
        total_travel_time = 0
        total_cost = 0
        total_points = 0
        feasible = True

        for i in range(len(itinerary) - 1):
            current = itinerary[i]
            next_dest = itinerary[i + 1]
            # Find the travel cost and travel time to the next destination
            connection = next(
                (
                    (price, travel_time)
                    for dest, price, travel_time in current.connections
                    if dest == next_dest
                ),
                None,
            )
            if not connection:  # Invalid connection
                feasible = False
                break

            travel_cost, travel_time = connection
            total_cost += travel_cost
            total_travel_time += travel_time
            total_time += travel_time  # Add travel time
            total_time += current.estimated_time  # Add time spent at the destination

            # Early return if the total time exceeds available days
            if total_time > days_available:
                feasible = False
                break

        # Add travel time for the last leg back to the start
        if feasible:
            total_time += itinerary[-2].estimated_time

            if total_time <= days_available:
                total_points = sum(
                    dest.preference_points for dest in itinerary[:-1]
                )  # Skip the last return to start

                # Check if this itinerary is better
                if (total_points > max_points) or (
                    total_points == max_points and total_cost < min_cost
                ):
                    max_points = total_points
                    min_cost = total_cost
                    best_itinerary = itinerary

    return best_itinerary, max_points, min_cost, total_travel_time


def calculate_itinerary(
    destinations, start_destination, days_available, mandatory_points
):
    """
    Calculate the best itinerary using parallel processing, ensuring mandatory points are included.

    Args:
        destinations (list): List of Destination objects.
        start_destination (Destination): Starting point of the itinerary.
        days_available (int): Total number of days available for the trip.
        mandatory_points (list): List of mandatory destinations to include in the itinerary.

    Returns:
        tuple: The best itinerary (list of Destination objects), total points, total cost, and total travel time.
    """
    best_itinerary = None
    max_points = 0
    min_cost = float("inf")
    total_travel_time = 0
    subsets = [
        subset
        for subset_size in range(1, min(len(destinations), 7))  # Limit subset size
        for subset in combinations(
            [d for d in destinations if d != start_destination], subset_size
        )
    ]

    with ProcessPoolExecutor() as executor:
        results = executor.map(
            evaluate_subset,
            [
                (subset, start_destination, days_available, mandatory_points)
                for subset in subsets
            ],
        )

    for itinerary, points, cost, travel_time in results:
        if points > max_points or (points == max_points and cost < min_cost):
            best_itinerary, max_points, min_cost, total_travel_time = (
                itinerary,
                points,
                cost,
                travel_time,
            )

    return best_itinerary, max_points, min_cost, total_travel_time


def format_itinerary(itinerary, mandatory_points):
    """
    Format the itinerary for display with day ranges, transit details, and descriptions.

    Args:
        itinerary (list): List of Destination objects representing the itinerary.
        mandatory_points (list): List of mandatory destinations to highlight transit points.

    Returns:
        str: Formatted string of the itinerary.
    """
    output = []
    current_day = 1
    output.append(f"Start at: {itinerary[0].title}")

    for i in range(len(itinerary) - 1):
        current = itinerary[i]
        next_dest = itinerary[i + 1]

        # Find the travel cost and travel time to the next destination
        connection = next(
            (
                (price, travel_time)
                for dest, price, travel_time in current.connections
                if dest == next_dest
            ),
            None,
        )
        travel_cost, travel_time = connection if connection else (None, None)

        # Add transit information
        output.append(
            f"{current.title} -> {next_dest.title}. ${travel_cost if travel_cost else 'N/A'}, Travel Time: {travel_time if travel_time else 'N/A'} days"
        )

        # If it's not a transit-only destination, add details
        if next_dest not in mandatory_points:
            end_day = current_day + next_dest.estimated_time - 1
            output.append(f"Day {current_day} - Day {end_day}: {next_dest.title}")
            output.append("-----")
            current_day = end_day + 1

    return "\n".join(output)
