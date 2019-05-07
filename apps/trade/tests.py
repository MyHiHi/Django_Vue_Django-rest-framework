from django.test import TestCase

# Create your tests here.
import shutil
p='D:\Documents\我的资料\实习\日志\保定学院学生实习日志1篇.DOC'

for i in range(2,9):
    shutil.copyfile(p,'D:\Documents\我的资料\实习\日志\保定学院学生实习日志{0}篇.DOC'.format(i))
