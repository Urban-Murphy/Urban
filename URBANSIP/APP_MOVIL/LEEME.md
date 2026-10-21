# App móvil UrbanSIP (información comercial)

Qué es: una página web instalable en el celular (funciona sin señal una vez abierta). Muestra los 6 modelos con m², dormitorios, baños, precios, forma de pago, terminaciones e información general.

## Carpetas
- `index.html`, `sw.js`, `manifest.webmanifest`, `icono.svg`: la app. No se tocan.
- `datos/datos.js`: **toda la información** (precios, m², pagos, terminaciones). Se actualiza solo este archivo.
- `imagenes/<modelo>/`: fotos. Por modelo: `portada.jpg`, `foto1.jpg` … `foto8.jpg`, `planta.jpg`.
  Modelos: `aura`, `origen`, `trama35`, `umbral64`, `umbral80`, `refugio`.

## Actualizar
1. Cambiar el dato en `datos/datos.js`.
2. Subir el número de `version` y la fecha `preciosAl`.

## Pendiente
- Fotos: copiar desde el Drive (carpeta Catálogo) a `imagenes/`.
- Precios a confirmar: Trama 35 y Origen 63 (la planilla no coincide con m² × 1.200 / 1.500).
- Fichas de terminaciones de Origen, Trama, Umbral y Refugio (hoy se muestra la de Aura como referencia).
- Garantías: no incluidas hasta validación legal.
- Publicar en un link para que el equipo la abra desde el celular.
