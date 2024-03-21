from src.dictionary import Dictionary

def test_dictionary():
    states = Dictionary()
    states.set("oregon", "OR")
    states.set("florida", "FL")
    states.set("california", "CA")
    states.set("New York", "NY")
    states.set("Michigan", "MI")

    state_list = states.list()
    assert len(state_list) == 5

    cities = Dictionary()
    cities.set('CA', 'San Francisco')
    cities.set('MI', 'Detroit')
    cities.set('FL', 'Jacksonville')
    print()
    print(cities.list())

    cities.set('NY', 'New York')
    cities.set('OR', 'Portland')

    print('-' * 10)
    print(f"NY state has: {cities.get('NY')}")
    print(f"OR state has: {cities.get('OR')}")

    print('-' * 10)
    print(f"Michigan has: {cities.get(states.get('Michigan'))}")
    print(f"Florida has: {cities.get(states.get('Florida'))}")

    print('-' * 10)
    states.list()

    # print(ever city in state)
    print('-' * 10)
    cities.list()

    print('-' * 10)
    state = states.get('Texas')

    if not state:
        print("Sorry, no Texas")

    city = cities.get('TX', 'Does Not Exist')
    print(f"The city for the state 'TX' {city}")