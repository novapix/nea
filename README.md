# NEA Billing Management System

A comprehensive Django-based billing management system designed for Nepal Electricity Authority (NEA). This system provides role-based access control for managing customers, employees, branches, and billing operations.

## ⚡ Features

- **Role-Based Authentication**: Support for multiple user types (Super Admin, Branch Admin, Employee, Meter Reader, Customer)
- **Customer Management**: Complete customer registration and profile management
- **Branch Operations**: Multi-branch support with dedicated dashboards
- **Employee Management**: Track employees across different branches and roles
- **Billing System**: Comprehensive billing with demand types and payment tracking
- **Modern UI**: Clean, responsive interface built with Tailwind CSS
- **Secure Login**: Professional authentication system with role-based redirects

## 🚀 User Roles

- **Super Admin**: Full system access and management
- **Branch Admin**: Branch-specific management and oversight
- **Employee**: General employee operations and customer service
- **Meter Reader**: Meter reading and data collection
- **Customer**: Self-service portal for billing information

## 🛠 Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, Tailwind CSS, DaisyUI
- **Database**: SQLite (development), MySQL (production ready)
- **Authentication**: Django's built-in auth system with custom user profiles
- **Environment**: Python 3.11+

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- Node.js (for Tailwind CSS)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd nea
   ```

2. **Install dependencies using uv (recommended)**
   ```bash
   pip install uv
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration. See [Database Configuration](#-database-configuration) for details.

4. **Generate Secret Key**
   ```bash
   python manage.py generate_secret_key
   ```
   Copy the generated key to your `.env` file.

5. **Install Tailwind CSS**
   ```bash
   python manage.py tailwind install
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   python manage.py seed_nepali_months
   ```

7. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   # Terminal 1: Django server
   python manage.py runserver
   
   # Terminal 2: Tailwind CSS (in another terminal)
   python manage.py tailwind start
   ```

9. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Login with your superuser credentials

## 🗄 Database Configuration

The system supports both SQLite (for development) and MySQL (for production). Configuration is managed through environment variables in the `.env` file.

### SQLite (Default - Development)

No additional configuration required. SQLite is used by default and the database file (`db.sqlite3`) will be created automatically.

```env
SECRET_KEY=your-generated-secret-key
DEBUG=True
```

### MySQL (Production)

For production deployment with MySQL, add the following to your `.env` file:

```env
SECRET_KEY=your-generated-secret-key
DEBUG=False

# MySQL Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=nea_billing
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

# Production Settings
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

[//]: # ()
[//]: # (### Prerequisites for MySQL)

[//]: # ()
[//]: # (1. Install MySQL server)

[//]: # (2. Create a database:)

[//]: # (   ```sql)

[//]: # (   CREATE DATABASE nea_billing CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;)

[//]: # (   ```)

[//]: # (3. Create a MySQL user with appropriate permissions:)

[//]: # (   ```sql)

[//]: # (   CREATE USER 'nea_user'@'localhost' IDENTIFIED BY 'your_password';)

[//]: # (   GRANT ALL PRIVILEGES ON nea_billing.* TO 'nea_user'@'localhost';)

[//]: # (   FLUSH PRIVILEGES;)

[//]: # (   ```)

[//]: # ()
[//]: # (### Environment Variables Reference)

[//]: # ()
[//]: # (<table>)

[//]: # (<thead>)

[//]: # (<tr>)

[//]: # (<th>Variable</th>)

[//]: # (<th>Description</th>)

[//]: # (<th>Required</th>)

[//]: # (<th>Default</th>)

[//]: # (</tr>)

[//]: # (</thead>)

[//]: # (<tbody>)

[//]: # (<tr>)

[//]: # (<td><code>SECRET_KEY</code></td>)

[//]: # (<td>Django secret key for security</td>)

[//]: # (<td>Yes</td>)

[//]: # (<td>-</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DEBUG</code></td>)

[//]: # (<td>Enable/disable debug mode</td>)

[//]: # (<td>No</td>)

[//]: # (<td>False</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_ENGINE</code></td>)

[//]: # (<td>Database backend</td>)

[//]: # (<td>No</td>)

[//]: # (<td>django.db.backends.sqlite3</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_NAME</code></td>)

[//]: # (<td>Database name</td>)

[//]: # (<td>No</td>)

[//]: # (<td>db.sqlite3</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_USER</code></td>)

[//]: # (<td>Database username</td>)

[//]: # (<td>No</td>)

[//]: # (<td>-</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_PASSWORD</code></td>)

[//]: # (<td>Database password</td>)

[//]: # (<td>No</td>)

[//]: # (<td>-</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_HOST</code></td>)

[//]: # (<td>Database host</td>)

[//]: # (<td>No</td>)

[//]: # (<td>localhost</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>DB_PORT</code></td>)

[//]: # (<td>Database port</td>)

[//]: # (<td>No</td>)

[//]: # (<td>3306</td>)

[//]: # (</tr>)

[//]: # (<tr>)

[//]: # (<td><code>ALLOWED_HOSTS</code></td>)

[//]: # (<td>Allowed hosts &#40;production&#41;</td>)

[//]: # (<td>No</td>)

[//]: # (<td>[]</td>)

[//]: # (</tr>)

[//]: # (</tbody>)

[//]: # (</table>)

[//]: # ()
[//]: # (## 📁 Project Structure)

[//]: # ()
[//]: # (```)

[//]: # (nea/)

[//]: # (├── billing/                 # Main application)

[//]: # (│   ├── models.py           # Database models)

[//]: # (│   ├── views.py            # View logic)

[//]: # (│   ├── admin.py            # Django admin configuration)

[//]: # (│   ├── utils.py            # Helper functions)

[//]: # (│   └── management/         # Custom management commands)

[//]: # (├── nea/                    # Django project settings)

[//]: # (├── templates/              # HTML templates)

[//]: # (│   ├── auth/              # Authentication templates)

[//]: # (│   └── dashboard/         # Dashboard templates)

[//]: # (├── theme/                 # Tailwind CSS theme)

[//]: # (├── static/                # Static files)

[//]: # (├── .env.example           # Environment configuration template)

[//]: # (└── manage.py              # Django management script)

[//]: # (```)

[//]: # ()
[//]: # (## 🗃 Database Models)

[//]: # ()
[//]: # (### Core Models)

[//]: # (- **User**: Django's built-in user model)

[//]: # (- **UserProfile**: Extended user information with role assignment)

[//]: # (- **Role**: System roles &#40;Super Admin, Branch Admin, etc.&#41;)

[//]: # (- **Branch**: Organization branches)

[//]: # (- **Employee**: Employee information and branch assignment)

[//]: # (- **Customer**: Customer details and billing information)

[//]: # (- **DemandType**: Electricity demand categories and rates)

[//]: # ()
[//]: # (## 🎨 UI Components)

[//]: # ()
[//]: # (The system features a modern, responsive design with:)

[//]: # (- Clean login interface with split-screen layout)

[//]: # (- Role-specific dashboards with relevant information)

[//]: # (- Professional color scheme using slate and emerald colors)

[//]: # (- Mobile-responsive design that works across all devices)

[//]: # ()
[//]: # (## 🔐 Authentication Flow)

[//]: # ()
[//]: # (1. Users login through the main authentication page)

[//]: # (2. System validates credentials and determines user role)

[//]: # (3. Users are redirected to their appropriate dashboard:)

[//]: # (   - Super Admin → Comprehensive system overview)

[//]: # (   - Branch Admin → Branch-specific management)

[//]: # (   - Employee → Employee operations dashboard)

[//]: # (   - Meter Reader → Customer meter reading interface)

[//]: # (   - Customer → Personal billing information)

[//]: # ()
[//]: # (## 🚦 Development Commands)

[//]: # ()
[//]: # (```bash)

[//]: # (# Generate new secret key)

[//]: # (python manage.py generate_secret_key)

[//]: # ()
[//]: # (# Seed initial data)

[//]: # (python manage.py seed_nepali_months)

[//]: # ()
[//]: # (# Collect static files &#40;production&#41;)

[//]: # (python manage.py collectstatic)

[//]: # ()
[//]: # (# Run tests)

[//]: # (python manage.py test)

[//]: # ()
[//]: # (# Create new migrations)

[//]: # (python manage.py makemigrations)

[//]: # ()
[//]: # (# Apply migrations)

[//]: # (python manage.py migrate)

[//]: # (```)

[//]: # ()
[//]: # (## 🌐 Environment Configuration)

[//]: # ()
[//]: # (### Development)

[//]: # (- Set `DEBUG=True` in `.env`)

[//]: # (- Uses SQLite database)

[//]: # (- Hot reloading enabled for Tailwind CSS)

[//]: # ()
[//]: # (### Production)

[//]: # (- Set `DEBUG=False`)

[//]: # (- Configure MySQL database)

[//]: # (- Set appropriate `ALLOWED_HOSTS`)

[//]: # (- Use environment variables for sensitive settings)

[//]: # ()
[//]: # (## 📝 Contributing)

[//]: # ()
[//]: # (1. Fork the repository)

[//]: # (2. Create a feature branch &#40;`git checkout -b feature/new-feature`&#41;)

[//]: # (3. Commit your changes &#40;`git commit -am 'Add new feature'`&#41;)

[//]: # (4. Push to the branch &#40;`git push origin feature/new-feature`&#41;)

[//]: # (5. Create a Pull Request)

[//]: # ()
[//]: # (## 📄 License)

[//]: # ()
[//]: # (This project is developed for Nepal Electricity Authority. All rights reserved.)

[//]: # ()
[//]: # (## 🔧 Troubleshooting)

[//]: # ()
[//]: # (### Common Issues)

[//]: # ()
[//]: # (**Tailwind CSS not loading:**)

[//]: # (```bash)

[//]: # (python manage.py tailwind install)

[//]: # (python manage.py tailwind start)

[//]: # (```)

[//]: # ()
[//]: # (**Database migration errors:**)

[//]: # (```bash)

[//]: # (python manage.py migrate --run-syncdb)

[//]: # (```)

[//]: # ()
[//]: # (**Secret key missing:**)

[//]: # (```bash)

[//]: # (python manage.py generate_secret_key)

[//]: # (```)

[//]: # ()
[//]: # (**MySQL connection issues:**)

[//]: # (- Verify MySQL server is running)

[//]: # (- Check database credentials in `.env` file)

[//]: # (- Ensure database exists and user has proper permissions)

[//]: # ()
[//]: # (## 📞 Support)

[//]: # ()
[//]: # (For technical support or questions about the system, please contact the system administrator.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (Built with ❤️ for Nepal Electricity Authority)
