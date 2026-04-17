"""
Sistema de Gestión - Hospital Veterinario
"""

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self): 
        pass

    def __str__(self):
        return f"{self.nombre} {self.documento})"

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"[Veterinario] {self.nombre} — Especialidad: {self.especialidad}"

    def atender_mascota(self, mascota):
        print(f" Dr/a. {self.nombre} está atendiendo a {mascota.nombre}")


class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"[Recepcionista] {self.nombre}"

    def registrar_cliente(self, cliente):
        print(f"\t {self.nombre} registró al cliente: {cliente.nombre}")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas: list = []

    def mostrar_rol(self):
        return f"[Cliente] {self.nombre} — Tel: {self.telefono}"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"\t Mascota '{mascota.nombre}' agregada al cliente {self.nombre}")

    def mostrar_mascotas(self):
        if not self.mascotas:
            print(" El cliente no tiene mascotas registradas.")
            return
        print(f"  Mascotas de {self.nombre}:")
        for m in self.mascotas:
            m.mostrar_info()

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print(f" - {self.nombre} | {self.especie} | {self.edad} años | {self.peso} kg")

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        print(f"  - {self.nombre} | ${self.costo:,.0f} | {self.duracion_dias} días")

class Consulta:
    def __init__(self, mascota: Mascota, veterinario: Veterinario, motivo: str):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = ""
        self.tratamientos: list[Tratamiento] = []

    def crear_tratamiento(self, nombre, costo, duracion_dias):
        t = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(t)
        print(f"\tTratamiento '{nombre}' añadido a la consulta.")
        return t

    def calcular_costo_consulta(self):
        total = sum(t.costo for t in self.tratamientos)
        return total

    def mostrar_resumen(self):
        print("  ─────────────────────────────")
        print(f"  CONSULTA")
        print(f"  Motivo    : {self.motivo}")
        print(f"  Diagnóstico: {self.diagnostico or 'pendiente'}")
        print(f"  Veterinario: {self.veterinario.nombre}")
        print(f"  Mascota   : {self.mascota.nombre} ({self.mascota.especie})")
        print("  Tratamientos:")
        for t in self.tratamientos:
            t.mostrar_tratamiento()
        print(f"  Total tratamientos: ${self.calcular_costo_consulta():,.0f}")
        print("  ─────────────────────────────")

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

    @abstractmethod
    def obtener_nombre(self):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"  Pago en EFECTIVO procesado: ${monto:,.0f}")
        print(f"  Por favor entregue el dinero en caja.")

    def obtener_nombre(self):
        return "Efectivo"

class PagoTarjeta(MetodoPago):
    def __init__(self, ultimos_digitos):
        self.ultimos_digitos = ultimos_digitos

    def procesar_pago(self, monto):
        print(f"  Pago con TARJETA procesado: ${monto:,.0f}")
        print(f"  Tarjeta terminada en: {self.ultimos_digitos}")
        print(f"  Transacción aprobada.")

    def obtener_nombre(self):
        return f"Tarjeta (*{self.ultimos_digitos})"


class PagoTransferencia(MetodoPago):
    def __init__(self, banco):
        self.banco = banco

    def procesar_pago(self, monto):
        print(f"  Pago por TRANSFERENCIA procesado: ${monto:,.0f}")
        print(f"  Banco: {self.banco}")
        print(f"  Se enviará comprobante por correo.")

    def obtener_nombre(self):
        return f"Transferencia ({self.banco})"

class Factura:
    IVA = 0.19  # 19%

    def __init__(self, consulta: Consulta):
        self.consulta = consulta
        self.subtotal = 0.0
        self.impuesto = 0.0
        self.total = 0.0
        self.pagada = False

    def calcular_total(self):
        self.subtotal = self.consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * self.IVA
        self.total = self.subtotal + self.impuesto
        return self.total

    def pagar(self, metodo_pago: MetodoPago):
        if self.pagada:
            print(" Esta factura ya fue pagada.")
            return
        
        self.calcular_total()
        print(f"\n  ═══════════════ FACTURA ═══════════════")
        print(f"  Paciente   : {self.consulta.mascota.nombre}")
        print(f"  Subtotal   : ${self.subtotal:,.0f}")
        print(f"  IVA (19%)  : ${self.impuesto:,.0f}")
        print(f"  TOTAL      : ${self.total:,.0f}")
        print(f"  Método     : {metodo_pago.obtener_nombre()}")
        print(f"  ────────────────────────────────────────")
      
        metodo_pago.procesar_pago(self.total)
        self.pagada = True
        print(f"  Pago completado exitosamente. ")
        print()

if __name__ == "__main__":

    print("   HOSPITAL VETERINARIO — PRUEBA DEL SISTEMA")

    # 1. Crear un cliente 
    print("\n[1] Creando cliente...")
    cliente = Cliente("María García", "CC-12345678", "310-555-0001")
    print(f"  {cliente.mostrar_rol()}")

    # 2. Registrar dos mascotas 
    print("\n[2] Registrando mascotas...")
    mascota1 = Mascota("Luna", "Perro", 3, 8.5)
    mascota2 = Mascota("Michi", "Gato", 5, 4.2)

    # AGREGACIÓN: el cliente agrega las mascotas a su lista
    cliente.agregar_mascota(mascota1)
    cliente.agregar_mascota(mascota2)
    cliente.mostrar_mascotas()

    # 3. Crear un veterinario 
    print("\n[3] Creando veterinario...")
    vet = Veterinario("Carlos Pérez", "CC-98765432", "Medicina Interna")
    print(f"  {vet.mostrar_rol()}")

    # POLIMORFISMO 
    recep = Recepcionista("Ana Torres", "CC-11223344")
    print(f"  {recep.mostrar_rol()}")

    # 4. Veterinario atiende una mascota 
    print("\n[4] Atendiendo mascota...")
    vet.atender_mascota(mascota1)

    # 5. Crear una consulta 
    print("\n[5] Creando consulta...")
    # ASOCIACIÓN: Consulta conecta a veterinario y mascota
    consulta = Consulta(mascota1, vet, "Vómitos y decaimiento general")
    consulta.diagnostico = "Gastroenteritis aguda"
    print(f"  Consulta creada para: {mascota1.nombre}")

    # 6. Crear dos tratamientos dentro de la consulta 
    print("\n[6] Añadiendo tratamientos (COMPOSICIÓN)...")
    # COMPOSICIÓN: los tratamientos nacen dentro de la consulta
    consulta.crear_tratamiento("Antibiótico oral 7 días", 85_000, 7)
    consulta.crear_tratamiento("Suero IV + hospitalización", 220_000, 2)

    # 7. Mostrar resumen y calcular costo total 
    print("\n[7] Resumen de la consulta:")
    consulta.mostrar_resumen()

    # 8. Pagar con efectivo 
    print("\n[8] Pagando con EFECTIVO (primer método)...")
    factura = Factura(consulta)
    pago_efectivo = PagoEfectivo()
    factura.pagar(pago_efectivo)

    # 9. Nueva consulta, cambiar método de pago 
    print("\n[9] Nueva consulta — pagando con TARJETA...")
    consulta2 = Consulta(mascota2, vet, "Control de peso y vacunas")
    consulta2.diagnostico = "Estado general bueno"
    consulta2.crear_tratamiento("Vacuna triple felina", 65_000, 0)
    consulta2.crear_tratamiento("Desparasitación interna", 35_000, 1)

    factura2 = Factura(consulta2)
    pago_tarjeta = PagoTarjeta("4321")
    factura2.pagar(pago_tarjeta)

    print("\n[10] Mismo sistema — pagando con TRANSFERENCIA...")
    consulta3 = Consulta(mascota1, vet, "Seguimiento post-tratamiento")
    consulta3.diagnostico = "Evolución favorable"
    consulta3.crear_tratamiento("Consulta de control", 50_000, 0)

    factura3 = Factura(consulta3)
    pago_transferencia = PagoTransferencia("Bancolombia")
    factura3.pagar(pago_transferencia)

print("_______________________________________________________________________")
print(" Elaborado por: JUAN SEBASTIAN RESTREPO DIAZ Y JONH ALEXANDER PRIETO LEIVA")
print()