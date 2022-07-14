class line:
    def __init__(self, headers, rows):
        for i, j in enumerate(headers):
            setattr(self, j, rows[i])

class Table(list):
    def __init__(self, file, stop=-1):
        table = open(file, 'r').read().split('\n')[:stop]
        self.headers = table[0].split('\t')
        table = table[1:]
        for i in table:
            row = i.split('\t')
            self.append(line(self.headers, row))

    def find(self, key=None):
        res = []
        for i in self:
            if key in i.__dict__.values():
                res.append(i)
        return res


