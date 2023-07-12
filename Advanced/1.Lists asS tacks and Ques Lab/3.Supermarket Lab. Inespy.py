# from collections import deque
#
#
# customers = deque()
# while True:
#
#     name = input()
#     if name == "Paid":
#         while customers:
#             print(customers.popleft())
#         continue
#     elif name == "End":
#         break
#     customers.append(name)
#
# print(f"{len(customers)} people remaining.")

from collections import deque

class CustomerQueue:
    def __init__(self):
        self.customers = deque()

    def process_customers(self):
        while True:
            name = input()
            if name == "Paid":
                while self.customers:
                    print(self.customers.popleft())
                continue
            elif name == "End":
                break
            self.customers.append(name)

        print(f"{len(self.customers)} people remaining.")


queue = CustomerQueue()
queue.process_customers()