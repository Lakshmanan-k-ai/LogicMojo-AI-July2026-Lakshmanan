#longest name with out using max function
names = ["Ada", "Alan", "Grace", "Katherine", "Ed"]
names_dicts = {name: len(name) for name in names}
print(names_dicts)
max_length = max(names_dicts.values())
#longest_name = max(names_dicts, key=names_dicts.get)
longest_names = [longest_name for longest_name in names_dicts if names_dicts[longest_name] == max_length]

print(f"Longest: {longest_names} ({max_length} letters)")
