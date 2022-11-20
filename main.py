from cloud import cloud
from sun import sun
from song import song
from grass import grass


def main():
    if cloud and sun and song and grass:
        pic = cloud() + sun() + song() + grass()
        for s in pic:
            print(s)
    else:
        print("Собери все детали!")

if __name__ == '__main__':
    main()
