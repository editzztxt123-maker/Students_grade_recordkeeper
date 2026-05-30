
gradebook = {}

print("--- Data Entry Phase ---")
while True:
    name = input("Enter student name (or type 'done' to finish): ").strip().capitalize()
    
    if name.lower() == 'done':
        break
        
    marks = input(f"Enter marks for {name}: ")
    gradebook[name] = marks  
    print(f"Added {name} to the records.\n")

print("\n--- Search Phase ---")
search_name = input("Enter the name of the student you want to find: ").strip().capitalize()

if search_name in gradebook:
    print(f"✅ {search_name} scored {gradebook[search_name]} marks.")
else:
    print(f"❌ Record for '{search_name}' not found.")