from algorithms.mr_rubix import Rubix
from structs.stack import Stack
from structs.linked_list import LinkedList

def main():
    bot = Rubix()

    # Example with Stack
    bot.set_data_structure(Stack())
    bot.data_structure.push(1)
    bot.data_structure.push(2)
    print("Stack elements:")
    bot.show()

    # Example with LinkedList
    bot.set_data_structure(LinkedList())
    bot.data_structure.addAtHead(2)
    bot.data_structure.addAtHead(4)
    bot.data_structure.addAtHead(7)

    print("LinkedList elements:")
    bot.show()

if __name__ == "__main__":
    main()
