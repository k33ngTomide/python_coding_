import re
from enum import Enum

def find_state_zone(state) -> str:
    state_enum = {
    "NORTH_CENTRAL" : ["Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"],
    "NORTH_EAST": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
    "NORTH_WEST" : ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"],
    "SOUTH_EAST" : ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"],
    "SOUTH_SOUTH" : ["Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"],
    "SOUTH_WEST" : ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"],
    }

    zone_found = get_zone(state, state_enum)
    zone_change = ""
    match zone_found:
        case "NORTH_CENTRAL": zone_change = "North Central"
        case "NORTH_EAST": zone_change =  "North East"
        case "NORTH_WEST": zone_change =  "North West"
        case "SOUTH_EAST": zone_change = "South East"
        case "SOUTH_SOUTH": zone_change =  "South South"
        case "SOUTH_WEST": zone_change =  "South West"
        case "No zone" :
            print(f"{state} is not a state")
            input_checker()

    return zone_change

def get_zone(state, given_dict) -> str:
    found_zone = "No zone"
    for politicalZone, state_list in given_dict.items():
        for new_state in state_list:
            if state.lower().capitalize() == new_state:
                found_zone = politicalZone
                break

    return found_zone

def input_checker() -> None:
    state_input = input("Enter a state to get the geopolitical zone: ")
    if state_input.isdigit() or re.search("^[0-9]*[.]", state_input):
        print("Input cannot be Numbers or contain special character")
        input_checker()
    state_zone = find_state_zone(state_input)
    print(state_zone)


if __name__ == '__main__':
    input_checker()





