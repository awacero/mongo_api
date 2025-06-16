# Mongo API Service

Servicio Flask para exponer datos desde MongoDB usando configuración externa y modular.

## Estructura

- `main.py`: Entrada principal
- `src/api_service.py`: Rutas Flask
- `src/db_connection.py`: Cliente MongoDB
- `src/config_loader.py`: Carga de configuración
- `config/config.yaml`: Configuración principal
- `config/mongo_config.json`: Credenciales de conexión

## Uso

```bash
pip install -r requirements.txt
python main.py
```

## UML Diagram

![Diagrama de despliegue](docs/mongo_api.png)