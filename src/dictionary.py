from src.double_linked_list import DoubleLinkedList

class Dictionary:
    def __init__(self, num_buckets=256):
        """Initializes a Map with given number of buckets"""
        self.map = DoubleLinkedList() # in real world this is an array
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        """
        Given a key this will create a number and then convert it
        to an index for the Map's buckets.
        """
        return hash(key) % self.map.count()
    
    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)


    def get_slot(self, key, default=None):
        """
        Returns either a bucket and node for a slot or None, None
        """
        bucket = self.get_bucket(key)

        if bucket:
            node = bucket.begin
            i = 0

            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
                    i += 1
        return bucket, None


    def get(self, key, default=None):
        """
        Gets the value in a bucket for the given key, or the default.
        """
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node


    def set(self, key, value):
        """
        sets the key to the value, replacing any existing value.
        """
        bucket, slot = self.get_slot(key)

        if slot:
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))


    def delete(self, key):
        """
        Deletes the given key (and its value) from the map.
        """
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break


    def list(self):
        """
        Prints out what's in the Map.
        """
        output = []
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin

            while slot_node:
                output.append(slot_node.value)
                # print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
        return output
