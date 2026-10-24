def clean_sensor_readings(values):
    cleaned = []

    for value in values:
        if value is None:
            continue

        try:
            num = float(value)
        except (ValueError, TypeError):
            continue

        if num < 0:
            continue

        if num > 500.0:
            num = 500.0

        cleaned.append(num)

    return cleaned


# Test Case 1: Mixed valid and invalid values
print(clean_sensor_readings([10, "25.5", None, -5, "abc", 600]))

# Test Case 2: Empty list
print(clean_sensor_readings([]))

# Test Case 3: All invalid values
print(clean_sensor_readings([None, -10, "hello", ""]))
