def seconds_since_midnight(hours, minutes, seconds):
	hours_in_seconds = hours * 60 * 60
	minutes_in_seconds = minutes * 60
	return hours_in_seconds + minutes_in_seconds + seconds


print(seconds_since_midnight(13,30,45))