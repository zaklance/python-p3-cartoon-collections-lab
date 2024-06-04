def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f'{num}. {dwarf}')
        num += 1

def summon_captain_planet(list):
    result = []
    for item in list:
        result.append(item.capitalize() + '!')
    return result

def long_planeteer_calls(list):
    for item in list:
        if len(item) < 4:
            return True
        else:
            return False
        
cheeses = ["camembert", "gouda", "cheddar"]

def find_the_cheese(list):
    for item in list:
        if item in cheeses:
            return item