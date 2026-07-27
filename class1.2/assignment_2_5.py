#shared tags
monday = ["python", "git", "venv", "ml"]
tuesday = ["git", "ml", "numpy", "pandas"]
monday_set = set(monday);
tuesday_set = set(tuesday);
#intersection
shared_tags = monday_set & tuesday_set
print(f"in both: {sorted(shared_tags)}")
#union
all_tags = monday_set | tuesday_set
print(f"in either: {sorted(all_tags)}")
print(f"{len(shared_tags)} shared, {len(all_tags)} total")