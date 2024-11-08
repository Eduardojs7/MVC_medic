# Sanchez Salinas Eduardo Josue

# Estudio de Caso: Problemas en una Aplicación .NET 8 MVC para la Reserva de Citas en Línea

Este proyecto se centra en la creación de una aplicación MVC en .NET 8 para gestionar citas en línea en una clínica médica ficticia. El código existente presenta varios problemas de diseño y arquitectura, lo que resulta en un bajo rendimiento, altos costos de mantenimiento y escalabilidad limitada. La tarea consiste en identificar, analizar y proponer soluciones a estos problemas utilizando patrones de diseño GoF y técnicas de refactorización. A continuación, se presenta una lista de objetivos específicos que deben abordarse, acompañados de patrones o enfoques recomendados.

## Objetivos y Problemas Clave

| Objetivo                             | Problema                                                                                   | Patrón/Sugerencia de Refactorización                          |
|--------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **1. Mejorar la organización del código**  | Los controladores grandes contienen demasiada lógica, lo que los hace difíciles de probar y mantener. | **Facade**, **Command**, **Capa de servicio**                |
| **2. Separar la lógica de negocio**  | Las reglas de negocio están fuertemente acopladas con los componentes de la interfaz de usuario, lo que causa efectos en cascada durante las actualizaciones. | **Strategy**, **Repository**, **Adapter**                   |
| **3. Minimizar la duplicación de código** | Existen bloques de código duplicados en controladores y vistas, lo que complica las actualizaciones y aumenta el riesgo de errores. | **Template Method**, **Decorator**, **Extract Method**       |
| **4. Mejorar la capa de acceso a datos** | El acceso directo a la base de datos dentro de los controladores, con consultas SQL repetidas, afecta el rendimiento y la escalabilidad. | **Repository**, **Unit of Work**, **Data Mapper**           |
| **5. Mejorar la flexibilidad de los programadores** | La programación de citas es inflexible, requiriendo ajustes de lógica codificada para reglas de programación específicas de la empresa. | **Strategy**, **Factory Method**                            |
| **6. Reducir las dependencias**      | La inyección de dependencias está mal implementada, causando un acoplamiento fuerte y módulos difíciles de probar. | **Dependency Injection**, **Inversión de Control**, **Factory** |
| **7. Refactorizar métodos largos**   | Los controladores y servicios contienen métodos largos y complejos que son difíciles de entender y depurar. | **Extract Method**, **Replace Method with Method Object**    |
| **8. Manejar la autenticación de usuarios** | La autenticación se repite en varios controladores, con un manejo de seguridad inconsistente, reduciendo la mantenibilidad y seguridad del código. | **Facade**, **Singleton** para autenticación centralizada    |
| **9. Mejorar el manejo de errores**  | La falta de manejo de errores centralizado resulta en bloques try-catch dispersos en toda la aplicación, lo que dificulta la depuración. | **Chain of Responsibility**, **Decorator**, **Manejo de excepciones** |
| **10. Mejorar el tiempo de respuesta** | Los tiempos de respuesta son lentos debido a consultas ineficientes y una carga excesiva de datos. | **Lazy Loading**, **Caching**, **Optimización de consultas** |

## Pasos prácticos a seguir

### Identificar lógica repetida
- Busca bloques repetitivos en controladores, servicios y vistas.
- Considera centralizar la lógica en componentes reutilizables utilizando los patrones **Facade** o **Capa de servicio** para reducir redundancia.

### Desacoplar el acceso a datos
- Reemplaza el acceso directo a los datos en los controladores con los patrones **Repository** y **Unit of Work** para mejorar la separación de responsabilidades y la mantenibilidad.

### Refactorizar métodos largos
- Extrae la lógica compleja o anidada dentro de los métodos utilizando la técnica de refactorización **Extract Method**. El objetivo es tener métodos con un solo propósito para mejorar la legibilidad y la capacidad de prueba.

### Implementar programación flexible con el patrón Strategy
- Utiliza el patrón **Strategy** para implementar diversas estrategias de programación de citas que puedan adaptarse a nuevas reglas sin modificar la lógica central.

### Usar Inyección de Dependencias
- Implementa la inyección de dependencias en todos los servicios y controladores, reduciendo las dependencias codificadas. Considera el uso de un contenedor de **Inversión de Control** (IoC) para manejar las dependencias.

### Centralizar el manejo de errores
- Usa el patrón **Chain of Responsibility** para gestionar el manejo de errores de manera centralizada, permitiendo que tipos de errores específicos sean gestionados por el manejador adecuado.

### Optimizar el rendimiento con Lazy Loading y Caching
- Aplica **Lazy Loading** para retrasar la carga de datos hasta que realmente se necesiten y usa **caching** cuando sea apropiado para reducir las llamadas repetidas a la base de datos.
