from requests import post
from requests.auth import HTTPDigestAuth
from homeassistant.core import HomeAssistant
import json
from homeassistant.core import ServiceCall


def open_remote_door(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    doorid = call.data.get("doorid", "")

    headers = {
        "Content-Type": "application/json",
    }

    payload = {"tdc:AccessDoor":  {"Token": doorid}}

    post(
        "http://{ip}/vapix/doorcontrol".format(ip=ip),
        data=json.dumps(payload),
        headers=headers,
        auth=HTTPDigestAuth(username, password)
    )


def access(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    doorid = call.data.get("doorid", "")

    headers = {
        "Content-Type": "application/json",
    }

    payload = {"tdc:AccessDoor":  {"Token": doorid}}

    post(
        "http://{ip}/vapix/doorcontrol".format(ip=ip),
        data=json.dumps(payload),
        headers=headers,
        auth=HTTPDigestAuth(username, password)
    )


def double_lock(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    doorid = call.data.get("doorid", "")

    headers = {
        "Content-Type": "application/json",
    }

    payload = {"tdc:DoubleLockDoor":  {"Token": doorid}}

    post(
        "http://{ip}/vapix/doorcontrol".format(ip=ip),
        data=json.dumps(payload),
        headers=headers,
        auth=HTTPDigestAuth(username, password)
    )


def unlock(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    doorid = call.data.get("doorid", "")

    headers = {
        "Content-Type": "application/json",
    }

    payload = {"tdc:UnlockDoor":  {"Token": doorid}}

    post(
        "http://{ip}/vapix/doorcontrol".format(ip=ip),
        data=json.dumps(payload),
        headers=headers,
        auth=HTTPDigestAuth(username, password)
    )


def lock(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    doorid = call.data.get("doorid", "")

    headers = {
        "Content-Type": "application/json",
    }

    payload = {"tdc:LockDoor":  {"Token": doorid}}

    post(
        "http://{ip}/vapix/doorcontrol".format(ip=ip),
        data=json.dumps(payload),
        headers=headers,
        auth=HTTPDigestAuth(username, password)
    )
