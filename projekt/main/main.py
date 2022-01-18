from detector import detector
import glob

for path in glob.glob('.\\images\\*'):
    print(path)
    detector(path)
