import os, json, argparse

def CloneJsonForModes(jsonname, modes):
    if os.path.exists(jsonname):
        with open(jsonname, 'r') as j:
            dict_in_json = json.load(j)
    for x, y in dict_in_json.items():
        for mode in modes:
            dict_in_json[x.replace('standard',mode)] = y
    with open(jsonname, 'w') as j:
        json.dump(obj=dict_in_json, fp=j, indent=2, sort_keys=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json', type=str, default='')
    parser.add_argument('-m', '--modes', nargs='*', default=[])
    args = parser.parse_args()
    CloneJsonForModes(jsonname=args.json, modes=args.modes)

if __name__ == '__main__':
    main()
