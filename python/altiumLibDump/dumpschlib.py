from io import StringIO
import optparse
import json

from pprint import pprint


filter = ['Designator', 
            'Manufacturer', 
            'Manufacturer Part Number',
            'Supplier 1',
            'Supplier Part Number 1',
            'Supplier 2',
            'Supplier Part Number 2',
            'Supplier 3',
            'Supplier Part Number 3']

# filter = []


class Component:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)


def parse(text,filter):
    for part in text.split("RECORD=1|"):
        if "LibReference" in part:
            p = {}
            for t in part.split("|"):
                if "LibReference" in t:
                    libref = t.split("=")[-1]

            for record in part.split("RECORD="):
                # param:
                if record.startswith("41") or record.startswith("34"):
                    param = {}
                    for entry in record.split("|"):
                        key = entry.split("=")[0].strip()
                        val = entry.split("=")[-1].strip()
                        param[key] = val
                    try:
                        if filter != []:
                            if param['Name'] in filter:
                                p[param['Name']] = param['Text']
                        else:
                            p[param['Name']] = param['Text']
                    except KeyError:
                        pass

                if record.startswith("45"):  # model:
                    p['Footprints'] = []
                    for entry in record.split("|"):
                        if "ModelName" in entry:
                            p['Footprints'].append(
                                entry.split("=")[-1])

            parts[libref] = p


if __name__ == "__main__":

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file",
                      dest="fn",
                      type='string',
                      help=".SchLib file to dump")
    (options, args) = parser.parse_args()

    parts = {}
    p = {}
    libref = ""

    with open(options.fn, 'rb') as f:
        try:
            text = f.read().decode(errors='ignore').replace('\n','')
            parse(text,filter)
        except UnicodeDecodeError as e:
            pass

    with open('parts.json', 'w') as f:
        json.dump(parts, f, default=lambda o: o.__dict__,
                  indent=4, sort_keys=True)
