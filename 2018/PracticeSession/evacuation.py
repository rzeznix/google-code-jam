import basepath
import utils.io as io

test_cases = io.read_int()
for i in range(0, test_cases):
    max_senators = 0
    max_senators_party = ""
    second_max_senators = 0
    second_max_senators_party = ""
    other_parties = {}
    number_of_parties = io.read_int()
    senators_in_party = io.read_ints()

    for index, senators in enumerate(senators_in_party):
        number_of_senators = senators
        party_name = chr(65 + index)
        if number_of_senators >= max_senators:
            second_max_senators = max_senators
            second_max_senators_party = max_senators_party
            max_senators = number_of_senators
            max_senators_party = party_name
        elif number_of_senators > second_max_senators:
            second_max_senators = number_of_senators
            second_max_senators_party = party_name
        other_parties.update({party_name: number_of_senators})

    other_parties.pop(max_senators_party, None)
    other_parties.pop(second_max_senators_party, None)

    senator_order = []
    while max_senators > second_max_senators:
        if max_senators - 2 >= second_max_senators:
            max_senators -= 2
            senator_order.append(max_senators_party + max_senators_party)
        else:
            max_senators -= 1
            senator_order.append(max_senators_party)

    for party, senators in other_parties.items():
        while senators > 1:
            senator_order.append(party + party)
            senators -= 2
        if senators == 1:
            senator_order.append(party)

    while max_senators > 0:
        senator_order.append(max_senators_party + second_max_senators_party)
        max_senators -= 1

    io.out(i + 1, " ".join(senator_order))