import face_recognition
import cv2
from gtts import gTTS
from playsound import playsound 

def sintesi_vocale2(testo):
    tts = gTTS(text=testo, lang='it')
    tts.save("riconoscimento_facciale/results.mp3")
    playsound("riconoscimento_facciale/results.mp3")


def face_match(image1, image2, image3): 
    # lavoro sulla prima immagine
    first_image = face_recognition.load_image_file(image1)
    encode_image = face_recognition.face_encodings(first_image)[0]

    # lavoro sulla seconda immagine
    second_image = face_recognition.load_image_file(image2)
    encode_image2 = face_recognition.face_encodings(second_image)[0]

    third_image = face_recognition.load_image_file(image3)
    encode_image3 = face_recognition.face_encodings(third_image)[0]

    multiple_image_encode = [
        encode_image,
        encode_image2,
    ]

    # confronto le immagini 
    match= face_recognition.compare_faces(multiple_image_encode, encode_image3)
    
    #TERMINATO IL MATCH TRA LE IMMAGINI 
    # LAVORO SU ENTRAMBE LE IMMAGINI PER AVERE L'INQUADRATURA SUL VOLTO 

    #Trovo la posizione dei volti nelle immagini 
    posizione_faccia = face_recognition.face_locations(first_image)
    posizione_faccia2 = face_recognition.face_locations(second_image)
    posizione_faccia3 = face_recognition.face_locations(third_image)

    #lavoro con cv2 sulle immagini 
    image=[

    cv2.imread(image1),
    cv2.imread(image2),
    cv2.imread(image3)

    ]
    
    
    #   inquadratura
    for (top, right, bottom, left) in posizione_faccia:
        cv2.rectangle(image[0], (left, top), (right, bottom), (0,0,255))
    
    #   inquadratura seconda immagine 
    for (top, right, bottom, left) in posizione_faccia2:
        cv2.rectangle(image[1], (left, top), (right, bottom), (229, 43, 80))
    
        #   inquadratura terza immagine 
    for (top, right, bottom, left) in posizione_faccia3:
        cv2.rectangle(image[2], (left, top), (right, bottom), (85, 107, 47))
    
    # Visualizzo le immagini a schermo 
    for x in range(len(image)):
        cv2.imshow("immagine"+str(x), image[x])
    
    #restituisco vocalemnte il risultato del match 
    sintesi_vocale2(testo = "riconoscimento facciale eseguito correttamente, esito positivo!!" if match[0] else "riconoscimento facciale eseguito correttamente, esito negativo!!")
    
    #ciclo per terminare con un comando lo script 
    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

face_match("riconoscimento_facciale\obama.jpg", "riconoscimento_facciale\prova.jpg", "riconoscimento_facciale\obama1.jpg")

input()



