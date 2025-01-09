# Sort dictionary in ascending and descending order.

d={"apple":10,"kiwi":20,"grape":12,"banana":23}
print("Dictionary before sorting:",d)
ares=dict(sorted(d.items()))
print("Dictionary in ascending order:",ares)
bres=dict(sorted(d.items(),reverse=True))
print("Dictionary in descending order:",bres)
