from prescription_data import adverse_interactions

# Extract all the drugs from the adverse_interactions list of sets
    # Create empty set to hold the union of all the sets of adverse_interaction
meds_to_watch = set()
    # Iterate over the sets in the list and use the union() to combine them
for interaction in adverse_interactions:
    #meds_to_watch = meds_to_watch.union(interaction)
    meds_to_watch.update(interaction)
print(sorted(meds_to_watch))

    # Instead of using the for loop to go over the list, we should prefer to unpack the list adverse_interactions
    # and pass each set as an argument to the update() method
meds_to_watch.update(*adverse_interactions)
print(*sorted(meds_to_watch), sep='\n')


# Basic principle of the union() method
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# Create a union of both sets. The union() method create a new set
all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)
all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

# Update an existing set doesn't create a new set
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

sting_animal = scorpions.union(vespas)
bite_animals = spiders.union(snakes)
arachnids = spiders.union(scorpions)