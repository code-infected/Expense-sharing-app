def validate_percentage_split(split_details):
    total_percentage = sum(split_details.values())
    if total_percentage != 100:
        raise ValueError("Percentages do not add up to 100%")
