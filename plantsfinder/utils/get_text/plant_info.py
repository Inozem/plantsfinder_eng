def get_plant_name(plant):
    """Получение названия растения."""
    is_name_cultivar = plant.name_cultivar is not None
    name_cultivar = ['', f'"{plant.name_cultivar}"'][is_name_cultivar]
    plant_name = (f'{plant.name_species_russian} {name_cultivar} '
                  f'({plant.name_species_latin} {name_cultivar})')
    return plant_name


def get_plant_usda_zones_min_max(plant):
    """Получение минимальной и максимальной зон морозостойкости растения."""
    usda_zones = sorted([zone.name for zone in plant.usda_zone.all()])
    return f'{usda_zones[0]}-{usda_zones[-1]}'


def get_plant_sun_types(plant):
    """Получение типов освещенности."""
    return ', '.join([sun.name for sun in plant.sun.all()]).lower()


def get_plant_soil_types(plant):
    """Получение типов почвы."""
    soil_types = [soil.name for soil in plant.soil_type.all()]
    soil_types += [soil.name for soil in plant.soil_fertility.all()]
    text = ', '.join(soil_types[:-1]) + ' и ' + soil_types[-1]
    return text.lower()


def get_plant_soil_ph_min_max(plant):
    """Получение минимальной и максимальной кислотности почвы растения."""
    soil_ph = sorted([ph.name for ph in plant.soil_ph.all()])
    return f'{soil_ph[0]}-{soil_ph[-1]}'


def get_plant_soil_moisture(plant):
    """Получение получение данных о влажности почвы растения."""
    extreme_moisture = {
        'Возможна засуха': 'засуху',
        'Возможны затопления': 'затопления',
    }
    moisture = [ph.name for ph in plant.soil_moisture.all()]
    soil_moisture = []
    soil_extreme_moisture = []
    for moisture_value in moisture:
        if moisture_value not in extreme_moisture:
            soil_moisture.append(moisture_value)
        else:
            soil_extreme_moisture.append(moisture_value)
    text = ''
    if len(soil_moisture) > 1:
        text += ', '.join(soil_moisture[:-1])
        text += f' и {soil_moisture[-1]}'
    elif len(soil_moisture) == 1:
        text += soil_moisture[0]
    if len(soil_extreme_moisture) > 0:
        for ind, moisture_name in enumerate(soil_extreme_moisture):
            soil_extreme_moisture[ind] = extreme_moisture[moisture_name]
        text += ', может переносить '
        if len(soil_extreme_moisture) == 1:
            text += soil_extreme_moisture[0]
        else:
            text += ' и '.join(soil_extreme_moisture)
    return text.lower()