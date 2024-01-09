def dfs_schedule(day, slot, staff, current_schedule, all_schedules, days, slots_per_day, availability):
    if day > days:
        all_schedules.append(current_schedule.copy())
        return
    
    if slot > slots_per_day:
        dfs_schedule(day + 1, 1, staff, current_schedule, all_schedules, days, slots_per_day, availability)
        return

    for staff_member in staff:
        # Check if the staff member is available on this day
        if day in availability.get(staff_member, []):
            # Assign staff_member to current slot
            current_schedule[(day, slot)].add(staff_member)

            # Move to next slot
            dfs_schedule(day, slot + 1, staff, current_schedule, all_schedules, days, slots_per_day, availability)

            # Backtrack
            current_schedule[(day, slot)].remove(staff_member)

def create_month_schedule(staff, availability, days=30, slots_per_day=3):
    # Initialize schedule for each day and slot
    current_schedule = {(day, slot): set() for day in range(1, days + 1) for slot in range(1, slots_per_day + 1)}
    all_schedules = []
    dfs_schedule(1, 1, staff, current_schedule, all_schedules, days, slots_per_day, availability)
    return all_schedules

staff = ["Staff1", "Staff2", "Staff3", "Staff4", "Staff5", "Staff6", "Staff7"]
availability = {
    "Staff1": [1, 2, 3, 15, 16],  # Days of the month Staff1 is available
    "Staff2": [1, 4, 5, 6, 20],
    # ... similarly for other staff members
}

all_schedules = create_month_schedule(staff, availability)

# Print the first schedule for demonstration
first_schedule = all_schedules[0]
for day in sorted(first_schedule.keys()):
    print(f"Day {day[0]}, Slot {day[1]}: {first_schedule[day]}")
