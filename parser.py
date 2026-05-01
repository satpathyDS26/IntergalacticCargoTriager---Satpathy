import json
import math

INPUT_FILE = "manifest.txt"
OUTPUT_FILE = "Task 1 - Satpathy - Parser.json"


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def parse_line(line):
    try:
        # Split structure
        date_part, rest = line.split("||")
        cargo_part, dest_part = rest.split(">>")

        # Extract fields
        date = date_part.strip().strip("[]")
        cargo_id_part, weight_part = cargo_part.split("::")

        cargo_id = cargo_id_part.strip()
        weight = float(weight_part.strip())
        destination = dest_part.strip()

        # Apply Rule 1 for exact substring(Sector-7)
        if  "Sector-7" in destination:
            weight *= 1.45

        # Apply Rule 2 (round AFTER multiplication)
        weight = round(weight)

        # Apply prime check
        if is_prime(weight):
            return None  # discard record

        return {
            "date": date,
            "cargo_id": cargo_id,
            "weight": int(weight),
            "destination": destination
        }

    except Exception as e:
        print(f"Error parsing line: {line}")
        return None


def main():
    results = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            parsed = parse_line(line.strip())
            if parsed:
                results.append(parsed)

    # Save JSON
    with open(OUTPUT_FILE, "w") as out:
        json.dump(results, out, indent=4)

    print(f"Valid records: {len(results)}")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()