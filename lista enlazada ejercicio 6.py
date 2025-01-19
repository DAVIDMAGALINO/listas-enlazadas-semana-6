class Estudiante:
    def __init__(self, cedula, nombre, apellido, correo, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nota = nota
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_estudiante(self, estudiante):
        if estudiante.nota >= 7:
            estudiante.siguiente = self.cabeza
            self.cabeza = estudiante
        else:
            if not self.cabeza:
                self.cabeza = estudiante
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = estudiante

    def buscar_estudiante(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_estudiante(self, cedula):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.cedula == cedula:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def contar_estudiantes(self):
        aprobados = 0
        reprobados = 0
        actual = self.cabeza
        while actual:
            if actual.nota >= 7:
                aprobados += 1
            else:
                reprobados += 1
            actual = actual.siguiente
        return aprobados, reprobados

# Ejemplo de uso del programa
lista = ListaEnlazada()

# Agregar estudiantes
lista.agregar_estudiante(Estudiante('001', 'Juan', 'Perez', 'juan@example.com', 8))
lista.agregar_estudiante(Estudiante('002', 'Ana', 'Garcia', 'ana@example.com', 5))
lista.agregar_estudiante(Estudiante('003', 'Luis', 'Lopez', 'luis@example.com', 9))

# Buscar estudiante por cédula
estudiante_buscado = lista.buscar_estudiante('002')
if estudiante_buscado:
    print(f'Encontrado: {estudiante_buscado.nombre} {estudiante_buscado.apellido}')
else:
    print('Estudiante no encontrado')

# Eliminar un estudiante
eliminado = lista.eliminar_estudiante('002')
if eliminado:
    print('Estudiante eliminado')
else:
    print('Estudiante no encontrado para eliminar')

# Contar estudiantes aprobados y reprobados
aprobados, reprobados = lista.contar_estudiantes()
print(f'Estudiantes aprobados: {aprobados}, Estudiantes reprobados: {reprobados}')
