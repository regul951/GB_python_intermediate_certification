import random
import pandas as pd

lst = ['robot'] * 1000
lst += ['human'] * 1000
random.shuffle(lst)



# Используем dummies
data = pd.DataFrame({'WhoAmI':lst})

print(pd.get_dummies(data, dtype=int))



# Не используем dummies
new_dict = {}
for i in lst:
  if i == 'human':
    new_dict['human'] = new_dict.get('human', []) + [1]
    new_dict['robot'] = new_dict.get('robot', []) + [0]
  else:
    new_dict['human'] = new_dict.get('human', []) + [0]
    new_dict['robot'] = new_dict.get('robot', []) + [1]

print(pd.DataFrame(new_dict))