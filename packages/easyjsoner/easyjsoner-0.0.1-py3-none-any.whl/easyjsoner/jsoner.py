import json


class jsoner():
    data = None
    last_path = None
    setted_path = None

    @classmethod
    def read(self, path):
        if (not self.data) or (self.last_path != path):
            with open(path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
                self.last_path = path
                print('read')

        return self.data


    @classmethod
    def read_from(self, path, path_in):
        if (not self.data) or (self.last_path != path):
            with open(path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

        mods = path_in.split('/')
        load = self.data
        for l in mods:
            try:
                load = load[l]
            except:
                return None
        return load


    @classmethod
    def write(self, path, data):
        with open(path, 'w', encoding='utf-8') as f:
            return json.dump(data, f, indent=4)
