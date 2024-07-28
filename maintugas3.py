import sys
from PyQt5 import QtWidgets, uic

class HotelApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('tugas3.ui', self)

        # Connect buttons to their respective functions
        self.pushButton.clicked.connect(self.show_guest_list)
        self.pushButton_2.clicked.connect(self.book_room)
        self.pushButton_3.clicked.connect(self.show_room_status)

    def show_guest_list(self):
        # Implement the logic to show the guest list
        print("Daftar Tamu button clicked")

    def book_room(self):
        # Implement the logic to book a room
        print("Pesan Kamar button clicked")

    def show_room_status(self):
        # Implement the logic to show room status
        print("Status Kamar button clicked")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec_())
