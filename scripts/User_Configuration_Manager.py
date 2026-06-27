def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings1, setting1):
    key, value = setting1
    key = key.lower()
    value = value.lower()

    if key in settings1:
        settings1[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings2, key):
    key = key.lower()

    if key in settings2:
        settings2.pop(key)
        return f"Setting '{key}' deleted successfully!"

    return f"Setting not found!"


def view_settings(settings3):
    if not settings3:
        return f"No settings available."
    
    result = 'Current User Settings:\n'

    for key, value in settings3.items():
        result += f'{key.capitalize()}: {value}\n'

    return result


test_settings = {
    'theme': 'dark',
    'language': 'english',
    'mode': 'light'
}
