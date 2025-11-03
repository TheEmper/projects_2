test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(settings, key_value_pair):

    for i in range(0, len(key_value_pair), 2):
        key = key_value_pair[i].lower()
        val = key_value_pair[i+1].lower()
        if key in settings:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
            break
        else:
            settings[key] = val
            return f"Setting '{key}' added with value '{val}' successfully!"
            

def update_setting(settings, key_value_P):

    for i in range(0, len(key_value_P), 2):
        key = key_value_P[i].lower()
        val = key_value_P[i+1].lower()
        if key in settings:
            settings[key] = val
            return f"Setting '{key}' updated to '{val}' successfully!"
        else:
            return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
            break

def delete_setting(settings, just_key):
    key = just_key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    full_string = "Current User Settings:\n"
    if not settings:
        return "No settings available."
    else:
        for key, value in settings.items():
            key = key.capitalize()
            full_string += f"{key}: {value}\n"
    
    return full_string

print(add_setting({'theme': 'light'}, ('VOLUME', 'high')))
print(update_setting(test_settings, ('notifications', 'veryon')))
print(view_settings(test_settings))