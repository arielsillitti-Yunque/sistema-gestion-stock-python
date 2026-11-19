# Sistema de Gestión de Stock - Colo Records

Proyecto práctico desarrollado en Python durante la cursada de **Iniciación a la Programación (Talento Tech)**. Es una aplicación de consola pensada para administrar el inventario básico de un comercio.

## Funcionalidades
* **Añadir productos:** Carga de nuevos artículos validando que los campos no queden vacíos y que el precio sea numérico.
* **Visualizar inventario:** Listado completo de productos en stock con detalle de ID, nombre, categoría, descripción, cantidad y precio.
* **Búsqueda:** Filtro rápido por ID o nombre del producto.
* **Actualización:** Edición individual de cualquiera de los datos de un producto existente.
* **Eliminación:** Baja de artículos con confirmación previa.
* **Reporte de stock bajo:** Consulta de productos que se encuentran por debajo de un mínimo definido por el usuario.

## Requisitos y ejecución
El proyecto utiliza la librería `colorama` para mejorar la visualización en terminal.

1. Instalar la dependencia:
   `pip install colorama`
2. Ejecutar el programa:
   `python gestion_stock.py`
