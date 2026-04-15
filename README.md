# 🐾 Sistema de Gestión - Hospital Veterinario

Este proyecto implementa un sistema orientado a objetos en Python que modela el funcionamiento básico de un hospital veterinario.

Permite gestionar:

* Clientes
* Mascotas
* Consultas
* Tratamientos
* Facturación
* Métodos de pago

---
## Conceptos de POO aplicados

| Concepto     | Implementación en el sistema                          |
| ------------ | ----------------------------------------------------- |
| Abstracción  | Clases `Persona` y `MetodoPago`                       |
| Herencia     | `Veterinario`, `Cliente`, `Recepcionista` ← `Persona` |
| Polimorfismo | Uso de `MetodoPago` en `Factura`                      |
| Asociación   | `Consulta` conecta `Mascota` y `Veterinario`          |
| Agregación   | `Cliente` contiene `Mascota`                          |
| Composición  | `Consulta` crea `Tratamiento`                         |

---
## Relación entre el UML y el código

###  Abstracción

En el UML se representan las clases abstractas `Persona` y `MetodoPago`.

En el código:

```python
class Persona(ABC):
    @abstractmethod
    def mostrar_rol(self):
        pass
```

---
### Herencia

En el UML se observa que varias clases heredan de una clase base.

En el código:

```python
class Veterinario(Persona):
```

También:

* Cliente → Persona
* Recepcionista → Persona
* PagoEfectivo → MetodoPago
* PagoTarjeta → MetodoPago
* PagoTransferencia → MetodoPago

---
### Agregación (Cliente ◇ Mascota)

En el UML se representa con un rombo blanco.

En el código:

```python
self.mascotas = []
```

Un cliente puede tener múltiples mascotas, pero estas existen independientemente del cliente.

---
### Asociación (Consulta ↔ Mascota / Veterinario)

En el UML se representa con líneas simples.

En el código:

```python
class Consulta:
    def __init__(self, mascota, veterinario, motivo):
```

La clase Consulta conecta al veterinario con la mascota.

---
### Composición (Consulta ◆ Tratamiento)

En el UML se representa con un rombo negro.

En el código:

```python
def crear_tratamiento(self, nombre, costo, duracion_dias):
    t = Tratamiento(nombre, costo, duracion_dias)
```

Los tratamientos se crean dentro de la consulta y dependen de ella.

---
### Polimorfismo (Métodos de pago)

En el UML se observa que Factura depende de MetodoPago.

En el código:

```python
def pagar(self, metodo_pago: MetodoPago):
```

Permite utilizar diferentes métodos de pago sin cambiar la lógica.

---
## Flujo del sistema

1. Se crea un cliente
2. Se registran una o más mascotas
3. Se crea un veterinario
4. Se genera una consulta
5. Se agregan tratamientos
6. Se calcula el costo total
7. Se genera una factura
8. Se paga con distintos métodos

---
## Ejecución del sistema

Para ejecutar el programa:

```bash
python main.py
```

El sistema incluye una simulación completa donde se prueba:

* Registro de cliente
* Registro de mascotas
* Atención por veterinario
* Creación de consulta
* Generación de tratamientos
* Pago con:

  * Efectivo
  * Tarjeta
  * Transferencia





