# base-datos/

Schemas, migraciones, seeds y documentación de bases de datos.

## Qué guardar

| Tipo | Ejemplo |
|------|---------|
| Schema SQL | `schema/usuarios.sql` |
| Migraciones | `migrations/001_init.sql` |
| Seeds de prueba | `seeds/dev-data.sql` |
| Diagramas ER | Ver `../imagenes/diagramas/` |

## Qué NO subir a Git

- Archivos `.db`, `.sqlite` con datos reales
- Dumps con passwords o PII
- Credenciales en `.env`

Usa `.env.example` en el proyecto con variables sin valores secretos.
