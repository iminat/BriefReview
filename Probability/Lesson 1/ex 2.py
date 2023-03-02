#Consider a game where your score is the maximum value from two dice.
#Compute the probability of each event from 1 to 6.
total_outcomes = 36  # 6 * 6 possible outcomes when rolling two dice

for event in range(1, 7):
    # The number of outcomes that result in the event
    favorable_outcomes = 0

    # Loop through all possible combinations of the two dice
    for i in range(1, 7):
        for j in range(1, 7):
            if max(i, j) == event:
                favorable_outcomes += 1

    # Compute the probability of the event
    probability = favorable_outcomes / total_outcomes

    print(f"Event {event}: {probability:.2f}")