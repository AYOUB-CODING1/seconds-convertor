# Cayvora Cybersecurity Website

A modern, responsive dark-mode website for Cayvora, a Moroccan cybersecurity company specializing in services for startups and businesses.

## 🎨 Features

- **Dark Cyber-Aesthetic Design**: Deep gray/black background (#0d1117) with neon-green/aqua (#00ffcc) accents
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Smooth Animations**: Fade-in effects, hover animations, and smooth scrolling
- **Mobile Menu**: Hamburger menu for mobile navigation
- **Modern Typography**: Uses Poppins font from Google Fonts
- **No Framework Required**: Pure HTML, CSS, and JavaScript

## 📁 Project Structure

```
cayvora-website/
├── index.html          # Home page with hero, services preview, and payment methods
├── services.html       # Detailed services page with 6 service offerings
├── about.html          # About page with company info and values
├── contact.html        # Contact page with form and contact information
├── style.css           # Global styles with dark cyber theme
├── script.js           # Interactive features and animations
├── assets/             # Folder for images and icons (currently empty)
└── README.md           # This file
```

## 🚀 Getting Started

### Option 1: Open Directly in Browser

Simply open `index.html` in any modern web browser:

```bash
# Navigate to the project directory
cd cayvora-website

# Open in your default browser (macOS)
open index.html

# Open in your default browser (Linux)
xdg-open index.html

# Open in your default browser (Windows)
start index.html
```

### Option 2: Use a Local Server

For the best experience, use a local web server:

**Using Python 3:**
```bash
cd cayvora-website
python3 -m http.server 8000
# Visit http://localhost:8000
```

**Using Node.js (http-server):**
```bash
cd cayvora-website
npx http-server -p 8000
# Visit http://localhost:8000
```

**Using PHP:**
```bash
cd cayvora-website
php -S localhost:8000
# Visit http://localhost:8000
```

## 📄 Pages

### 1. Home (index.html)
- Hero section with company tagline
- Call-to-action buttons (WhatsApp & Email)
- Services preview (4 cards)
- Why Choose Us section
- Payment methods section
- Footer with contact links

### 2. Services (services.html)
- 6 detailed service cards:
  - Vulnerability Assessment
  - Penetration Testing
  - Security Consultation
  - Awareness & Training
  - Security Audits
  - Incident Response
- Process overview (4 steps)
- Call-to-action section

### 3. About (about.html)
- Company overview
- Mission statement
- Core values (4 cards)
- Why Choose Us (8 points)
- Approach and methodology
- Certifications & standards

### 4. Contact (contact.html)
- Contact information cards (WhatsApp & Email)
- Contact form with validation
- "What Happens Next" section
- FAQ section
- Morocco location highlight

## 🎨 Design System

### Colors
- **Background Primary**: `#0d1117`
- **Background Secondary**: `#161b22`
- **Card Background**: `#1c2128`
- **Accent Primary**: `#00ffcc` (Neon Green/Aqua)
- **Accent Secondary**: `#00d4aa`
- **Text Primary**: `#ffffff`
- **Text Secondary**: `#8b949e`
- **Border**: `#30363d`

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

### Spacing
- **Section Padding**: 80px vertical, 20px horizontal
- **Card Padding**: 2rem
- **Border Radius**: 8px (buttons), 12px (cards)

## ✨ Interactive Features

### JavaScript Functionality
- **Mobile Menu Toggle**: Hamburger menu for mobile devices
- **Active Navigation**: Highlights current page in navigation
- **Smooth Scrolling**: Smooth scroll to anchor links
- **Fade-in Animations**: Elements fade in when scrolling into view
- **Navbar Effects**: Shadow increases on scroll
- **Contact Form Handler**: Opens email client with form data
- **Parallax Effect**: Subtle parallax on hero section
- **Notification System**: Shows success messages

### CSS Animations
- **Fade In Up**: Hero content animation
- **Hover Effects**: Cards lift and glow on hover
- **Button Hover**: Buttons scale and glow
- **Border Animation**: Top border animates on card hover

## 📱 Responsive Breakpoints

- **Desktop**: > 768px (full layout)
- **Tablet**: 768px (adjusted grid)
- **Mobile**: < 768px (hamburger menu, stacked layout)
- **Small Mobile**: < 480px (further optimized)

## 🔧 Customization

### Update Contact Information

Replace placeholder contact details in all HTML files:

1. **WhatsApp Number**: Replace `2126XXXXXXXX` with actual number
2. **Email**: Update `cayvora.security@gmail.com` if needed

### Add Logo

Replace the emoji logo (🔒) with an actual logo:

1. Add logo image to `assets/` folder
2. Update logo in navigation:
```html
<a href="index.html" class="logo">
  <img src="assets/logo.png" alt="Cayvora" style="height: 40px;">
</a>
```

### Add Images

Add images to the `assets/` folder and reference them:

```html
<img src="assets/your-image.jpg" alt="Description">
```

### Modify Colors

Update CSS variables in `style.css`:

```css
:root {
  --bg-primary: #0d1117;
  --accent-primary: #00ffcc;
  /* ... other variables */
}
```

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 License

This project is created for Cayvora Security. All rights reserved.

## 🤝 Support

For questions or support, contact:
- **Email**: cayvora.security@gmail.com
- **WhatsApp**: +212 6XX XXX XXX

---

**Built with ❤️ for Moroccan Startups**
