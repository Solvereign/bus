def bus_info(bus_code, point):
    """ point нь start эсвэл end гэсэн утга авна """

    import requests

    r = requests.post("https://api.u-money.mn/travel/bus_line_detail/" + bus_code +  "/" + point)
    info = r.json()

    if info['result_code'] == '001':
        return info
    elif info['result_code'] == '002':
        return "Арай аймар ачааллуулаад байна !"
    else:
        return "Нэг л *аахгүй байна."

if __name__ == "__main__":
    print (bus_info("11100720", "start"))

print("hello")
    