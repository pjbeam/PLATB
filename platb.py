from selenium import webdriver
import json
import pathlib
import glob
import sys
sys.path.append(".")
import random
import utils
import texas_geo_data
import clinics_doctors
import how_evidence
import violate_how

geo_data = texas_geo_data.get_geo_data()
forms_of_texas = ["TX", "Tx", "tx", "Texas", "texas", "TEXAS", "tex", "Tex", "TEX"]

def assemble_submission_data():
    submission_geo_data = random.choice(geo_data)
    return {
        "VIOLATE_HOW": violate_how.get_violate_how(),
        "HOW_EVIDENCE": how_evidence.get_how_evidence(),
        "CLINIC_OR_DOCTOR": clinics_doctors.get_clinics_doctors(),
        "CITY": submission_geo_data["City"],
        "COUNTY": submission_geo_data["County"],
        "ZIP": submission_geo_data["Zip Code"],
        "STATE": random.choice(forms_of_texas)
    }

# Form element information

VIOLATE_HOW_ID = "forminator-field-textarea-1"
HOW_EVIDENCE_ID = "forminator-field-text-1"
CLINIC_OR_DOCTOR_ID = "forminator-field-text-6"
CITY_ID = "forminator-field-text-2"
STATE_ID = "forminator-field-text-3"
ZIP_ID = "forminator-field-text-4"
COUNTY_ID = "forminator-field-text-5"


# handle checkbox:
# driver.findElement(By.xpath("//label[text()='No']")).click()

print(assemble_submission_data())

# platb = faker.Faker()
# colors = ["Blue","Pink","Black","White","Green"]

# names = [f.name() for _ in range(100)]
# ages =  [np.random.randint(18,65) for _ in range(100)]
# color_choices = [np.random.choice(colors,1)[0] for _ in range(100)]

# database = pd.DataFrame(dict(names=names, ages=ages, colors = color_choices))
# database.to_csv("submission_form_database.csv", index=False)
# database.head()