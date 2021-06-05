import face_recognition

def compare_face(image1, image2):
    first_image = face_recognition.load_image_file(image1)
    encode_image = face_recognition.face_encodings(first_image)[0]


    second_image = face_recognition.load_image_file(image2)
    encode_image2 = face_recognition.face_encodings(second_image)[0]

    match= face_recognition.compare_faces([encode_image], encode_image2)

    risultato = "è lui!" if match[0] else "false"

    print(risultato)

compare_face(image1 = "riconoscimento_facciale\prova.jpg", image2= "riconoscimento_facciale\obama1.jpg")



