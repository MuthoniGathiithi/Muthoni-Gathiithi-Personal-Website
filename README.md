# Joyce Muthoni Gathiithi - Personal Portfolio Website

A beautiful, modern personal portfolio website built with Django, showcasing my work as a Python/Django developer and cybersecurity enthusiast.

## 🌟 Features

- **Modern Design**: Dark theme with cyan/blue accents and sophisticated animations
- **Responsive Layout**: Optimized for all devices and screen sizes
- **Advanced Navigation**: Sophisticated dropdown menus with smooth transitions
- **Project Showcase**: Categorized portfolio with filtering capabilities
- **Security Focus**: Dedicated section for cybersecurity projects and achievements
- **Contact System**: Functional contact form with AJAX submission
- **Admin Panel**: Easy content management through Django admin
- **Performance Optimized**: Fast loading with optimized assets and animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuthoniGathiithi/personal-website.git
   cd personal-website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the website**
   Open your browser and go to `http://127.0.0.1:8000`

## 📁 Project Structure

```
personal-website/
├── portfolio/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                   # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   ├── forms.py           # Django forms
│   └── admin.py           # Admin configuration
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   └── main/              # App-specific templates
├── static/                 # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Images
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎨 Customization

### Adding Projects
1. Access the Django admin panel at `/admin/`
2. Login with your superuser credentials
3. Navigate to "Projects" and click "Add project"
4. Fill in the project details and save

### Adding Skills
1. In the admin panel, go to "Skills"
2. Add skills with categories and proficiency levels
3. Skills will automatically appear on the About page

### Updating Content
- Edit templates in the `templates/main/` directory
- Modify styles in `static/css/style.css`
- Update JavaScript functionality in `static/js/main.js`

## 🛡️ Security Features

- CSRF protection enabled
- Secure static file serving with WhiteNoise
- Input validation and sanitization
- SQL injection protection through Django ORM
- XSS protection with Django's template system

## 🚀 Deployment

### Render Deployment
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn portfolio.wsgi:application`
   - **Environment Variables**:
     - `PYTHON_VERSION`: `3.11.0`
     - `DATABASE_URL`: (if using external database)

### Environment Variables
Create a `.env` file for local development:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

## 🎯 Key Sections

### Home Page
- Hero section with typing animation
- Featured projects showcase
- Skills overview
- Call-to-action sections

### About Page
- Personal story and background
- Detailed skills with progress bars
- Professional information

### Projects Page
- Filterable project portfolio
- Detailed project cards
- Pagination support
- Category-based organization

### Security Focus
- Cybersecurity projects showcase
- Learning platform profiles (TryHackMe, HackerRank)
- Security skills and philosophy

### Contact Page
- Functional contact form
- Social media links
- FAQ section
- Professional contact information

## 🛠️ Technologies Used

- **Backend**: Django 4.2.7, Python
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5, Custom CSS with CSS Variables
- **Icons**: Font Awesome, Devicons
- **Fonts**: Inter, JetBrains Mono
- **Animations**: AOS (Animate On Scroll)
- **Database**: SQLite (development), PostgreSQL (production)

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## ⚡ Performance Features

- Optimized images and assets
- Lazy loading for images
- Minified CSS and JavaScript
- Efficient database queries
- Caching strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Joyce Muthoni Gathiithi**
- Email: gathiithijoyce74@gmail.com
- GitHub: [@MuthoniGathiithi](https://github.com/MuthoniGathiithi)
- LinkedIn: [muthoni-gathiithi](https://linkedin.com/in/muthoni-gathiithi)
- TryHackMe: [MuthoniGathiithi](https://tryhackme.com/p/MuthoniGathiithi)
- HackerRank: [gathiithijoyce74](https://www.hackerrank.com/profile/gathiithijoyce74)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive framework
- Font Awesome for the beautiful icons
- All the open-source contributors who made this possible

---

⭐ **Star this repository if you found it helpful!**
