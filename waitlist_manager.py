class Node:
    """A single node in the singly linked list.

    Stores a customer's name and a reference to the next Node in the list.
    """

    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    """A singly linked list used to manage an event waitlist."""

    def __init__(self):
        self.head = None

    def add_front(self, name):
        """Add a customer to the front of the waitlist (e.g. VIPs)."""
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        """Add a customer to the end of the waitlist (general customers)."""
        new_node = Node(name)

        # Empty list: the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        # Otherwise, walk to the last node (the one whose next is None).
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        """Remove the first node matching `name` from the waitlist."""
        current = self.head
        previous = None

        while current is not None:
            if current.name == name:
                if previous is None:
                    # Removing the head node: move head to the next node.
                    self.head = current.next
                else:
                    # Removing a middle/last node: skip over it.
                    previous.next = current.next
                return f"Removed {name} from the waitlist"

            previous = current
            current = current.next

        return f"{name} not found"

    def print_list(self):
        """Print every name currently on the waitlist, in order."""
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        current = self.head
        while current is not None:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    """Run an interactive command-line waitlist manager."""
    waitlist = LinkedList()

    menu = (
        "\n--- Waitlist Manager ---\n"
        "1. Add customer to front\n"
        "2. Add customer to end\n"
        "3. Remove customer by name\n"
        "4. Print waitlist\n"
        "5. Exit"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter customer name to add to front: ").strip()
            waitlist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ").strip()
            message = waitlist.add_end(name)
            print(message)
        elif choice == "3":
            name = input("Enter customer name to remove: ").strip()
            message = waitlist.remove(name)
            print(message)
        elif choice == "4":
            waitlist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    waitlist_generator()
    