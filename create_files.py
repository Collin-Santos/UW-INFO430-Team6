twitter_handles = [17351972, 300114634, 153031349, 21915474, 50883209,
    32171828, 183398746, 752072829278023680, 16252784, 23114836,
    15383636]

for handle in twitter_handles:
    f = open('data/tweets_{}.json'.format(handle), 'w')
    f.close()

u = open('data/users.json', 'w')
u.close()