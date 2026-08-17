# 01. Arquitectura y Decisiones Tecnológicas

## Modelo C4: Nivel 1 (Contexto)

```mermaid
flowchart TB
    admin["👤 Administrador<br/>[Person]<br/>Personal autorizado"]
    commitlens["CommitLens<br/>[Software System]<br/>Sistema analítico"]
    github["Github<br/>[External System]<br/>Fuente de información de commits"]

    admin -.->|Consulta métricas| commitlens
    commitlens -.->|Extrae datos| github
```

## Modelo C4: Nivel 2 (Contenedores)

```mermaid
flowchart TB
    admin["👤 Administrador<br/>[Person]<br/>Personal autorizado"]
    github["GitHub<br/>[External System]<br/>Contiene información sobre los commits"]

    subgraph commitlens["CommitLens [Container]"]
        webapp["Aplicación web<br/>[Container: React/js]<br/>Dashboard"]
        api["API Service<br/>[Container: Java/Python]"]
        db[("Database<br/>[Container: PostgreSQL]")]
    end

    admin -->|"Accede [HTTPS]"| webapp
    api -->|"Actualiza [Rest API]"| webapp
    api -->|"CRUD [SQL]"| db
    api -->|"Pull/Push [GIT]"| github
```

## Modelo C4: Nivel 3 (Componentes)

```mermaid
flowchart TB
    admin["👤 Administrador<br/>[Person]<br/>Personal autorizado"]
    github["GitHub<br/>[External System]<br/>Contiene información sobre los commits"]
    db[("Database<br/>[Container: MySQL]<br/>")]

    subgraph webapp["Web Application [Container]"]
        viz["Módulo de visualización<br/>[Component: HTML5/JS]"]
        apiclient["API Client<br/>[Component: JavaScript]"]
    end

    subgraph apiservice["API SERVICE [Container]"]
        apilayer["API Layer<br/>[Component: Python]"]
        orchestrator["Orchestrator<br/>[Component: Python]"]
        commit["Commit Module<br/>[Component: Python]"]
        analysis["Analysis Module<br/>[Component: Python]"]
        repo["Repository Module<br/>[Component: Python]"]
        user["User Module<br/>[Component: Python]"]
    end

    admin -->|"Accede [HTTPS]"| viz
    apiclient -->|" "| viz
    apiclient -->|" "| apilayer
    apilayer -->|" "| orchestrator
    orchestrator -->|" "| repo
    orchestrator -->|" "| commit
    orchestrator -->|" "| user
    orchestrator -->|" "| analysis
    commit -->|" "| github
    repo -->|"CRUD [SQL]"| db
```