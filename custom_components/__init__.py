DOMAIN = "ecoflow_powerocean"

def setup(hass, config):
    hass.states.set("ecoflow_powerocean.test", "Hello World!")

    return True # indicate init success
