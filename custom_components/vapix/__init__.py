from requests import post
from requests.auth import HTTPDigestAuth

import json

from .const import (
    DOMAIN
)


def setup(hass, config):

    def open_remote_door(call):
        ip = call.data.get("ip", "")
        username = call.data.get("username", "")
        password = call.data.get("password", "")
        doorid = call.data.get("doorid", "")

        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "tdc:AccessDoor":  {
                "Token": doorid
            }
        }

        post("http://" + username + ":" + password + "@" + ip + "/vapix/doorcontrol",
                        data=json.dumps(payload), headers=headers, auth=HTTPDigestAuth(username, password))

    hass.services.register(DOMAIN, "open_remote_door", open_remote_door)

    return True
