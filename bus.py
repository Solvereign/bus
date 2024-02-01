import requests
import json
def bus_info(bus_code, point):
    """ point нь start эсвэл end гэсэн утга авна """


    r = requests.post("https://api.u-money.mn/travel/bus_line_detail/" + bus_code +  "/" + point)
    info = r.json()

    if info['result_code'] == '001':
        del info["end_time_at_start_point"]
        del info["result_code"]
        del info["weekday_interval"]
        del info[ "start_time_at_end_point"]
        del info["holiday_interval"]    
        del info["start_time_at_start_point"]
        del info["line_type"]
        del info["end_time_at_end_point"]

        for station in info["station_list"]:
            del station["exist_bus"]
            del station["station_seq"]
        return info
    elif info['result_code'] == '002':
        return "Арай аймар ачааллуулаад байна !00000000000000000000000000"
    else:
        return "00000000000000000000000000000000000000000000000000000000"

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


ir = requests.post("https://api.u-money.mn/travel/bus_lines")
bus_lines = ir.json()
len = len(bus_lines)
all = []
for bus in bus_lines:
    all.append(bus_info(bus["id"], "start"))
    all.append(bus_info(bus["id"], "end"))
# all.append(bus_info(bus_lines[0]["id"], "start"))
# all.append(bus_info(bus_lines[0]["id"], "end"))

file = open("bus_lines.json", "w", encoding='utf8')
# file.write(listToString(all))
json.dump(all, file, ensure_ascii=False)
file.close()






