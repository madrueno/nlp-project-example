# Ejemplo Proyectos NLP

Este repositorio presenta un ejemplo educativo de buenas prácticas para la estructuración de experimentos en proyectos de procesamiento del lenguaje natural.

## Estructura del repositorio

```bash
.
├── data/           # datos organizados por etapas de transformacion
│   ├── raw/        # datos originales en crudo sin modificar
│   ├── interim/    # datos con transformaciones intermedias
│   └── processed/  # datos listos para experimentacion
├── models/         # modelos entrenados y artefactos
├── notebooks/      # notebooks de exploracion
├── reports/        # documentacion elaborada
├── runs/           # ejecuciones del proyecto
├── src/            # codigo principal del proyecto
│   ├── cli/        # comandos de consola para experimentacion
│   ├── config/     # configuracion general
│   ├── datasets/   # preparacion de datos
│   ├── evaluation/ # evaluacion de modelos
│   ├── modeling/   # definicion de modelos
│   └── pipelines/  # pipelines de experimentacion
├── .env.sample     # placeholder de variables de entorno
├── .gitignore      # archivos y carpetas sin trackear
├── README.md       # guia del repositorio
├── LICENSE         # licencia del repositorio
├── pyproject.toml  # dependencias y configuracion del proyecto
└── uv.lock         # fijado de versiones para reproducibilidad
```

