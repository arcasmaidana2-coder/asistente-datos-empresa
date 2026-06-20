# Asistente de Datos Empresa

Este repositorio forma parte de mi portfolio junior orientado a empresas de datos, automatización, IA y backend Python.

## Objetivo del proyecto

Crear progresivamente un asistente de datos capaz de analizar información empresarial como stock, facturas, incidencias o documentación administrativa.

La idea es empezar con automatizaciones simples en Python y evolucionar el proyecto hacia herramientas más completas usando Pandas, SQL, FastAPI, Docker e integración con IA.

## Primer módulo: análisis de stock

El primer script del proyecto revisa una lista de productos y detecta cuáles están por debajo del stock mínimo.

Archivo principal:

```text
analisis_stock.py
```

## Caso de negocio

En una empresa, revisar stock manualmente puede provocar errores, pérdidas de tiempo o roturas de inventario.

Este script automatiza una primera revisión básica y muestra alertas claras cuando un producto necesita reposición.

## Qué hace el script

El programa:

1. Define una lista de productos.
2. Guarda para cada producto su stock actual y su stock mínimo.
3. Revisa cada producto uno por uno.
4. Detecta si el stock actual está por debajo del mínimo.
5. Muestra una alerta con las unidades que faltan.
6. Indica qué productos tienen stock suficiente.

## Ejemplo de salida

```text
REVISIÓN DE STOCK
-----------------
ALERTA: Café molido está bajo de stock. Faltan 6 unidades.
OK: Leche sin lactosa tiene stock suficiente.
ALERTA: Servilletas está bajo de stock. Faltan 3 unidades.
OK: Vasos takeaway tiene stock suficiente.
```

## Tecnologías usadas en esta fase

* Python
* VS Code

## Relación con mi experiencia previa

Este proyecto conecta con mi experiencia en administración, hostelería, gestión operativa, almacén, stock, facturas y documentación.

El objetivo es traducir esa experiencia práctica a soluciones técnicas simples, útiles y orientadas a negocio.

## Próximas mejoras

* Leer productos desde un archivo CSV.
* Analizar datos con Pandas.
* Guardar datos en una base SQL.
* Crear una API con FastAPI.
* Preparar el proyecto con Docker.
* Añadir un asistente de IA que resuma alertas y proponga acciones.


También genera un resumen final con el total de productos revisados, productos en alerta y unidades faltantes.