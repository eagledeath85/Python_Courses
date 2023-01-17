import re

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

words = set(re.findall(r'[\w]+', text))

print(words)
preps_used = words.intersection(prepositions)
print(preps_used)