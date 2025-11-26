import yaml

with open(r"C:\Users\Veena madhuri\Downloads\docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ip = list(service.get("networks", {}).values())[0].get("ipv4_address")
    deps = service.get("depends_on", [])
    print(f"{name} -> IP: {ip}, Depends On: {deps}")
    
    
    
    
# import yaml
# yaml_path = r"C:\Users\Veena madhuri\Downloads\docker-compose-basic-nrf.yaml"

# def env_to_dict(env):
#     result = {}
#     if isinstance(env, dict):
#         return {str(k): str(v) for k, v in env.items()}
#     elif isinstance(env, list):
#         for item in env:
#             if isinstance(item, str) and "=" in item:
#                 k, v = item.split("=", 1)
#                 result[k] = v
#     return result
# with open(r"C:\Users\Veena madhuri\Downloads\docker-compose-basic-nrf.yaml", "r") as f:
#     data = yaml.safe_load(f)
# services = data.get("services", {})

# for service_name, service_data in services.items():
#     print(f"\nService: {service_name}")
#     env_section = service_data.get("environment", [])
#     env_dict = env_to_dict(env_section)

#     ips = [v for k, v in env_dict.items() if "IP" in k.upper()]
#     if ips:
#         print("  IP Address(es):", ", ".join(ips))
#     else:
#         print("  IP Address(es): None")
#     deps = service_data.get("depends_on")
#     if isinstance(deps, dict):          
#         deps_list = list(deps.keys())
#     elif isinstance(deps, list):        
#         deps_list = deps
#     else:
#         deps_list = []

#     if deps_list:
#         print("  Depends On:", ", ".join(deps_list))
#     else:
#         print("  Depends On: None")
