import cv2
import time


video_name = 'MOT17-04-DPM.mp4'

# Video içe aktar: capture, cap
cap = cv2.VideoCapture(video_name)

print('Genişlik: ', cap.get(3))
print('Yükseklik: ', cap.get(4))

if cap.isOpened() == False:
    print('Hata')

while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01) # uyarı: kullanmazsak çok hızlı akar.
        cv2.imshow('Video', frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # stop capture
cv2. destroyAllWindows()

# cv2.VideoCapture(video_name) satırı, belirtilen video dosyasını ('video_name') içe aktarmak için bir 'VideoCapture' nesnesi oluşturur.

# 'cap.get(3)' ve 'cap.get(4)' satırları, video dosyasının genişliğini ve yüksekliğini alır ve ekrana yazdırır.

# 'cap.isOpened()' satırı, video dosyasının başarıyla açılıp açılmadığını kontrol eder. Eğer dosya başarıyla açılamazsa, ekrana 'Hata' mesajı yazdırılır.

# while True döngüsü, videoyu oynatmak için sonsuz bir döngü oluşturur.

# 'cap.read()' satırı, bir sonraki kareyi ('frame') ve bir geri dönüş değeri ('ret') döndürür. 'ret' değeri, kameranın veya video dosyasının hala kare döndürüp döndürmediğini gösterir.

# 'if ret == True' bloğu, 'ret' değerinin 'True' olduğunu kontrol eder, yani bir sonraki karenin alındığını belirtir. Ardından, 'time.sleep(0.01)' satırı, video akışının çok hızlı olmaması için 0.01 saniye uyku verir.

# 'cv2.waitKey(1) & 0xFF == ord('s')' satırı, kullanıcının 'q' tuşuna basıp basmadığını kontrol eder. Eğer basılmışsa, döngüyü kırar ve video oynatmayı durdurur.

# 'cap.release()' satırı, video yakalama kaynağını serbest bırakır ve kullanılan belleği temizler.

# 'cv2.destroyAllWindows()' satırı, açık olan tüm OpenCV pencerelerini kapatır ve belleği temizler. 