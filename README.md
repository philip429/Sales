# Sales


# Sales CLI Tool 🚀
Command Line Repo

Una potente interfaz de línea de comandos (CLI) desarrollada en **Python** para la gestión integral de clientes. Este sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) de manera persistente sobre archivos planos.

## 🛠️ Tecnologías y Herramientas
* **Python 3.x**
* **Click**: Para la creación de la interfaz de comandos interactiva.
* **Setuptools**: Para la distribución e instalación del script como un comando del sistema.

## 📋 Requisitos Previos
Se recomienda el uso de un entorno virtual para mantener las dependencias aisladas:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## 🚀 Installation
To register the sales command in your system so it is available from any terminal:
1. Clone this repository.
2. Navigate to the project root (where the setup.py file is located).
3. Install in development mode

```bash
pip install -e .
```

## 💻 Usage Guide
The main command is `sales`. The command structure follows the pattern: `sales clients [COMMAND]`

### Available Commands:

|  Command  |  Description  |  Example
| ------------- |  :-------------:  |  ------------- |
|  `create`	  |  Creates a client (Name, Company, Email, Position)  |  `sales clients create`
|  `list`	    |  Displays a table with all registered clients  |  `sales clients list`
|  `update`	  |  Modifies client data using their UID	sales  |  `clients update [UID]`
|  `delete`	  |  Permanently removes a client using their UID  |  `sales clients delete [UID]`

## 📂 Project Structure

For the system to function correctly, the following file structure is expected:

* **sales.py**: Entry point that initializes the CLI context.
* **clients/**: Client module directory.
    * **commands.py**: Contains Click command logic.
    * **services.py**: (Required) Must contain the `ClientService` class for CSV persistence.
    * **models.py**: (Required) Must contain the `Client` class for data definition.
* **setup.py**: Package configuration for installation via `pip`.

❤️
