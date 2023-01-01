from prescription_data import *


trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
# In this example, Kenny doesn't take Warfarin
# With discard() we don't know that, as the method doesn't return any error
# We then end by adding edoxaban to someone that doesn't need it
for patient in trial_patients:
    prescription = patients[patient]  # prescription is a set
    prescription.remove(warfarin)
    prescription.add(edoxaban)
    print(patient, prescription)