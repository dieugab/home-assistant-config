"""
Convert Lovelace configuration from "Storage mode" to "YAML" for shareability.
From: https://gist.github.com/ludeeus/bf91cea41f910f3f1f9a7bc98e951ab7

Requirements:
 - PyYAML
 - simplejson
 
"Requirements":
  - Use this or similar script.
  - Use the UI to edit your Lovelace configuration.

Tips:
Change the paths for "READFILE" and "WRITEFILE" To match your installation.
"""

try:
    import simplejson as json
except ImportError:
    print('simplejson missing, install with "pip install simplejson"')
try:
    import yaml
except ImportError:
    print('yaml missing, install with "pip install pyyaml"')

READFILE = "/config/.storage/lovelace"
WRITEFILE = "/config/lovelace.yaml"


def convert():
    """Start convertion."""
    try:
        lljson = open(READFILE, "r+")
        lldata = json.load(lljson)
        lljson.close()
        llyaml = open(WRITEFILE, "w+")
        yaml.dump(lldata["data"]["config"], llyaml, default_flow_style=False)
        llyaml.close()
        print("Convertion done!")
    except Exception as error:  # pylint: disable=broad-except
        errormsg = "Something went wrong - {}".format(error)
        print(errormsg)


convert()