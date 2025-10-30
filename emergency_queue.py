class Patient:
    def __init__(self, name, severity):
        """
        name: patient's name (string) 
        urgency: integer 1-10, where 1 = most urgent 
        """
        if not isinstance(name, str):
            raise TypeError("Patient name must be a string.")
        if not isinstance(urgency, int):
            raise TypeError("Urgency must be an integer.")
        if urgency < 1 or urgency > 10:
            raise ValueError("Urgency must be between 1(most urgent) and 10 (least urgent).")
        
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"Patient(name={self.name!r}, urgency={self.urgency})"



class MinHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def _parent(self, i):
        return (i - 1) // 2
    
    def _left(self, i):
        return 2 * i + 1
    
    def _right(self, i):
        return 2 * i + 2   
    
    def heapify_up(self, index):
        while index > 0:
            parent_index = self._parent(index)
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break


    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left_index = self._left(index)
            right_index = self._right(index)
            smallest = index

            if left_index < size and self.data[left_index].urgency < self.data[smallest].urgency:
                smallest = left_index
            if right_index < size and self.data[right_index].urgency < self.data[smallest].urgency:
                smallest = right_index


            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest
    

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("insert() expects a Patient object.")
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            print("Heap is empty.")
            return None
        return self.data[0]
    

    def remove_min(self):
        if not self.data:
            print("Heap is empty - no patient to remove.")
            return None
        

        root = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self.heapify_down(0)

        return root
    
    def print_heap(self):
        print("Cirrent Queue:")
        if not self.data:
            print("- (empty)")
            return 
        for patient in self.data:
            print(f"- {patient.name} (urgency: {patient.urgency})")



if __name__ == "__main__":
    heap = MinHeap


    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Morgan", 2))

    heap.print_heap()


    top = heap.peek()
    if top: 
        print(f"Next up: {top.name} (urgency: {top.urgency})")

    served = heap.remove_min()
    print(f"Served patient: {served.name}")
    heap.print_heap()

    served = heap.remove_min()
    print(f"Served patient: {served.name}")
    heap.print_heap()

    heap.remove_min()
    heap.remove_min()
    heap.remove_min()

    try: 
        heap.insert(("NotAPatient", 4))
    except TypeError as e:
        print("Caught error:", e)


    try: 
        bad_patient = Patient("Sam", 15)
    except ValueError as e:
        print("Caught error:", e)
