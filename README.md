# Sistema POS para Raspberry Pi

## Descripción General
Este es un sistema de punto de venta (POS) desarrollado para Raspberry Pi, construido utilizando la biblioteca `tkinter` de Python. El sistema está diseñado para proporcionar una interfaz de usuario simple para gestionar productos, procesar pagos y generar recibos. El sistema incluye botones, etiquetas y marcos personalizados que admiten un flujo de pago sin problemas.

https://github.com/user-attachments/assets/d3df38ee-a41d-411c-9835-c0eeeca8f488

## Características
- **Selección de Categoría**: Utiliza botones de radio para seleccionar diferentes categorías de productos.
- **Lista de Productos**: Muestra los productos disponibles en la categoría seleccionada.
- **Gestión de Recibos**: Agrega productos al recibo, ajusta cantidades y calcula el total.
- **Calculadora**: Una calculadora simple que realiza operaciones aritméticas básicas, incluyendo agregar y reducir productos.
- **Sistema de Pago**: Procesa pagos y calcula el cambio.
- **Limpiar Recibo**: Opción para limpiar el recibo actual.
- **Salir**: Un botón simple de salida para cerrar la aplicación.

## Componentes
1. **Botones Personalizados**:
    - Varios botones para agregar, limpiar y remover productos.
    - Botones para controlar la salida del sistema y limpiar el recibo.
2. **Etiquetas Personalizadas**:
    - Etiquetas para mostrar cantidad, total, entrada de efectivo y cambio.
3. **Variables Personalizadas**:
    - Variables actualizadas dinámicamente para manejar cantidad, total y cambio.
4. **Vista de Árbol Personalizada**:
    - Muestra el recibo de manera estructurada, con columnas para número de producto, nombre, cantidad y subtotal.
5. **Calculadora**:
    - Una calculadora simple basada en cuadrícula para operaciones básicas de POS.
6. **Sistema de Caja**:
    - Maneja pagos y proporciona cálculos de cambio en tiempo real.
7. **Gestión de Productos**:
    - Organiza productos por categorías, permitiendo la selección de productos y opciones personalizadas.
8. **Gestión de Recibos**:
    - Muestra y gestiona recibos, incluyendo funciones para limpiar y remover productos.
