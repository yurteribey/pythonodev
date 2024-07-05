import tkinter as tk  # tkinter modülünü tk olarak içe aktarıyoruz. Bu modül, Python'da grafiksel kullanıcı arayüzleri (GUI) oluşturmak için kullanılır.

class CalculatorApp:  # CalculatorApp adlı bir sınıf tanımlıyoruz. Bu sınıf, hesap makinesi uygulamasının tüm işlevlerini içerecek.
    
    def __init__(self, root):  # Sınıfın kurucu metodunu tanımlıyoruz, root parametresi ana pencereyi temsil ediyor.
        self.root = root  # root parametresini sınıfın bir özelliği olarak saklıyoruz.
        self.root.title("Hesap Makinesi")  # Ana pencerenin başlığını "Simple Calculator" olarak ayarlıyoruz.

        self.entry = tk.Entry(root, width=20, font=('Arial', 14))  # Kullanıcıdan girdi almak için bir giriş kutusu (Entry widget'ı) oluşturuyoruz. Genişliği 20 karakter, yazı tipi Arial 14.
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Giriş kutusunu pencereye yerleştiriyoruz. İlk satıra (row=0), dört sütun boyunca (columnspan=4) ve kenarlık boşlukları (padx ve pady) ile yerleştiriyoruz.

        # Hesap makinesi tuşlarının metin, satır ve sütun bilgilerini içeren bir liste oluşturuyoruz.
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('←', 5, 1)
        ]

        # Listeyi döngü ile gezerek her bir tuş için bir buton oluşturuyoruz.
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),  # Butonları oluşturuyoruz. Genişlik 5, yükseklik 2, yazı tipi Arial 14.
                               command=lambda t=text: self.on_button_click(t))  # Butona tıklandığında on_button_click metodunu çağıracak şekilde ayarlıyoruz.
            button.grid(row=row, column=col, padx=5, pady=5)  # Butonları belirtilen satır ve sütuna yerleştiriyoruz. Her butonun çevresinde 5 birimlik boşluk bırakıyoruz.

    def on_button_click(self, char):  # Buton tıklamalarını işleyen metod.
        if char == '=':  # Eşittir butonuna tıklanırsa:
            try:
                result = eval(self.entry.get())  # Giriş kutusundaki ifadeyi değerlendiriyoruz (hesaplıyoruz).
                self.entry.delete(0, tk.END)  # Giriş kutusunu temizliyoruz.
                self.entry.insert(tk.END, str(result))  # Sonucu giriş kutusuna yazıyoruz.
            except:  # Herhangi bir hata oluşursa:
                self.entry.delete(0, tk.END)  # Giriş kutusunu temizliyoruz.
                self.entry.insert(tk.END, "Error")  # Hata mesajını giriş kutusuna yazıyoruz.
        elif char == 'C':  # C butonuna tıklanırsa:
            self.entry.delete(0, tk.END)  # Giriş kutusunu tamamen temizliyoruz.
        elif char == '←':  # Geri butonuna tıklanırsa:
            current_text = self.entry.get()  # Giriş kutusundaki mevcut metni alıyoruz.
            if len(current_text) > 0:  # Eğer metin varsa:
                self.entry.delete(len(current_text) - 1, tk.END)  # Metnin son karakterini siliyoruz.
        else:  # Diğer tüm butonlar (rakamlar ve işlemler) için:
            self.entry.insert(tk.END, char)  # Tıklanan butonun karakterini giriş kutusuna ekliyoruz.

if __name__ == "__main__":  # Bu kod bloğu, dosya doğrudan çalıştırıldığında çalışır.
    root = tk.Tk()  # Ana pencereyi oluşturuyoruz.
    app = CalculatorApp(root)  # CalculatorApp sınıfının bir örneğini oluşturuyoruz.
    root.mainloop()  # Ana pencere döngüsünü başlatıyoruz, böylece GUI sürekli açık kalır.
