Este proyecto fue realizado como trabajo final del curso de Django, con el objetivo de integrar todos los conceptos vistos durante la cursada:

• Modelos y migraciones
• Formularios (Forms)
• Vistas basadas en funciones y clases (FBV / CBV)
• Templates y herencia
• Manejo de imágenes
• Sistema de autenticación de Django
• CRUD completo
• Navegación y diseño básico con HTML + CSS inline

La aplicación permite administrar una base de datos de notebooks y mostrar la información de manera organizada dentro de una interfaz simple y clara.

Funcionalidades principales
1. Crear nueva notebook

Formulario donde el usuario registrado puede cargar:
• Modelo
• Procesador
• Memoria RAM
• Imagen del equipo

Los datos se guardan en la base y luego pueden visualizarse desde el listado.

2. Listar notebooks

Página que muestra todas las notebooks registradas.
Incluye buscador por modelo y enlaces directos para:

• Ver
• Actualizar
• Eliminar

El formato se presenta dentro de un recuadro estilo tabla mejorada (simulación tipo Excel).

3. Ver detalle de cada notebook

Al seleccionar “Ver”, el usuario puede acceder a una ficha detallada que muestra:

• Modelo
• Procesador
• Memoria RAM
• Imagen del equipo en tamaño ampliado

Todo en un recuadro centrado y prolijo.

4. Actualizar notebook

Se utiliza una Vista Basada en Clase (UpdateView) que permite modificar cualquier campo del registro, incluida la imagen.

5. Eliminar notebook

Confirmación dentro de un recuadro estilizado, donde se solicita validar la eliminación antes de borrar definitivamente.

6. Sistema de usuarios

Incluye:

• Registro de usuarios
• Login
• Logout con mensaje estilizado
• Protección de rutas (solo usuarios logueados pueden crear o modificar notebooks)

7. Página “Acerca de mí”

