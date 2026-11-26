import passes
passes_rounds = passes.rounds

import archive
archive_rounds = archive.rounds

all_rounds = passes_rounds + archive_rounds

print("REGEX-ДЕТЕКТИВ")
print("Из лаборатории пропали секретные чертежи. Найдите вора.")

clues = []

for game_round in all_rounds:
    print()
    print(game_round.title)
    print()
    print(game_round.task)
    print()

    while True:
        pattern = input("Введите регулярное выражение (? - подсказка): ")

        if pattern == "?":
            print("Подсказка:", game_round.hint)
            continue

        success, message = game_round.check(pattern)
        print(message)

        if success:
            print("Улика:", game_round.clue)
            clues.append(game_round.clue)
            break

        print("Попробуйте ещё раз.")
        print()

print()
print("Все улики собраны:")
for clue in clues:
    print(clue)
print("Вор - завхоз Громов. Дело закрыто!")
