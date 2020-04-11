from LinkedList import LinkedList


def partition(ll, x):
    


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)
