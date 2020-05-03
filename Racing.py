import random


class Racer:
    value = 1

    def __init__(self, name, num, denom):
        self.name = name
        self.odds = num/denom
        self.num = num
        self.denom = denom


# verifies that the odds are mathematically accurate
def odds_verification(participants, trials, race_setup):
    stats = list()
    adjustment = 0
    accuracy = 0
    for a in range(0, len(participants)):
        stats.append(0)
        adjustment = adjustment + participants[a].odds
    for b in range(0, trials):
        choice = random.choice(race_setup)
        for n in range(0, len(participants)):
            if choice == participants[n].name:
                stats[n] = stats[n] + 1

    for m in range(0, len(participants)):
        print(participants[m].name + ": ")
        experimental = stats[m] * adjustment / trials
        print("  Experimental Odds (Adjusted): " + str(experimental))
        print("  Theoretical Odds:             " + str(participants[m].odds))
        x = 1 - abs(experimental - participants[m].odds)
        x = x * 100
        accuracy = x + accuracy
        print("                               ", '{:.2f}'.format(round(x, 2)), "% accurate")
    print('\n' + "Overall:                       ", '{:.2f}'.format(round(accuracy/len(participants), 2)), "% accurate" + '\n')


# Displays winners, chosen based on given theoretical odds
def winners(participants, race_setup):
    for l in range(0, len(participants)):
        winner = random.choice(race_setup)
        temprace = list()
        for c in race_setup:
            if c != winner:
                temprace.append(c)
        race_setup = temprace
        print(str(l + 1) + ". " + winner)


racers = list()
factor = 1
race = list()

racers.append(Racer("Big Honker", 7, 8))
racers.append(Racer("Ubtao's Favorite", 5, 6))
racers.append(Racer("Banana Candy", 3, 4))
racers.append(Racer("Bonecruncher", 2, 3))
racers.append(Racer("Grung Stomper", 1, 2))
racers.append(Racer("Scarback", 1, 3))
racers.append(Racer("Nasty Boy", 1, 4))
racers.append(Racer("Jungle Princess", 1, 6))
racers.append(Racer("Mountain Thunder", 1, 8))

for x in racers:
    if not ((factor % x.denom) == 0):
        factor = factor * x.denom

for y in racers:
    y.value = y.num * y.value * (factor/y.denom)

for z in racers:
    for r in range(0, int(z.value)):
        race.append(z.name)

# odds_verification(racers, 100000, race)
winners(racers, race)
