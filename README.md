# pySQLExport-gui

## Overview

**pySQLExport-gui** is a cross-platform graphical application designed to pull SQL data from MySQL and PostgreSQL databases and export it to various formats including CSV, JSON, HTML, XML, Excel, Parquet, HDF5, and more. Built using PyQt6, it provides an intuitive interface for managing database connections, running queries, and exporting data.

## Features

- **Cross-Platform:** Runs on Windows, macOS, and Linux.
- **Database Support:** Connects to both MySQL and PostgreSQL databases.
- **Data Export:** Export query results to multiple formats including CSV, JSON, HTML, XML, Parquet, HDF5, and Excel.
- **GUI:** Easy-to-use graphical user interface built with PyQt6.
- **Data Management:** Support for appending data to existing results or replacing them, with options to handle duplicates.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip package manager

### Installation Steps

```sh
pip install pySQLExport-gui
```

OR

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/pySQLExport-gui.git
    cd pySQLExport-gui
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Build the package:**

    ```sh
    python setup.py sdist bdist_wheel
    ```

4. **Install the package locally:**

    ```sh
    pip install .
    ```

## Usage

After installation, you can start the application by running:

    ```sh
    pySQLExport-gui
    ```

## Connecting to a Database

1. **Database Type:** Choose either MySQL or PostgreSQL from the dropdown menu.
2. **Server:** Enter the database server address (e.g., `localhost`).
3. **Username:** Enter the database username.
4. **Password:** Enter the database password.
5. **Database:** Enter the name of the database to connect to.
6. **Port:** The port will automatically update based on the database type selected but can be manually adjusted if needed.
7. **Establish Connection:** Click the `Establish Connection` button to connect to the database.

   
![pySQLExport Connection Screen](images/pySQLExport_connection_screen.png)
### Running Queries

1. **SQL Query:** Enter your SQL query in the provided text area.
2. **Execute Query:** Click the `Execute Query` button to run the query. Results will be displayed in the table view.


![pySQLExport Query Window](images/pySQLExport_Query_window.png)

### Exporting Data

1. **Export Selection:** Select the rows you wish to export, or choose to export all rows.
2. **Export Format:** Choose the desired export format from the options available (CSV, JSON, HTML, XML, Excel, Parquet, HDF5).
3. **Save File:** A file dialog will prompt you to choose the save location.

![pySQLExport Export Menu](images/pySQLExport_Export_Menu.png)

### Handling Duplicates

- **Allow Duplicates:** Use the checkbox to allow or disallow duplicate rows in your results.
- **Open in New Tab:** Use the checkbox to open query results in a new tab.


### Dependencies

- `PyQt6`: For the graphical user interface.
- `mysql-connector-python`: To connect to MySQL databases.
- `psycopg2-binary`: To connect to PostgreSQL databases.
- `pandas`: To convert SQL to various data formats
- `fastparquet`: To convert SQL to Parquet
- `numpy`: To assist in conversion to HDF5
- `tables`: To assist in export to HDF5

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features, bug fixes, or enhancements.

## License

This project is licensed under the GNU General Public License v3 (GPLv3). See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Special thanks to the open-source community for the tools and libraries that make this project possible.
