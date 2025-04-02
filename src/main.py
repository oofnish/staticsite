import os.path
import shutil

from textnode import TextNode, TextType

def copy_static(path, srcpath, destpath):
    srcdir = os.path.join(srcpath,path)
    destdir = os.path.join(destpath,path)
    if not os.path.exists(destdir):
        print(f"Making dir {destdir}")
        os.mkdir(destdir)

    entries = os.listdir(srcdir)
    for e in entries:
        entpath = os.path.join(srcdir, e)
        entdst = os.path.join(destdir, e)
        if os.path.isfile(entpath):
            print(f"Copying file {entpath} to: {entdst}")
            shutil.copy(entpath, entdst)
        else:
            print(f"Entering Dir {entpath}.")
            copy_static(e, srcdir, destdir)



def publish_static():
    #if os.path.exists('public'):
    #    shutil.rmtree('public')
    #os.mkdir('public')
    copy_static('' , 'static', 'public')

def main():
    publish_static()

if __name__ == '__main__':
    main()