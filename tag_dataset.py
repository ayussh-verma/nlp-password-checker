import csv
from zxcvbn import zxcvbn

scored_passwords: dict[str, int] = {}

with open("data.csv") as f:
    reader = csv.DictReader(open("data.csv"))

    for entry in reader:
        scored_passwords[entry["password"]] = zxcvbn(entry["password"])["score"]


with open("data_scored.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, ["password", "strength"])
    writer.writeheader()

    for password, strength in scored_passwords.items():
        writer.writerow({"password": password, "strength": strength})
