import random

def username_generator(n, first_names=None, last_names=None):
  if not first_names:
    first_names = ["Max", "Sophia", "Liam"]
  if not last_names:
    last_names = ["Miller", "Davis", "Garcia"]
  for id in range(1, n+1):
    user = {}
    first_name_idx = random.randint(0, len(first_names) - 1)
    last_name_idx = random.randint(0, len(last_names) - 1)
    user['id'] = id
    user['first_name'] = first_names[first_name_idx]
    user['last_name'] = last_names[last_name_idx]
    yield user
