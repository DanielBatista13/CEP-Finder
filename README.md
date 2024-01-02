
# CEP Finder

CEP Finder is a simple Python program that allows users to find address details based on a Brazilian ZIP code (CEP). The program utilizes the tkinter library for the graphical user interface and makes use of the ViaCEP API for retrieving address information.

## Features

- **User-Friendly Interface:** The program provides a straightforward interface for users to input a CEP and view corresponding address details.

- **CEP Lookup:** Users can enter a CEP in the entry field and click the "Listar" button to retrieve address information.

- **Copy to Clipboard:** The program allows users to copy address components such as logradouro, bairro, cidade, UF, and DDD to the clipboard for easy sharing.

## How to Use

1. **Enter CEP:** Input the Brazilian CEP (ZIP code) in the entry field.

2. **Listar (List):** Click the "Listar" button to fetch address details from the ViaCEP API.

3. **Copy to Clipboard:** After retrieving address details, use the "Copiar" buttons to copy specific components to the clipboard.

## Requirements

- Python 3.x
- tkinter module
- requests module

## Installation

1. Clone or download the repository to your local machine.

2. Run the following command to install the required modules:
    ```
    pip install -r requirements.txt
    ```

3. Run the program:
    ```
    python main.py
    ```

## Note

- The program uses the ViaCEP API to fetch address details based on the provided CEP. Ensure that your machine has an active internet connection for proper functionality.

## Screenshots

![J5Y5zTG.md.png](https://iili.io/J5Y5zTG.md.png)
![J5YeAOb.md.png](https://iili.io/J5YeAOb.md.png)
![J5Yk9hx.md.png](https://iili.io/J5Yk9hx.md.png)

## License

This project is licensed under the [MIT License](LICENSE).
