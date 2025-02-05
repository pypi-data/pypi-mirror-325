import sys
import os
sys.path.append('../oofempostpy')
import timeCount as timeCount
import hm2of2d as hm2of2d
import hm2of3d as hm2of3d

## count time and iterations required for each increment
timeCount.log2csv('./extractorTest.log', 'extractorTest.csv')

### two materials: one is concrete, another is steel
# 2d
hm2of2d.hm2of2d('circleTPB_cps4.inp','circleTPB_cps4.in')
# 3d
hm2of3d.hm2of3d('circleTPB_c3d8r.inp','circleTPB_c3d8r.in')

hm2of2d.hm2of2d('threeMaterials.inp','threeMaterials.in')

# os.system('python ../oofempostpy/extract.py -f extractorTest.in > extractorTest.csv')