bays = 1 # 16
units = 2 # 4

with open("NETMAP", "w", encoding="utf-8") as f:
    for bay in range(0, bays):
        for unit in range(0, units):
            f.write("{iouyap_id}:{bay}/{unit}{iou_id:>5d}:{bay}/{unit}\n".format(iouyap_id=str(1 + 512),
                                                                                 bay=bay,
                                                                                 unit=unit,
                                                                                 iou_id=1))


import configparser

iouyap_ini = "iouyap.ini"

config = configparser.ConfigParser()
config["default"] = {"netmap": "NETMAP",
                     "base_port": "49000"}

ethernet_id = 0
for bay_id in range(0, bays):
    for unit_id in range(0, units):
        connection = {"eth_dev": "eth{ethernet_id}".format(ethernet_id=ethernet_id)}
        ethernet_id += 1

        interface = "{iouyap_id}:{bay}/{unit}".format(iouyap_id=str(1 + 512), bay=bay_id, unit=unit_id)
        config[interface] = connection
        unit_id += 1
    bay_id += 1

with open(iouyap_ini, "w", encoding="utf-8") as config_file:
    config.write(config_file)
