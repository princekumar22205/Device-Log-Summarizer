
import json
import matplotlib.pyplot as plt

INPUT_FILE = "summary.json"
OUTPUT_FILE = "temperature_chart.png"


def create_temperature_chart():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Unable to read input file: {error}")
        return

    if not records:
        print("No device data available to plot.")
        return

    device_names = [item["device_id"] for item in records]
    avg_temperatures = [
        item["average_temperature"] for item in records
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(device_names, avg_temperatures)

    plt.title("Average Temperature by Device")
    plt.xlabel("Device ID")
    plt.ylabel("Average Temperature")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(OUTPUT_FILE, dpi=300)
    plt.show()

    print(f"Chart saved as {OUTPUT_FILE}")


if __name__ == "__main__":
    create_temperature_chart()
