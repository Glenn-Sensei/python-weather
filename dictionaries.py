# Dictionaries
band = {
    'vocals': 'Plate',
    'guitar': 'Page'
}

band2 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access items
print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

print(band.items())

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))
