# IPL Auction App

## Overview
This IPL Auction App is a web application developed using Flask, HTML, CSS, JavaScript, SQLite or PostgreSQL, and Flask-SocketIO. It facilitates real-time IPL auctions, allowing users to bid on players, manage player data, and interact seamlessly.

## Features
- **Real-time Bidding**: Users can participate in live auctions and place bids in real-time.
- **Player Management**: Admins can add, update, and remove player information.
- **User Authentication**: Secure user login and registration functionality.
- **Responsive Design**: User-friendly interface compatible with various devices.
- **Database Integration**: Supports SQLite or PostgreSQL for data storage.
![bid](https://github.com/Ayush1974/Innovate-Intern-Project/assets/101924850/80fc290d-3a3f-4f1c-85e2-a2c5d7874466)

## Technologies Used
- **Flask**: Micro web framework for Python used to develop the backend of the application.
- **HTML/CSS**: Used for structuring and styling the web pages.
- **JavaScript**: Adds interactivity and dynamic content to the web pages.
- **SQLite or PostgreSQL**: Database systems used for storing and managing application data.
- **Flask-SocketIO**: Enables real-time communication between the server and clients.
![home](https://github.com/Ayush1974/Innovate-Intern-Project/assets/101924850/40374e50-326e-4a0b-814e-6813407e4072)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ayush1974/ipl-auction-app.git
   cd ipl-auction-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - For SQLite (default):
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```
   - For PostgreSQL:
     Update the `SQLALCHEMY_DATABASE_URI` in `config.py` with your PostgreSQL database URI, then run:
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

5. **Run the application**:
   ```bash
   flask run
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
- **Admin Panel**: Access via `/admin` to manage players and oversee auctions. Use the following credentials to log in:
  - **Login ID**: admin@cricket.ipl
  - **Password**: admin123
- **User Registration/Login**: Register and log in to participate in auctions.
- **Auction Page**: Real-time bidding and auction updates.
![accepted_bid](https://github.com/Ayush1974/Innovate-Intern-Project/assets/101924850/028ce6c9-32be-45a6-893d-5b67e0cad32e)
![rejected_bid](https://github.com/Ayush1974/Innovate-Intern-Project/assets/101924850/0d4e3688-723c-4b92-945e-7c80f242c9f1)

## Contributing
1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a pull request**.

## License
This project is licensed under the MIT License.

## Contact
For any queries, please contact Ayush Mishra at ayushmgkp@gmail.com.

---

This README provides a comprehensive guide to understanding, installing, and contributing to the IPL Auction App. It highlights the key features and technologies used in the project.
