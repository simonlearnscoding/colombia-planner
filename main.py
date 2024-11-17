from data import bogota, destinations  # Import data
from logic import calculate_itinerary, format_itinerary, get_user_preferences


def get_trip_duration():
    """
    Prompt the user for the total duration of their trip.

    Returns:
        int: The total number of days for the trip.
    """
    while True:
        try:
            days = int(input("Enter the total number of days for your trip: "))
            if days > 0:
                return days
            else:
                print("Please enter a positive number of days.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    # Ask the user for the total duration of the trip first
    days_available = get_trip_duration()

    # Ask the user for their preference points
    get_user_preferences(destinations)

    # Configuration for the itinerary
    mandatory_points = [bogota]  # Ensure the trip starts and ends in Bogotá

    # Calculate the best itinerary
    best_itinerary, points, cost = calculate_itinerary(
        destinations, bogota, days_available, mandatory_points
    )

    # Output results
    if best_itinerary:
        print("Best Itinerary:")
        print(format_itinerary(best_itinerary, mandatory_points))
        print(f"Total Preference Points: {points}")
        print(f"Total Travel Cost: ${cost}")
    else:
        print("No feasible itinerary found.")
