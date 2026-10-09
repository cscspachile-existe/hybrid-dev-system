-- Esquema mínimo para generar cotizaciones desde BD
-- (misma estructura conceptual que el Excel maestro).

CREATE TABLE IF NOT EXISTS emisor (
  id              INTEGER PRIMARY KEY,
  razon_social    TEXT NOT NULL,
  nombre_fantasia TEXT,
  rut             TEXT NOT NULL,
  domicilio_legal TEXT,
  condicion_proveedor TEXT,
  contacto_comercial  TEXT
);

CREATE TABLE IF NOT EXISTS cotizacion (
  id                   INTEGER PRIMARY KEY,
  id_proceso           TEXT NOT NULL UNIQUE,  -- ej. 5178-4975-COT26
  titulo_oferta        TEXT,
  cliente              TEXT NOT NULL,
  unidad_solicitante   TEXT,
  responsable_proceso  TEXT,
  referencia_proceso   TEXT,
  justificacion_tecnica TEXT,
  fecha_emision        DATE,
  emisor_id            INTEGER REFERENCES emisor(id),
  plazo_entrega        TEXT,
  garantia_tecnica     TEXT,
  validez_oferta       TEXT,
  forma_pago           TEXT,
  iva_pct              REAL NOT NULL DEFAULT 19,
  creado_en            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cotizacion_item (
  id                   INTEGER PRIMARY KEY,
  cotizacion_id        INTEGER NOT NULL REFERENCES cotizacion(id) ON DELETE CASCADE,
  item                 INTEGER NOT NULL,
  descripcion          TEXT NOT NULL,
  cantidad             REAL NOT NULL DEFAULT 1,
  precio_unitario_neto REAL NOT NULL,
  UNIQUE (cotizacion_id, item)
);

-- Vista con totales calculados
CREATE VIEW IF NOT EXISTS v_cotizacion_resumen AS
SELECT
  c.id,
  c.id_proceso,
  c.cliente,
  SUM(i.cantidad * i.precio_unitario_neto) AS subtotal_neto,
  ROUND(SUM(i.cantidad * i.precio_unitario_neto) * (c.iva_pct / 100.0)) AS iva,
  ROUND(SUM(i.cantidad * i.precio_unitario_neto) * (1 + c.iva_pct / 100.0)) AS total_bruto
FROM cotizacion c
JOIN cotizacion_item i ON i.cotizacion_id = c.id
GROUP BY c.id;
