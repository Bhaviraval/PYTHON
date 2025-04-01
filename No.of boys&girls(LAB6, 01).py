names = [('Ayaan',), 'Bhavi', ('Aakash',), 'Nishi', 'Aarya']

boys_count = sum(1 for name in names if isinstance(name, tuple))
girls_count = len(names) - boys_count

print("Number of boys:", boys_count)
print("Number of girls:", girls_count)
