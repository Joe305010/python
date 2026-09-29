animals = {
    'mammals': {
        'land': {
            'carnivores': {
                'big_cats': ['lion', 'tiger'],
                'bears': ['grizzly bear', 'polar bear']
            },
            'herbivores': {
                'large': ['elephant', 'giraffe'],
                'small': ['rabbit', 'deer']
            },
            'omnivores': ['bear', 'human']
        },
        'aquatic': {
            'cetaceans': {
                'toothed_whales': ['dolphin', 'killer whale'],
                'baleen_whales': ['blue whale', 'humpback whale']
            },
            'pinnipeds': {
                'true_seals': ['harbor seal', 'elephant seal'],
                'eared_seals': ['sea lion', 'fur seal']
            }
        }
    },
    'birds': {
        'flightless': {
            'ratites': {
                'large': {
                    'ostrich': {
                        'habitat': 'Savannah',
                        'speed': '70 km/h'
                    }
                },
                'small': ['kiwi', 'cassowary']
            },
            'penguins': ['emperor penguin', 'king penguin']
        },
        'birds_of_prey': {
            'diurnal': ['eagle', 'hawk'],
            'nocturnal': ['owl']
        }
    },
    'reptiles': {
        'snakes': {
            'venomous': ['cobra', 'rattlesnake'],
            'non_venomous': ['python', 'boa constrictor']
        },
        'turtles': ['loggerhead', 'leatherback'],
        'lizards': {
            'iguanas': ['green iguana', 'marine iguana'],
            'geckos': ['leopard gecko', 'crested gecko']
        }
    },
    'amphibians': {
        'anurans': {
            'frogs': ['bullfrog', 'tree frog'],
            'toads': ['American toad', 'cane toad']
        },
        'caudates': ['salamander', 'newt']
    },
    'invertebrates': {
        'arthropods': {
            'insects': {
                'hymenoptera': ['ant', 'bee'],
                'lepidoptera': ['butterfly', 'moth']
            },
            'arachnids': {
                'spiders': ['tarantula', 'black widow'],
                'scorpions': ['emperor scorpion', 'bark scorpion']
            },
            'crustaceans': ['crab', 'lobster']
        },
        'mollusks': {
            'cephalopods': ['octopus', 'squid'],
            'gastropods': ['snail', 'slug']
        }
    }
}

print(animals['reptiles']['lizards']['geckos'][1])