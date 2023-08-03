print ('Hello to anyone in the world')


# Example of list
countdown = [3, 2, 1]
print(countdown)


last_calls = ["Andreas", "Habibi", "Khan"]
print(last_calls[0])
print(last_calls[1])




fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))


n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)