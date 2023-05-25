# while True:
#     outcome = input("Throw the coin and enter head or tail here: ? ")
#     match outcome:
#         case "head" | "tail":
#             with open("outcome_entries.txt", "a") as file:
#                 file.write(outcome + "\n")
#             number_heads = 0
#             number_tails = 0
#             with open("outcome_entries.txt", "r") as file:
#                 entries = file.readlines()
#                 for entry in entries:
#                     match entry.strip("\n"):
#                         case "head":
#                             number_heads += 1
#                         case "tail":
#                             number_tails += 1
#
#             heads_probability = number_heads * 100 / (number_heads + number_tails)
#             print(f"Heads: {heads_probability}%")
#         case "exit":
#             break


# This code is shorter because we have to think that saving the input is just a side job. Start simple without thinking
# of saving the data, and it will be shorter and clearer like this. And also, use the count method of lists instead of
# re-writing everything again
while True:
    with open("outcome_entries.txt", "r") as file:
        entries = file.readlines()

    outcome = input("Throw the coin and enter head or tail here: ? ")

    if outcome == "exit":
        break

    entries.append(outcome + "\n")

    with open("outcome_entries.txt", "w") as file:
        file.writelines(entries)

    number_heads = entries.count("head\n")
    heads_probability = number_heads * 100 / len(entries)
    print(f"Heads: {heads_probability}%")
