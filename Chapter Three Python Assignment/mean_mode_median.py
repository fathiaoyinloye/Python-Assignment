import statistics

values = [9,11,22,34,17,22,34,22,40]
mean_of_values =  statistics.mean(values)
median_of_values =  statistics.median(values)
mode_of_values =  statistics.mode(values)
 
print(f"The mean is{mean_of_values: .0f}")
print(f"The median is{median_of_values: .0f}")
print(f"The mode  is{mode_of_values: .0f}")
