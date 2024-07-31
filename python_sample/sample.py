def ingresar_evaluacion():
    while True:
        print('')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Ingrese un valor de 1 a 5')
            else:
                print('')
                comment = input()
                post = f': {point} : {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('La evaluación debe ser un número.')

def mostrar_resultados():
    print('')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main():
    while True:
        print('')
        print('1: Ingresar evaluación')
        print('2: Mostrar resultados hasta ahora')
        print('3: Terminar')
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                ingresar_evaluacion()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('')
                break
            else:
                print('Por favor ingrese 1 a 3')
        else:
            print('Por favor ingrese 1 a 3')

if __name__ == "__main__":
    main()
