"""Blood donation management demonstration."""

from datetime import date, timedelta
import tempfile

donors = []
stock = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "O+": 0,
    "O-": 0,
    "AB+": 0,
    "AB-": 0,
}

COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
    "AB-": ["AB-", "A-", "B-", "O-"],
    "A-": ["A-", "O-"],
    "B-": ["B-", "O-"],
}


def register_donor(
    donor_name,
    blood_group,
    age,
    last_donation=None,
    notes=None,
):
    """Register a donor after validating their details."""
    if blood_group not in stock:
        raise ValueError("Unknown blood group")

    if age < 18 or age > 65:
        if notes is not None:
            notes.append(
                f"{donor_name} is not eligible because of age"
            )
        return False

    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Check whether a donor can donate based on their last donation."""
    if donor["last"] is None:
        return True

    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation if the donor is eligible."""
    if units <= 0:
        raise ValueError("Units must be greater than zero")

    for donor in donors:
        if donor["name"] == donor_name and can_donate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True

    return False


def units_for(patient_group):
    """Calculate available units compatible with a patient's group."""
    if patient_group not in COMPATIBLE:
        return 0

    return sum(
        stock[group] for group in COMPATIBLE[patient_group]
    )


def is_universal(blood_group):
    """Check whether the group is a universal donor or recipient group."""
    return blood_group in ("O-", "AB+")


def low_stock(threshold=2):
    """Return blood groups with stock below the threshold."""
    return [
        group
        for group, units in stock.items()
        if units < threshold
    ]


def donor_sheet_path():
    """Create a secure temporary file path for a donor sheet."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv",
        delete=False,
    ) as temporary_file:
        return temporary_file.name


def notify_donors(phone_list):
    """Prepare a notification message for the supplied phone numbers."""
    if not phone_list:
        return "No donors to notify."

    return f"Notification prepared for {len(phone_list)} donor(s)."


def main():
    """Run the blood donation demonstration."""
    register_donor("Arjun", "O+", 25)
    register_donor(
        "Priya",
        "A+",
        30,
        date.today() - timedelta(days=30),
    )
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)

    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")

    eligible = [donor for donor in donors if can_donate(donor)]

    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("O- is universal:", is_universal("O-"))
    print("Low stock groups:", low_stock())
    print("Eligible donors today:", len(eligible))


if __name__ == "__main__":
    main()
