# VAPIX

This custom integration permits Home Assistant to communicate with `axis` controllers through  http requests.

**Whats does it do?**
- Allow opening the doors/access points

**Tested hardwares**:
- A1001: https://www.axis.com/pt-br/products/axis-a1001

## GETTER STARTED

Paste this property `vapix:` in your configuration file

## SERVICES AVAILABLE

* **vapix.open_remote_door**: Open doors Remote


```yaml
ip: 192.168.0.1
username: admin
password: admin
doorid: 'Axis-000000000:00000000.00000000'
```

* **vapix.get_door_list**: List all doors id's 

```yaml
ip: 192.168.0.1
username: admin
password: admin
```

* **vapix.double_lock**: Double Lock door 

```yaml
ip: 192.168.0.1
username: admin
password: admin
doorid: 'Axis-000000000:00000000.00000000'
```

* **vapix.unlock**: Unlock door. 

```yaml
ip: 192.168.0.1
username: admin
password: admin
doorid: 'Axis-000000000:00000000.00000000'
```

* **vapix.lock**: lock door. 

```yaml
ip: 192.168.0.1
username: admin
password: admin
doorid: 'Axis-000000000:00000000.00000000'
```

## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
# AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/vapix/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
  <tr>
</table>

