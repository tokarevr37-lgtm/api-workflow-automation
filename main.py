import csv
from datetime import datetime


def fetch_api_data():
    """
    Demo API response.
    In a real project, this function would connect to an external API.
    """
    return [
        {"id": 1, "source": "CRM", "status": "success", "records": 250},
        {"id": 2, "source": "Orders API", "status": "success", "records": 180},
        {"id": 3, "source": "Inventory API", "status": "success", "records": 95},
    ]


def process_data(data):
    processed = []

    for item in data:
        processed.append({
            "workflow_id": item["id"],
            "data_source": item["source"],
            "status": item["status"],
            "records_processed": item["records"],
            "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return processed


def export_to_csv(data, filename="sample_output.csv"):
    fieldnames = [
        "workflow_id",
        "data_source",
        "status",
        "records_processed",
        "processed_at"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    api_data = fetch_api_data()
    processed_data = process_data(api_data)
    export_to_csv(processed_data)

    print("API workflow completed successfully.")
    print(f"Records processed: {sum(item['records_processed'] for item in processed_data)}")
    print("Output file: sample_output.csv")


if __name__ == "__main__":
    main()
