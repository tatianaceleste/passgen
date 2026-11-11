from random import randint
import os

chars = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = list(chars)

encrypted_message = ""

def get_new_encrypted(base_name="encriptado", ext=".txt"):
    i = 0
    while True:
        if i == 0:
            new_filename = f"{base_name}{ext}"
        else:
            new_filename = f"{base_name}{i}{ext}"
        if not os.path.exists(new_filename):
            return new_filename
        i += 1

def get_new_decrypted(base_name="desencriptado", ext=".txt"):
    i = 0
    while True:
        if i == 0:
            new_filename = f"{base_name}{ext}"
        else:
            new_filename = f"{base_name}{i}{ext}"
        if not os.path.exists(new_filename):
            return new_filename
        i += 1


while True:
    print("Bienvenido/a al script de generador de contraseñas de Tatiana. Elige una opción:")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")
    print()
    choice = input("Introduce tu opción: ")

    if choice == "1":
        print("- Encripción -")
        print()

        while True:
            rorm = input("Quieres usar una llave manual o aleatoria?? (a/m): ").lower()
            if rorm in ["a", "m"]:
                break
            print("Valor no válido, introduce 'a' o 'm'")


        if rorm == "a":
            keys = randint(1, 92)
            used_key = keys
            message_to_encrypt = input("Introduce el mensaje para encriptar: ")
            encrypted_message = ""
            for char in message_to_encrypt:
                if char in chars:
                    position = chars.index(char)
                    cipher_char = chars[(position + keys) % len(chars)]
                    encrypted_message += cipher_char
                else:
                    encrypted_message += char
            print()
            print(f"Tu mensaje encriptado es '{encrypted_message}'")
            print(f"Tu llave es '{used_key}'")
            print()
            save = input("¿Quieres guardar una copia del mensaje y la llave? (s/n): ").lower()

            if save == "s":
                filename = get_new_encrypted()
                with open(filename, "w") as f:
                    f.write(str(f"Mensaje encriptado: {encrypted_message}") + "\n")
                    f.write(str(f"Llave: {used_key}") + "\n")
                print(f"Guardado como {filename}")
            elif save == "n":
                continue

        elif rorm == "m":
            while True:
                manual_key = int(input("Introduce tu llave aquí: "))
                if manual_key == 93:
                    print("La llave no puede ser 93, sería el mismo mensaje, intentalo con otro número.")
                else:
                    break
            used_key = manual_key
            message_to_encrypt = input("Introduce el mensaje para encriptar: ")
            encrypted_message = ""
            for char in message_to_encrypt:
                if char in chars:
                    position = chars.index(char)
                    cipher_char = chars[(position + manual_key) % len(chars)]
                    encrypted_message += cipher_char
                else:
                    encrypted_message += char
            print()
            print(f"Tu mensaje encriptado es '{encrypted_message}'")
            print(f"Tu llave es '{used_key}'")
            print()
            save = input("¿Quieres guardar una copia del mensaje y la llave? (s/n): ").lower()

            if save == "s":
                filename = get_new_encrypted()
                with open(filename, "w") as f:
                    f.write(str(f"Mensaje encriptado: {encrypted_message}") + "\n")
                    f.write(str(f"Llave: {used_key}") + "\n")
                print(f"Guardado como {filename}")
            elif save == "n":
                continue

    elif choice == "2":
        print("- Desencripción -")
        print()
        key_insert = int(input("Inserta tu llave aquí: "))
        message_to_decrypt = input("Insert el mensaje para desencriptar: ")
        decrypted_message = ""
        for char in message_to_decrypt:
            if char in chars:
                cipher_char = chars.index(char)
                cipher_char = chars[(cipher_char - key_insert) % len(chars)]
                decrypted_message += cipher_char
            else:
                decrypted_message += char
        print()
        print(f"Tu mensaje desencriptado es: '{decrypted_message}'")
        print()
        save = input("¿Quieres guardar la llave, el mensaje encriptado y el desencriptado? (s/n): ").lower()

        if save == "s":
            filename = get_new_decrypted()
            with open(filename, "w") as f:
                f.write(str(f"Mensaje encriptado: {message_to_decrypt}") + "\n")
                f.write(str(f"Mensaje desencriptado: {decrypted_message}") + "\n")
                f.write(str(f"Llave: {key_insert}") + "\n")
            print(f"Guardado como {filename}")
        elif save == "n":
            continue


    elif choice == "3":
        print("Saliendo...")
        break


    else:
        print()
        print("Introduce una opción valida (1, 2 o 3): ")
        print()
        continue