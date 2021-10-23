
# API-HealthTech

![image](https://img.shields.io/github/downloads/TcNobo/TcNo-Acc-Switcher/total?color=%23AEEA7A&label=Django&logo=Django&logoColor=%23AEEA7A&style=for-the-badge)
![image](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

## CONECTAR CON LA API

 **API horarioMedico**

 Metodo GET 🎈
 ```
 /api/horarioMedico/
 ```

 Metodo POST 📃

 ```
 /api/horarioMedico/
 ```
 Ejemplo de Request
 ```
 {
     "hora_inicio": "16:22:00",
     "hora_fin": "22:22:00"
 } 
 ```
 -----------------------------------------------------
 **API Medico**
 Metodo GET 🎈 --> Consultar
 ```
  /api/medico/
 ```
 Metodo POST 📃 --> Crear
 ```
 }
        "id_usuario": 10,
        "tipo_documento": "cc",
        "numero_documento": "10234757",
        "nombre_usuario": "Fabian Gonzales XD",
        "contrasena": "990518",
        "correo": "amata@gmail.com",
        "telefono": "20928937",
        "sexo": "M",
        "fecha_nacimiento": "2021-10-06",
        "grupo_sanguineo": "+O",
        "estrato": 3,
        "estado_civil": "soltero",
        "id_perfil": 3,
        "id_agenda": 5,
        "id_especialidad": 2
    }
  ```
Metodo  PUT    --> Actualizar
Metodo DELETE  --> Eliminar
 
 
 -----------------------------------------------------
**API Consultorios**
 Metodo GET 🎈 --> Consultar
 ```
  /api/medico/
 ```
 Metodo POST 📃 --> Crear
 ```
  {
        "codigo": "1155",
        "estado": "Activo",
        "id_consultorio": 99,
        "nombre": "eget",
        "piso": 50
},
  ```
 Metodo  PUT    --> Actualizar
 Metodo DELETE  --> Eliminar
 
 -----------------------------------------------------
**API especialidad**
 Metodo GET 🎈 --> Consultar
 ```
  /api/medico/
 ```
 Metodo POST 📃 --> Crear
 ```
{
        "descripcion": "Medicina Interna",
        "estado": "Activa",
        "id_especialidad": 8,
        "name": "Medicina Interna"
    }


  ```
Metodo  PUT    --> Actualizar
Metodo DELETE  --> Eliminar
```
/api/medico/id

Ejemplo:
http://localhost:8000/api/medico/10/
Status: 204
```
