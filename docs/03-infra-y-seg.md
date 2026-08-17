# 03. Infraestructura, Seguridad y Requisitos No Funcionales

## Requisitos No Funcionales (RNFs)

* **RNF-01 — Self-hosted:** El sistema debe poder ejecutarse íntegramente dentro de la infraestructura del usuario sin dependencias de servidores de terceros.
* **RNF-02 — Privacidad:** Los datos y el código fuente extraídos del repositorio no deben enviarse a servicios externos; todo el análisis se procesa de forma local.
* **RNF-03 — Reproducibilidad:** La infraestructura se gestiona mediante **Terraform**, permitiendo desplegar o recrear el entorno en minutos.
* **RNF-04 — Persistencia:** El sistema conserva el historial de métricas calculadas mediante una base de datos **PostgreSQL** con volúmenes persistentes.
* **RNF-05 — Seguridad:** Manejo de secretos estricto mediante variables de entorno; queda prohibido incluir tokens, passwords o llaves en el control de versiones.
* **RNF-06 — Usabilidad:** Interfaz minimalista de un solo paso donde el usuario solo provee la URL del repositorio y el Access Token (si el repositorio es privado).
* **RNF-07 — Código Abierto (Open Source):** El proyecto se distribuye bajo una licencia libre para permitir su auditoría, uso personal y contribuciones de la comunidad.

## Estrategia de Seguridad

### 1. Manejo de Secretos y Credenciales
* **Variables de Entorno (`.env`):** Las credenciales nunca se suben al control de versiones. Se incluye `.env` en `.gitignore`.
* **Despliegues Cloud:** Uso de **AWS Secrets Manager** o **GitHub Secrets** para inyección dinámica de variables en tiempo de ejecución.

### 2. Permisos y Autenticación de Git
* **Mínimo Privilegio:** Uso exclusivo de Personal Access Tokens (PAT) con alcance reducido (`Contents: Read-only`).
* **Cero Almacenamiento:** Los tokens enviados por el usuario se procesan únicamente en memoria para clonar el repositorio y no se persisten.

### 3. Aislamiento de Puertos y Redes
* **Puertos Públicos:** Exposición única de los puertos de aplicación (`80` / `443` / `8000`).
* **Puertos Privados:** Los puertos de la base de datos PostgreSQL (`5432`) y de la caché Redis (`6379`) permanecen cerrados a internet.

### 4. Comunicación Inter-servicio
* **Docker Networks:** Uso de una red privada interna (`bridge`). Los servicios se comunican entre sí mediante sus nombres de contenedor (`http://db:5432`, `http://redis:6379`).

### 5. Permisos Cloud (AWS IAM)
* **IAM Roles:** El servidor/contenedor utiliza un rol de IAM asignado con acceso exclusivo a los recursos requeridos, eliminando el uso de llaves maestras (`AWS_ACCESS_KEY`).