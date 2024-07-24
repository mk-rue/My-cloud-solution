import csv
from .models import Company

def handle_uploaded_file(file):
    reader = csv.reader(file)
    for row in reader:
        Company.objects.create(
            name=row[0],
            registration_date=row[1],
            registration_number=row[2],
            address=row[3],
            contact_person=row[4],
            departments=row[5],
            number_of_employees=row[6],
            contact_phone=row[7],
            email=row[8],
        )
