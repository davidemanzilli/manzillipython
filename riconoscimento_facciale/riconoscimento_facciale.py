import face_recognition
import cv2
from gtts import gTTS
from playsound import playsound 

def sintesi_vocale2(testo):
    tts = gTTS(text=testo, lang='it')
    tts.save("riconoscimento_facciale/results.mp3")
    playsound("riconoscimento_facciale/results.mp3")


def face_match(image1, image2): 
    # lavoro sulla prima immagine
    first_image = face_recognition.load_image_file(image1)
    encode_image = face_recognition.face_encodings(first_image)[0]

    # lavoro sulla seconda immagine
    second_image = face_recognition.load_image_file(image2)
    encode_image2 = face_recognition.face_encodings(second_image)[0]

    # confronto le immagini 
    match= face_recognition.compare_faces([encode_image], encode_image2)
    
    #TERMINATO IL MATCH TRA LE IMMAGINI 
    # LAVORO SU ENTRAMBE LE IMMAGINI PER AVERE L'INQUADRATURA SUL VOLTO 

    #Trovo la posizione dei volti nelle immagini 
    posizione_faccia = face_recognition.face_locations(first_image)
    posizione_faccia2 = face_recognition.face_locations(second_image)

    #lavoro con cv2 sulle immagini 
    img =cv2.imread(image1)
    img2 =cv2.imread(image2)

    #   inquadratura
    for (top, right, bottom, left) in posizione_faccia:
        cv2.rectangle(img, (left, top), (right, bottom), (0,0,255))
    
    #   inquadratura seconda immagine 
    for (top, right, bottom, left) in posizione_faccia2:
        cv2.rectangle(img2, (left, top), (right, bottom), (229, 43, 80))
    
    # Visualizzo le immagini a schermo 
    cv2.imshow("immagine", img)
    cv2.imshow("immagine 2", img2)
    
    #restituisco vocalemnte il risultato del match 
    sintesi_vocale2(testo = "è lui!" if match[0] else "Non è lui ")
    
    #ciclo per terminare con un comando lo script 
    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

face_match("riconoscimento_facciale\obama.jpg", "riconoscimento_facciale\obama1.jpg")



