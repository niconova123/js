"""
Nama:frankcy pamungkas
Nim:A11.2019.12305
"""

#Double Linked List Non Circular : Stack

class Node:
    def __init__(self, data): #konstruktor
        self.data = data #data
        self.next = None #Inisiasi 
        self.prev = None #Inisiasi 
        
class Stack:
    def __init__(self): #konstruktor
        self.head = None # Inisiasi head atau node awal

# Menambahkan data pada stack
    def push(self, data):
        #jika head kosong, maka data yang dimasukan menjadi head
        if self.head is None:
            self.head = Node(data)
            
        #Jika tidak, maka new node akan diletakan seblum head sekarang
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None # mengarahakan prev ke pointer new node ke None
            self.head = new_node # new node menjadi head
            
        #menghapus data teratas dan mengembalikan data dari Stack
    def pop(self):
        #Jika head kosong maka node kosong
        if self.head is None:
            return None
        
        #jika hanya ada satu node(head), maka hapus node tersebut
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        
        #jika ada data setelah head, hapus head
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp
        
#mengembalikan nilai teratas dalam stack
    def top(self):
        return self.head.data
    
# mengembalikan panjang data dalam stack
    def size(self):
        temp = self.head
        count = 0 # Inisiasi hitung dari 0
        while temp is not None:
            count += 1 #incerment 1 pada count
        # Lakukan sampai node is None
            temp = temp.next
        return count
    
# Menguji apakah Stack kosong atau tidak
    def isEmpty(self):
        if self.head is None: #jika kosong,maka benar
            return True
        else:
            return False # Jika kosong, maka salah
        
#mencetak seluruh data pada stack
    def cetakStack(self):
        print("Stack saat ini:", end="") # Atas <--> bawah
        while temp is not None: #perulangan saat node awal tidak kosong smapai node terakhir dalam keadaan None
            print(temp.data, end = "<-->")
            temp = temp.next # node selanjutnya akan dicetak sampai ke None