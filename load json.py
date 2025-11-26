# import yaml
# import json
# with open(r"C:\Users\Veena madhuri\Downloads\TS24558_Eecs_ServiceProvisioning.yaml") as f:
#     data=yaml.safe_load(f)
# json_data=json.dumps(data,indent=2)
# print(json_data)

# import yaml,json
# with open(r"C:\Users\Veena madhuri\Downloads\TS24558_Eecs_ServiceProvisioning.yaml") as f:
#     j=json.load(f)
# yaml_out=yaml.dump(j,default_flow_style=False)
# print(yaml_out)

import json,yaml
with open(r"C:\Users\Veena madhuri\Downloads\sample2 (1).json") as f:
    j=json.load(f)
yaml_out=yaml.dump(j,default_flow_style=False)
print(yaml_out)