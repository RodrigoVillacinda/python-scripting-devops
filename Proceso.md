# Plantilla DevOps - Flujo para nuevo ejercicio

Esta plantilla sirve como guia para crear, validar y documentar cada nuevo ejercicio del cursdo de scripting en Python aplicado a DevOps.

## Flujo paso a paso

### 1. Crear estructura del ejercicio

```bash
mkdir -p Tareas/tareaXX/ejercicioYY
cd Tareas/tareaXX/ejercicioYY
touch main.py test_main.py README.md notas.md

```

### 2. Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install flake8 pytest
```

### 3. Escribir y probar codigo

```bash
python main.py        
flake8 main.py        
pytest test_main.py   
```
### 4. Control de versiones

```bash
git checkout -b tareaXX-ejercicioYY
git add .
git commit -m "Agrega ejercicioYY de tareaXX con estructura base"
git push origin tareaXX-ejercicioYY
```
### 5. Crear Pull

### 6. Merge main

```bash
git checkout main
git pull origin main
```

