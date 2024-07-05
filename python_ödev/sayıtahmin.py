import tkinter as tk  # Tkinter kütüphanesini 'tk' olarak import ediyoruz, GUI uygulamaları için kullanacağız.GUI (Graphical User Interface), yani Grafik Kullanıcı Arayüzü, kullanıcıların yazılımla etkileşime geçmesi için görsel elemanlar sunan bir arayüzdür. 
import random  # Rastgele sayı üretmek için 'random' kütüphanesini import ediyoruz.

class NumberGuessingGame:  # 'NumberGuessingGame' adında bir sınıf tanımlıyoruz.
    def __init__(self, master):  # Sınıfın yapıcı (constructor) fonksiyonu, GUI bileşenlerini burada tanımlıyoruz.
        self.master = master  # Ana pencereyi (master) sınıfın bir üyesi yapıyoruz.
        self.master.title("Numara Tahmin Oyunu")  # Pencerenin başlığını "Number Guessing Game" olarak ayarlıyoruz.

        self.new_game()  # "new_game" adında Yeni bir oyun başlatıyoruz.

        self.guess_label = tk.Label(master, text="1-100 arasında bir sayı giriniz")  # Tahmin girişi için bir yazı oluşturuyoruz.
        self.guess_label.pack()  # yazıyı pencereye ekliyoruz.

        self.guess_entry = tk.Entry(master)  # Kullanıcının tahminini gireceği bir giriş alanı(text area) oluşturuyoruz.
        self.guess_entry.pack()  # Giriş alanını(text area) pencereye ekliyoruz.

        self.submit_button = tk.Button(master, text="Gönder", command=self.check_guess)  # Tahmini kontrol edecek bir buton oluşturuyoruz.
        self.submit_button.pack()  # butonu pencereye ekliyoruz.

        self.result_label = tk.Label(master, text="")  # Sonuçları gösterecek bir yazı oluşturuyoruz.
        self.result_label.pack()  # Sonuç yazısını pencereye ekliyoruz.

    def new_game(self):  # Yeni bir oyun başlatmak için bir fonksiyon tanımlıyoruz.ve  "new_game" adını veriyoruz. 
        self.secret_number = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı seçiyoruz.

    def check_guess(self):  # Kullanıcının tahminini kontrol eden fonksiyon.
        try:   # Kullanıcının girişinin geçerli olup olmadığını kontrol ediyoruz.
            guess = int(self.guess_entry.get())  # Kullanıcının girişini tam sayıya çeviriyoruz.
            if guess == self.secret_number:  # Eğer tahmin doğruysa:
                self.result_label.config(text="Tebrikler doğru numarayı buldunuz")  # Kullanıcıyı tebrik ediyoruz.
                self.new_game()  # Yeni bir oyun başlatıyoruz.
            elif guess < self.secret_number:  # Eğer tahmin gizli sayıdan küçükse:
                self.result_label.config(text="Maalesef,daha yüksek bir sayı söylemelisiniz.")  # Kullanıcıya daha yüksek bir sayı denemesini söylüyoruz.
            else:  # Eğer tahmin gizli sayıdan büyükse:
                self.result_label.config(text="Çok yüksek,şimdi daha düşük bir sayı söyleyebilirsiniz.")  # Kullanıcıya daha düşük bir sayı denemesini söylüyoruz.
        except ValueError:  # Eğer kullanıcı geçersiz bir giriş yaparsa:
            self.result_label.config(text="Please enter a valid number.")  # Kullanıcıya geçerli bir sayı girmesini söylüyoruz.

def main():  # Ana fonksiyonu tanımlıyoruz.
    root = tk.Tk()  # Tkinter ana penceresini oluşturuyoruz.
    game = NumberGuessingGame(root)  # 'NumberGuessingGame' sınıfından bir oyun örneği oluşturuyoruz.
    root.mainloop()  # Pencereyi çalıştırıyoruz,kullanıcıdan gelen etkileşimleri bekliyoruz

if __name__ == "__main__":  # Eğer bu dosya doğrudan çalıştırılıyorsa:
    main()  # Ana fonksiyonu çağırıyoruz.
