# 🚀 Quick Start Guide

Get your Student Management System up and running in 5 minutes!

## 📋 Prerequisites

Before you begin, ensure you have:
- ✅ Python 3.7 or higher installed
- ✅ MySQL Server installed and running
- ✅ pip (Python package installer)

## 🔧 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
cd student-management-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install mysql-connector-python Pillow
```

### 3. Configure Database

**Option A: Use the setup script (Recommended)**

Run the SQL script to create database and table:
```bash
mysql -u root -p < database_setup.sql
```

**Option B: Manual setup**

1. Open MySQL:
   ```bash
   mysql -u root -p
   ```

2. Run the simple setup script:
   ```sql
   source simple_database_setup.sql
   ```

### 4. Configure Application

1. Copy the config template:
   ```bash
   copy config_template.py config.py
   ```
   (On Linux/Mac: `cp config_template.py config.py`)

2. Edit `config.py` and update your MySQL password:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'user': 'root',
       'password': 'YOUR_MYSQL_PASSWORD',  # Update this!
       'database': 'project_sql'
   }
   ```

### 5. Run the Application

```bash
python student_management_system.py
```

## 🎉 Success!

The application should now open with a professional interface. You can:
- ➕ Add new students
- ✏️ Edit existing records
- 🗑️ Delete students
- 🔍 Search and filter
- 📊 View analytics
- 💾 Backup/restore data
- 📁 Import/export CSV

## 🐛 Troubleshooting

### Database Connection Error
- Verify MySQL is running
- Check username and password in `config.py`
- Ensure database `project_sql` exists

### Module Not Found Error
```bash
pip install mysql-connector-python Pillow
```

### Permission Denied
- Run terminal/command prompt as administrator
- Check file permissions

### Port Already in Use
- Close other MySQL connections
- Restart MySQL service

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed features
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Explore the [database_setup.sql](database_setup.sql) for schema details

## 💡 Tips

1. **Sample Data**: The setup script includes sample student records
2. **Backup**: Use the built-in backup feature regularly
3. **Export**: Export data to CSV for Excel compatibility
4. **Search**: Use real-time search for quick access

## 🆘 Need Help?

- 📖 Check the [README.md](README.md)
- 🐛 Open an [Issue](https://github.com/YOUR_USERNAME/student-management-system/issues)
- 📧 Contact: [Your Email]

---

**Happy Managing! 🎓**
