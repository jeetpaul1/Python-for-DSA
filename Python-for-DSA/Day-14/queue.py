#Write a Python program to simulate a queue for customer support tickets. The program should allow:

# 1 - Adding a new ticket to the queue.
# 2 - Serving the next ticket (dequeue).
# 3 - Viewing the next ticket in the queue.



from collections import deque  #solution

class SupportQueue:
    def __init__(self):
        self.queue = deque()

    def add_ticket(self, ticket):
        """
        Add a new ticket to the queue.

        Args:
            ticket (str): The ticket description.
        """
        self.queue.append(ticket)
        print(f"Ticket added: {ticket}")

    def serve_ticket(self):
        """
        Serve the next ticket in the queue.

        Returns:
            str: The ticket being served, or a message if the queue is empty.
        """
        if self.is_empty():
            return "No tickets to serve."
        return f"Serving ticket: {self.queue.popleft()}"

    def next_ticket(self):
        """
        View the next ticket in the queue without serving it.

        Returns:
            str: The next ticket, or a message if the queue is empty.
        """
        if self.is_empty():
            return "No tickets in the queue."
        return f"Next ticket: {self.queue[0]}"

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

# Example usage
support_queue = SupportQueue()

# Adding tickets
support_queue.add_ticket("Issue with login")
support_queue.add_ticket("Error in payment processing")
support_queue.add_ticket("Feature request: Dark mode")

# Viewing the next ticket
print(support_queue.next_ticket())

# Serving tickets
print(support_queue.serve_ticket())
print(support_queue.serve_ticket())
print(support_queue.serve_ticket())

# Trying to serve from an empty queue
print(support_queue.serve_ticket())
