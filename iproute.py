import json
file_path = "json_file.txt"
routes = []
with open(file_path) as f:
	for line in f:
		words = line.strip().split()
		# default values
		data = {
	    		"route":words[0],
	    		"interface":None,
	    		"protocol":None,
	    		"source":None,
	    		"metric":None
		}
		#scan line for keywords
		for i in range(1, len(words)):
			if words[i] == "via":
		   		data["source"] = words[i+1]
			elif words[i] == "dev":
		   		data["interface"] = words[i+1]
			elif words[i] == "proto":
		   		data["protocol"] = words[i+1]
			elif words[i] == "src":
		   		data["source"] = words[i+1]
			elif words[i] == "metric":
		   		data["metric"] = words[i+1]
		routes.append(data)
#save to json
with open("routes.json","w") as out:
	json.dump(routes,out,indent=2)
print("Conversion complete - routes.json created")
