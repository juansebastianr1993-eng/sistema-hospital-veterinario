## 🐾 Sistema de Gestión Veterinaria

Este proyecto modela un flujo completo dentro de una clínica veterinaria, desde el registro de clientes y mascotas hasta la generación de consultas médicas, tratamientos y facturación con múltiples métodos de pago utilizando POO en python. 

Se aplican conceptos clave como:

--- 
| Concepto        | Uso en el sistema                                    |
| --------------- | ---------------------------------------------------- |
| Herencia        | Reutilización de atributos en `Persona`              |
| Abstracción     | Clases abstractas como `Persona` y `MetodoPago`      |
| Encapsulamiento | Organización interna de la lógica                    |
| Polimorfismo    | Diferentes métodos de pago                           |
| Composición     | `Consulta` contiene `Tratamientos`                   |
| Agregación      | `Cliente` tiene múltiples `Mascotas`                 |
| Asociación      | Relación entre `Consulta`, `Mascota` y `Veterinario` |

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

## Autores: 

Proyecto elaborado por:

- Juan Sebastián Restrepo Díaz
- John Alexander Prieto Leiva



