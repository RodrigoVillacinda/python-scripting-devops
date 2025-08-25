# Ejercicio 01 - Tarea 06

# 🧮 BMI Calculator (Python)

Este proyecto implementa una clase en **Python** para calcular el **Índice de Masa Corporal (BMI – Body Mass Index)** de una persona, utilizando su peso (en kilogramos) y altura (en metros).

El ejercicio está diseñado para practicar:

* **Clases y objetos en Python**
* Uso de **atributos internos** (convención con `_`)
* Definición de **propiedades** (`property`, `getter`, `setter`, `deleter`)
* Creación de un método para realizar un cálculo real (BMI)

---

## 📖 Fórmula del BMI

$$
BMI = \frac{Peso}{Altura^2}
$$

Donde:

* **Peso** → en kilogramos (kg)
* **Altura** → en metros (m)

Ejemplo:

* Peso = `75 kg`
* Altura = `2.0 m`

$$
BMI = 75 / (2.0^2) = 18.75
$$

---

## 🚀 Ejecución

```bash
python main.py
```

### ✅ Salida de ejemplo:

```
18.75
```

---

## 🔑 Aprendizajes principales

* Cómo usar `self` para acceder a los atributos del objeto.
* Diferencia entre **atributos públicos**, `_protegidos` y `__privados`.
* Uso de `property` para controlar acceso a atributos.
* Implementación de un método que devuelve un cálculo como **float**.

