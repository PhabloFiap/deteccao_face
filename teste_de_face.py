import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
# caminho ="fotos/"
# print("Digite o nome da foto")
# d = input()
# caminho += d +".jpg"
# foto = cv2.imread(caminho)
# cv2.imshow("pessoa 1", foto_cinza)
foto = cv2.imread("fotos/varias_faces.jpg")

foto_cinza = cv2.cvtColor(foto,cv2.COLOR_BGRA2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza)

print (faces_detectadas)
for x,y,l,a in faces_detectadas:
    # arquivo da imagem, ponto inicial, ponto final e a cor_BGR, espessura em px
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a),(0,0,255),2)

print(faces_detectadas)
cv2.imshow("pessoa 1", foto)
cv2.waitKey()
