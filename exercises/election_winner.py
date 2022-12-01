from collections import Counter

votes = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie',
         'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']

vote_count = Counter(votes)
print(vote_count)

max_votes = max(vote_count.values())
print(max_votes)

#lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]
lst = []
for i in vote_count.keys():
    if vote_count[i] == max_votes:
        lst.append(i)

lst.sort()
print(lst)
print(lst[0])
