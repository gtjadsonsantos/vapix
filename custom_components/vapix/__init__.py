from requests import post
from requests.auth import HTTPDigestAuth
from homeassistant.core import HomeAssistant
import json

from .const import (
    DOMAIN
)
from .doors import (
    open_remote_door,
    access,
    double_lock,
    lock,
    unlock
)

def setup(hass:HomeAssistant, config):

    def get_door_list(call):
        ip = call.data.get("ip", "")
        username = call.data.get("username", "")
        password = call.data.get("password", "")
        data = {"axtdc:GetDoorList":{}}
       
        r=post("http://{ip}/vapix/doorcontrol".format(ip=ip),
        json.dumps(data),
        auth=HTTPDigestAuth(username, password))
      
        if r.status_code == 200:
            e = json.loads(r.text)

            for k in e['Door']:
                hass.services.call(
                domain="notify",
                service="persistent_notification",
                service_data={ "title": k['Name'], "message": k['token'] })

            return True
        else:
            return False

    hass.services.register(DOMAIN, "open_remote_door", open_remote_door)
    hass.services.register(DOMAIN, "access", access)
    hass.services.register(DOMAIN, "double_lock", double_lock)
    hass.services.register(DOMAIN, "lock", lock)
    hass.services.register(DOMAIN, "unlock", unlock)
    hass.services.register(DOMAIN, "get_door_list", get_door_list)

    
    return True
