class hewan:
    def __init__(self, data):
        self.spesies = data
    

    def banding(self,angkaA, angkaB):
        if self.spesies[angkaA]['genus'] == self.spesies[angkaB]['genus']:
            return 'genus sama'
        else:
            return 'genus beda'


data = {
    1: {
        'famili' : 'Ursidae', 
        'genus': 'A',
        'spesis': 'Alluropoda'},
    2: {
        'famili' : 'Caridae', 
        'genus': 'Canis',
        'spesis': 'Canis adustus'},
    3: {
        'famili' : 'caridae', 
        'genus': 'Vulpes',
        'spesis': 'Vulpes corsac'},
    4: {
        'famili' : 'caridae', 
        'genus': 'Vulpes',
        'spesis': 'vulpes bengalensis'},
    5: {
        'famili' : 'caridae', 
        'genus': 'Canis',
        'spesis': 'Canis lupus'},
    }
a = hewan(data)
print(a.banding(2,3))