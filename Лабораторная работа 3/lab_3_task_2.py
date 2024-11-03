def find_common_participants(first_group, second_group, separator=","):
    first_participants = set(first_group.split(separator))
    second_participants = set(second_group.split(separator))
    common_participants = list(first_participants.intersection(second_participants))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", common_participants)
