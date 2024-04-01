def calculate_coffee_needed(events):
    coffee_count = 0
    for event in events:
        if event == "coding":
            coffee_count += 1
        elif event == "dog" or event == "cat":
            coffee_count += 1
        elif event == "movie":
            coffee_count += 1
        elif event.isalpha():  # ignore other events represented by arbitrary strings
            continue
    return coffee_count

def main():
    events = []
    while True:
        event = input().strip().lower()
        if event == "end":
            break
        events.append(event)

    coffee_count = calculate_coffee_needed(events)
    if coffee_count > 5:
        print("You need extra sleep")
    else:
        print(coffee_count)

if __name__ == "__main__":
    main()
