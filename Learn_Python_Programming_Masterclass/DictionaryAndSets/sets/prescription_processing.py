from prescription_data import patients

# Create the trial_patients set
trial_patients = {"Denise", "Eddie", "Frank", "Georgia","Kenny"}

while trial_patients:
    # pop() method removes an item from a set and returns it.
    # It's useful when we need to go over all the items of a set, but we don't care about the order
    patient_name = trial_patients.pop()
    print(patient_name, end=" : ")
    patient_prescription = patients[patient_name]
    print(patient_prescription)
