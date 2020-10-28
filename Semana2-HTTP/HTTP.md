
Peticiones HTTP

GET: El método GET  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.
HEAD: El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.
POST: El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.
PUT: El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.
DELETE: El método DELETE borra un recurso en específico.
CONNECT: El método CONNECT establece un túnel hacia el servidor identificado por el recurso.
OPTIONS: El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.
TRACE: El método TRACE  realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.
PATCH: El método PATCH  es utilizado para aplicar modificaciones parciales a un recurso.


Códigos de respuesta HTTP

Los códigos de estado de respuesta HTTP indican si se ha completado satisfactoriamente una solicitud HTTP específica. Las respuestas se agrupan en cinco clases:

- Respuestas informativas (100–199),
- Respuestas satisfactorias (200–299),
- Redirecciones (300–399),
- Errores de los clientes (400–499),
- y errores de los servidores (500–599).

Códigos de estado HTTP más importantes

- Código de estado 200 –OK: El código de respuesta 200 indica que la solicitud ha sido procesada correctamente. Todos los datos solicitados fueron recibidos por el servidor y se trasmitirán al cliente. Los usuarios de Internet no suelen encontrarse este código.

- Código de estado 301 –Moved Permanently: El código 301 significa que los datos solicitados por el cliente ya no se encuentran bajo la misma dirección de Internet, sino que han sido desplazados de manera permanente. Debido a que la ubicación actual del contenido solicitado está incluida en el informe de estado, el navegador web podrá redireccionar la petición a la nueva dirección. Así, el usuario es redireccionado y la antigua dirección pierde validez. Este código suele pasar desapercibido ante los ojos de los usuarios, el único cambio visible es la redirección de la URL en la barra de direcciones.

- Código de estado 302 – Moved Temporarily: A diferencia del 301, que hace referencia a una reubicación permanente, el código 302 informa que los datos solicitados están disponibles temporalmente en una dirección diferente. Aquí, la ubicación de la información es especificada, lo que genera una redirección automática. La antigua dirección sigue siendo válida.

- Código de estado 403 – Forbidden: El código de estado HTTP 403  indica al cliente que los datos solicitados están protegidos y, por ende, se le ha denegado el acceso debido a la falta de autorización del cliente. En estos casos, el usuario de Internet verá una página en formato HTML generada automáticamente que le informará sobre su falta de permisos para ejecutar la acción.

- Código de estado 404 – Not Found: Cuando el servidor envía el código 404 como respuesta significa que no fue posible encontrar los datos de la página web solicitada en el servidor. Esto sucede cuando la dirección ya no existe o los contenidos han sido trasladados sin especificar la nueva dirección. Cuando a un usuario le aparece el código de estado 404, deberá comprobar si ha introducido la URL de manera correcta en la barra de direcciones. Aquellos enlaces que dirigen a páginas inexistentes suelen conocerse como “enlaces muertos”.

- Código de estado 500 –Internal Server Error: Este tipo de respuesta actúa como un código de estado colectivo para un error inesperado en el servidor. Si el servidor falla y está interrumpiendo la recuperación de los datos solicitados, se emitirá automáticamente el código de estado 500. Además de la respuesta al cliente, el servidor web generará un tipo de registro de error interno en donde se expliquen más detalles sobre el error. Este último debe ser analizado por propietarios de páginas web que estén interesados en hacer las respectivas reparaciones en el software del servidor.

- Código de estado 503 –Service Unavailable: Este código de respuesta indica que el servidor web destinado a proporcionar la información está sobrecargado. Es común que esta respuesta del servidor incluya, además, información sobre cuándo se podrá procesar nuevamente la primera solicitud. Aquí, los usuarios de Internet pueden asumir que el administrador está trabajando en el problema y que, por lo tanto, el servidor estará disponible de nuevo. 


 
