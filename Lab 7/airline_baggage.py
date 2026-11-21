import math


def parse_booking(code):
    if not isinstance(code, str):
        raise TypeError("Booking code must be a string")

    parts = code.split('-')

    if len(parts) != 3:
        raise ValueError("Invalid booking code")

    airline, flight, seat = parts

    if not airline.isalpha():
        raise ValueError("Invalid airline code")

    if not flight.isdigit() or int(flight) <= 0:
        raise ValueError("Invalid flight number")

    if not seat[:-1].isdigit() or not seat[-1:].isalpha():
        raise ValueError("Invalid seat number")

    return airline.upper(), int(flight), seat[-1].upper()


def total_weight(weights_csv):
    if not isinstance(weights_csv, str):
        raise TypeError("Weights must be a string")

    if not weights_csv.strip():
        raise ValueError("Weights cannot be empty")

    weights = weights_csv.split(',')
    total = 0

    for w in weights:
        if not w.strip():
            raise ValueError("Empty weight")

        try:
            weight = float(w)
        except ValueError:
            raise ValueError("Invalid weight")

        if not math.isfinite(weight) or weight < 0:
            raise ValueError("Invalid weight value")

        total += weight

    return total


def tag_label(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    parts = name.split()

    if len(parts) < 2:
        raise ValueError("Enter first and last name")

    return parts[0][0].upper() + '. ' + parts[1].upper()

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)

if __name__ == "__main__":
    main()
