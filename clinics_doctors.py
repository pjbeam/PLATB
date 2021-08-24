import rando_names
import random

name_pool = rando_names.get_names()

def get_clinics_doctors():
    clinic_or_doctor = random.choice([0,1,2,3,4,5,6,7,8,9])
    if clinic_or_doctor > 6:
        return random.choice(["Planned Parenthood", "Houston Women's Clinic", "Boulder Abortion Clinic", "Houston Women's Reproductive Services", "Southwestern Women's Surgery Center", "Suburban Women's Clinic"])
    else:
        return random.choice(name_pool) + " " + random.choice(name_pool)