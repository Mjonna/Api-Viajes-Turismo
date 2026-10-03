cat > README.md <<'EOF'
# API de Viajes y Turismo

API REST con Django REST Framework para gestionar destinos, guías, tours, clientes y reservas.

## Instalación
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Configuración
1. Copia `.env.example` como `.env` y completa los valores (SECRET_KEY y DB_PASSWORD).
2. Ejecuta `scripts_sql/crear_bd.sql` en MySQL/MariaDB para crear la base de datos, el usuario y sus permisos.
3. Aplica las migraciones y enciende el servidor:

        python manage.py migrate
        python manage.py runserver

## Endpoints (CRUD completo)
- /api/destinos/
- /api/guias/
- /api/tours/
- /api/clientes/
- /api/reservas/

Cada uno acepta GET (lista y detalle), POST, PUT, PATCH y DELETE.
EOF