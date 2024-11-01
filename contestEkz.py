n = int(input())
tic = list(map(int, input().split()))
tickets = sorted(tic, reverse=True)
total_tickets = sum(tickets)
if total_tickets % 3 != 0:
 print(0)
else:

 group_size = total_tickets // 3


 groups = [0] * 3


 for i in range(n):
  min_group = groups.index(min(groups))
  groups[min_group] += tickets[i]

 if all(group == group_size for group in groups):
  print(1)
 else:
  print(0)