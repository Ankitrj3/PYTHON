import pyshorteners

s = pyshorteners.Shortener()
long_url = input("Enter a long URL to shorten: ")
short_url = s.tinyurl.short(long_url)
print("Shortened URL:", short_url)
