def validate_duration(duration):
    try:
        int(duration)
        if duration < 0:
            return False
        return True
    except ValueError:
        return False


def name_length(name):
    if len(name) > 100:
        return False
    return True


def validate_participants(particapants):
    list_participants = particapants.split(",")
    if len(list_participants) > 10:
        return False
    for name in list_participants:
        if len(name) > 100:
            return False
    return True
