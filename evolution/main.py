from typing import List
from txt_manager import TXTManager
from typing import List

def main():
    txt_manager = TXTManager()
    headers, objects = txt_manager.get_input()

    for i, h in enumerate(headers):
        print(h)
        for obj in objects:
            print(
                obj.id if i==0 else obj.name if i==1
                else obj.weight if i==2 else obj.value
            )
        print('\n')

if __name__=='__main__':
    main()