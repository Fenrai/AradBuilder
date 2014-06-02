import ConfigParser
from _pyio import __metaclass__
import os

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Paths():
    __metaclass__ = Singleton

    def __init__(self):
#         pathParser = ConfigParser.SafeConfigParser()
#         pathParser.read('paths.abp')
        classParser = ConfigParser.SafeConfigParser()
        classParser.read(os.path.join('classes', 'classes.abc'))
        self.createPictureDicts(classParser)
        self.createFileDict(classParser)

    def createPictureDicts(self, classParser):
        self.charPicturePaths = {}
        self.skillPicturePaths = {}
        for mainClass in classParser.sections():
            self.charPicturePaths[mainClass] = os.path.join('classes', mainClass)
            self.skillPicturePaths[mainClass + '.Common'] = \
                os.path.join('skills', mainClass, 'Common')
            for subClass in classParser.options(mainClass):
                name = classParser.get(mainClass, subClass)
                self.skillPicturePaths[mainClass + '.' + name] = \
                os.path.join('skills', mainClass, name)

        for point in ['QP', 'SP', 'TP']:
            self.skillPicturePaths['General.' + point] = \
                os.path.join('skills', 'General', point)

    def createFileDict(self, classParser):
        self.skillFilePaths = {}
        for mainClass in classParser.sections():
            self.skillFilePaths[mainClass] = os.path.join('skills', mainClass)
        self.skillFilePaths['General'] = os.path.join('skills', 'General')

    def getSPicPath(self, mainClass, subClass):
            return self.skillPicturePaths[mainClass + '.' + subClass]

    def getCPicPath(self, mainClass):
            return self.charPicturePaths[mainClass]

    def getFilePath(self, mainClass):
        return self.skillFilePaths[mainClass]


if __name__ == '__main__':
    paths = Paths()
    path2 = Paths()

    paths.charPicturePaths['a'] = 1
    print path2.charPicturePaths['a']

    print paths.charPicturePaths
    print '---------------------------------------'
    print paths.skillPicturePaths
    print '---------------------------------------'
    print paths.skillFilePaths
    print '---------------------------------------'
    print paths.getPicturePath('skill', 'Gunner (F)', 'Mechanic')
    print paths.getPicturePath('skill', 'General', 'TP')
    print paths.getPicturePath('char', 'Gunner (F)')
