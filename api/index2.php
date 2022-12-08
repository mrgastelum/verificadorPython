<?php
header("Content-Type:application/json");

if (!empty($_GET["codigo"])) {
   $codigo = $_GET["codigo"];
   $conn = new mysqli("127.0.0.1", "root", "", "excel");

   // Check connection
   if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
   }

   $query = "SELECT descripcion, precio, imagen FROM productos WHERE id=" . $codigo . ";";

   
   $result = $conn->query($query);



   if ($result->num_rows > 0) {
      while ($row = $result->fetch_assoc()) {
         //echo "id: " . $row["nombre_producto"]. " - Name: " . $row["precio_producto"]. " " . $row["imagen_producto"]. "<br>";
         peticion(200, $row["descripcion"], $row["precio"], $row["imagen"]);
      }
   } else {
      //echo "0 results";
      peticion(300, NULL, NULL, NULL);
   }
   $conn->close();
   // peticion(200,NULL,NULL,NULL);
} else {
   peticion(400, NULL, NULL, NULL);
}
function peticion($status, $descripcion, $precio, $imagen)
{
	
	
	
   header("HTTP/1.1" . $status);
   $respuesta["Status"] = $status;
   $respuesta["Nombre"] = $descripcion;
   $respuesta["Precio"] = $precio;
   $respuesta["Imagen"] = $imagen;

   $json_response = json_encode($respuesta);
   echo $json_response;
}
