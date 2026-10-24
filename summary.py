
import csv
import json
from collections import defaultdict

CSV_FILE = "device_telemetry.csv"
JSON_FILE = "summary.json"
MAX_AVERAGE_TEMP = 80


def analyze_telemetry():
    devices = defaultdict(lambda: {
        "total_records": 0,
        "temperature_sum": 0.0,
        "temperature_count": 0,
        "error_count": 0
    })

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {"device_id", "status", "temperature"}
            if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
                print("Error: CSV file is missing required columns.")
                return

            for row in reader:
                device = row["device_id"].strip()
                status = row["status"].strip().upper()

                if not device:
                    continue

                stats = devices[device]
                stats["total_records"] += 1

                if status == "ERROR":
                    stats["error_count"] += 1

                try:
                    temp = float(row["temperature"])
                    if temp == temp and abs(temp) != float("inf"):
                        stats["temperature_sum"] += temp
                        stats["temperature_count"] += 1
                except (ValueError, TypeError):
                    continue

    except FileNotFoundError:
        print(f"Error: {CSV_FILE} was not found.")
        return

    results = []

    for device_id, stats in devices.items():
        count = stats["temperature_count"]

        if count == 0:
            continue

        average = stats["temperature_sum"] / count

        if average <= MAX_AVERAGE_TEMP:
            results.append({
                "device_id": device_id,
                "total_records": stats["total_records"],
                "average_temperature": round(average, 2),
                "error_count": stats["error_count"]
            })

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\nDevice Telemetry Summary")
    print("-" * 76)
    print(f"{'Device ID':<15}{'Total Records':<18}{'Average Temp':<20}{'Errors':<10}")
    print("-" * 76)

    for item in results:
        print(
            f"{item['device_id']:<15}"
            f"{item['total_records']:<18}"
            f"{item['average_temperature']:<20.2f}"
            f"{item['error_count']:<10}"
        )

    print("-" * 76)
    print(f"Results saved to {JSON_FILE}")


if __name__ == "__main__":
    analyze_telemetry()
