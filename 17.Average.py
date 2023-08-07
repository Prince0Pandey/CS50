import statistics
lst = [12,90,50,45,35,25,75,60,120,900,4,50,3,6,8,69,45,35,67,25,5,35,25,50]
print(f"mean:",statistics.mean(lst))
print(f"Median:",statistics.median(lst))
print("Mode:",statistics.mode(lst))
print("Median_Low:",statistics.median_low(lst))
print("MultiMode:",statistics.multimode(lst))