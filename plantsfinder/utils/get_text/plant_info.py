def get_plant_name(plant):
    """Returns the name of a plant."""
    is_name_cultivar = plant.name_cultivar is not None
    name_cultivar = ['', f'"{plant.name_cultivar}"'][is_name_cultivar]
    plant_name = (f'{plant.name_species_english} {name_cultivar} '
                  f'({plant.name_species_latin} {name_cultivar})')
    return plant_name


def get_plant_usda_zones_min_max(plant):
    """Returns the minimum and maximum USDA zones of the plant."""
    usda_zones = sorted([zone.name for zone in plant.usda_zone.all()])
    return f'{usda_zones[0]}-{usda_zones[-1]}'


def get_plant_sun_types(plant):
    """Returns sun exposure types of the plant."""
    return ', '.join([sun.name for sun in plant.sun.all()]).lower()


def get_plant_soil_types(plant):
    """Returns soil types of the plant."""
    soil_types = [soil.name for soil in plant.soil_type.all()]
    soil_types += [soil.name for soil in plant.soil_fertility.all()]
    text = ', '.join(soil_types[:-1]) + ' and ' + soil_types[-1]
    return text.lower()


def get_plant_soil_ph_min_max(plant):
    """
    Returns the minimum and maximum optimal level of soil pH of the plant.
    """
    soil_ph = sorted([ph.name for ph in plant.soil_ph.all()])
    return f'{soil_ph[0]}-{soil_ph[-1]}'


def get_plant_soil_moisture(plant):
    """Returns soil moisture types of the plant."""
    extreme_moisture = ['Drought possible', 'Flooding possible']
    moisture = [moisture.name for moisture in plant.soil_moisture.all()]
    soil_moisture = []
    soil_extreme_moisture = []
    for moisture_value in moisture:
        if moisture_value not in extreme_moisture:
            soil_moisture.append(moisture_value)
        else:
            soil_extreme_moisture.append(moisture_value.split(' ')[0])
    text = ''
    if len(soil_moisture) > 1:
        text += ', '.join(soil_moisture[:-1])
        text += f' and {soil_moisture[-1]}'
    elif len(soil_moisture) == 1:
        text += soil_moisture[0]
    if len(soil_extreme_moisture) > 0:
        text += ', can tolerate '
        if len(soil_extreme_moisture) == 1:
            text += soil_extreme_moisture[0]
        else:
            text += ' and '.join(soil_extreme_moisture)
    return text.lower()
