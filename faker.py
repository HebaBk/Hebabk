from faker import Faker
import csv

fake = Faker()

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Job"])  # العناوين
    for _ in range(10):
        writer.writerow([fake.name(), fake.email(), fake.job()])

print("✅ users.csv file created with fake data!")

