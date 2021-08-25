from selenium import webdriver
import sys
import time
sys.path.append(".")
import random
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
        "ZIP": str(submission_geo_data["Zip Code"]),
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
CHECKBOX_CLASS = "forminator-checkbox-label"
SUBMIT_CLASS = "forminator-button-submit"

# Setup Web Driver

# For theoretical research purposes ONLY:
url = "https://prolifewhistleblower.com/anonymous-form/"

# Note: the windows webdriver is packaged here. If you are on Mac/Linux, get the correct one from
# https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/ and switch it out (ensure filename is correct in the line below).
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920x1080")
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(options=options, executable_path="./chromedriver.exe")


driver.get("https://manytools.org/http-html-text/http-request-headers/")
driver.get(url)

# Fill in form:

submission_data = assemble_submission_data()
randobet = "abcdefghijklmnopqrstuvwxyz1234567890.,/'"
def type_like_personish(target, data):
    while len(data) > 0:
        correct_or_typo = random.randint(1,100)
        if correct_or_typo > 3:
            target.send_keys(data[0])
            data = data[1:]
        else:
            rando_key = random.randint(0,len(randobet)-1)
            target.send_keys(randobet[rando_key])
            time.sleep((random.randint(23, 389))/1000)
            target.send_keys("\b")
        time.sleep((random.randint(23, 389))/1000)

time.sleep(15)

# How do you think the law has been violated?
VIOLATE_HOW_TARGET = driver.find_element_by_id(VIOLATE_HOW_ID)
VIOLATE_HOW_TARGET.click()
type_like_personish(VIOLATE_HOW_TARGET, submission_data["VIOLATE_HOW"])

time.sleep(random.randint(1,9))

# How did you obtain this evidence?
HOW_EVIDENCE_TARGET = driver.find_element_by_id(HOW_EVIDENCE_ID)
HOW_EVIDENCE_TARGET.click()
type_like_personish(HOW_EVIDENCE_TARGET, submission_data["HOW_EVIDENCE"])

time.sleep(random.randint(6,11))

# Clinic or Doctor this evidence relates to
CLINIC_OR_DOCTOR_TARGET = driver.find_element_by_id(CLINIC_OR_DOCTOR_ID)
CLINIC_OR_DOCTOR_TARGET.click()
type_like_personish(CLINIC_OR_DOCTOR_TARGET, submission_data["CLINIC_OR_DOCTOR"])

time.sleep(random.randint(6,11))

# City
CITY_TARGET = driver.find_element_by_id(CITY_ID)
CITY_TARGET.click()
type_like_personish(CITY_TARGET, submission_data["CITY"])

time.sleep(random.randint(6,11))

# State
STATE_TARGET = driver.find_element_by_id(STATE_ID)
STATE_TARGET.click()
type_like_personish(STATE_TARGET, submission_data["STATE"])

time.sleep(random.randint(6,11))

# ZIP
ZIP_TARGET = driver.find_element_by_id(ZIP_ID)
ZIP_TARGET.click()
type_like_personish(ZIP_TARGET, submission_data["ZIP"])

time.sleep(random.randint(6,11))

# County
COUNTY_TARGET = driver.find_element_by_id(COUNTY_ID)
COUNTY_TARGET.click()
type_like_personish(COUNTY_TARGET, submission_data["COUNTY"])

time.sleep(random.randint(6,11))

# handle checkbox:
driver.find_elements_by_class_name(CHECKBOX_CLASS)[1].click()

time.sleep(45)

# launch it
driver.find_element_by_class_name(SUBMIT_CLASS).click()
