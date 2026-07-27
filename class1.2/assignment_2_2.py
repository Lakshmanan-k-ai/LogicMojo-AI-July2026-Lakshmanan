#clean a messy record
raw = "  Ada Lovelace,  ADA@Math.ORG , London  "
fieldsraw = raw.split(",")
print (fieldsraw)
name = fieldsraw[0].strip()
email = fieldsraw[1].strip().lower()
city = fieldsraw[2].strip()
print(f"Name: {name}")
print(f"Email: {email}")
print(f"City: {city}")
print(f"domain: {email.split('@')[1]}")
print(f"initials: {name[0]}{name.split()[1][0]}")