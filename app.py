"""Small, network-free example that actually imports the pinned packages."""

import requests
import yaml
from packaging.version import Version


def describe_release(document):
    data = yaml.safe_load(document)
    name = data["name"]
    version = Version(str(data["version"]))
    request = requests.Request("GET", f"https://example.invalid/{name}")
    return f"{name} {version}", request.prepare().url
