from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        #//self.resize(800,500) #Pencere boyutu ayarlandı
        #print(self.size())

        #self.move(100,100) #Pencere taşıma ilk sağa, ikinci aşağı kaydırır

        #iki işlemi beraber yapma

        #self.setGeometry(150,150,300,150)
        #print(self.geometry())
        #self.show()
        #self.showMinimized() #Simge durumunda küçülterek pencere açma, örneğin bir butona eklenirken işe yarayabilir
        #self.showMaximized() #Ekranı kapsar
        #self.showFullScreen() 
        #self.showNormal() #Ayarlanan orjinal pencere
        self.setMinimumSize(500, 100) #Pencere ayarlanabilir fakat bundan daha küçük ayarlanamaz
        self.setMaximumSize(1000,500) #Percere ayarlanabilir fakat bundan daha büyük ayarlanamaz
        self.setMaximumHeight(500) #Sadece yüksekliğin max değeri ayarlama
        self.setMinimumHeight(100) #Sadece yüksekliğin min değerini ayarlama
        self.setMinimumWidth(100) #Sadece genişliğin min değerini ayarlama
        self.setMaximumWidth(500) #Sadece genişliğin max değerini ayarlama
        self.setFixedSize(300,300) #Boyutlandırılamayan 
        print(self.geometry())

        self.button = QPushButton("Tıkla", self) #Buton oluşturma
        #self.setDiseabled(True) #Pencerenin içerisindeki bütüm kompenentler inaktif olur
        #self.setEnabled(True) #Pencerenin içerisindeki bütün komponentler aktif olur
        
        self.setWindowTitle("Dememe QT")
        self.setWindowIcon(QIcon("Icon_Resmi_Yolu.png"))
        self.show()
        self.close() #pencereyi kapatma fonksiyonu



app = QApplication([])
window = main()
window.show()
app.exec()

