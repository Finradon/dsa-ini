from enemies.melee_fighter import melee_fighter

# label to class name for file import
def map_entities(label):
    ret = None
    if label == 'Gegner (Nahkampf)':
        ret = melee_fighter
    elif label == 'Gegner (Fernkampf)':
        pass
    elif label == 'Dämon':
        pass
    return ret
