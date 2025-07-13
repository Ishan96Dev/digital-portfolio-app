# 🚀 Digital Portfolio App

A modern, interactive digital portfolio built with Streamlit featuring dual themes and AI/ML-inspired effects.

## ✨ Features

### 🎨 **Dual Theme System**
- **Professional Theme**: Clean, modern design with subtle AI/ML effects
- **Cyberpunk Theme**: Neon colors with sci-fi gaming aesthetics
- **Theme Switcher**: Easy toggle between themes via sidebar

### 🎯 **Interactive Sections**
- **Home**: Professional summary with animated stats
- **Skills**: Expandable skill descriptions with hover effects
- **Experience**: Detailed work history with enhanced cards
- **Education**: Academic background with modern styling
- **Certifications**: Professional certifications with view buttons
- **Activities**: Personal interests and achievements
- **Stats**: Professional and personal statistics

### 🎮 **Enhanced UI/UX**
- **Hover Animations**: Smooth transitions and scaling effects
- **AI/ML Effects**: Gradient overlays and particle animations
- **Responsive Design**: Works on desktop and mobile devices
- **Social Integration**: Direct links to professional networks
- **Resume Download**: One-click PDF download functionality

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Python**: Backend programming
- **CSS3**: Advanced styling and animations
- **PIL/Pillow**: Image processing
- **Base64**: Image encoding for web display

## 📁 Project Structure

```
digital-portfolio-app/
├── app.py                      # Main application file
├── requirements.txt             # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
└── src/
    ├── Images/                 # All image assets
    │   ├── Email-logo.png
    │   ├── linkedin-logo.png
    │   ├── GitHub-logo.png
    │   ├── YouTube-logo.png
    │   ├── Instagram-logo.png
    │   ├── Facbook-logo.png
    │   ├── Discord-logo.png
    │   ├── twitter-x-logo.png
    │   ├── IMG_20201227_0005 (1).jpg
    │   ├── Katonic-Mlops-certificate.png
    │   ├── Docker.png
    │   ├── Python.png
    │   ├── Google-ana.png
    │   └── Z-code.png
    └── Docs/                   # Document files
        └── Ishan_Chakraborty_Resume.pdf
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd digital-portfolio-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and go to `http://localhost:8501`
   - The app will automatically open in your default browser

## 🎨 Theme Features

### Professional Theme
- **Clean Design**: Minimalist layout with professional colors
- **AI/ML Effects**: Subtle gradient overlays and particle animations
- **Enhanced Cards**: Hover effects with scaling and shadow animations
- **Modern Typography**: Inter and Poppins fonts for readability

### Cyberpunk Theme
- **Neon Colors**: Bright cyan, magenta, and green accents
- **Glitch Effects**: Animated text with cyberpunk aesthetics
- **Glowing Elements**: Box shadows and text shadows for sci-fi look
- **Scan Lines**: Animated background effects

## 🔧 Customization

### Adding New Sections
1. Add section to the `sections` list in the sidebar
2. Create corresponding `elif` block in the main content area
3. Apply appropriate CSS classes for consistent styling

### Modifying Themes
1. Edit the `get_theme_css()` function in `app.py`
2. Add new CSS rules for custom elements
3. Test both themes for consistency

### Adding Images
1. Place images in `src/Images/` directory
2. Update file paths in `app.py`
3. Use base64 encoding for reliable display

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile devices
- Different screen resolutions

## 🎯 Key Features

### Interactive Elements
- **Theme Switcher**: Toggle between Professional and Cyberpunk themes
- **Social Links**: Direct access to professional networks
- **Resume Download**: One-click PDF download
- **Certificate Viewer**: View certification images
- **Hover Effects**: Enhanced user interaction

### Animation System
- **Smooth Transitions**: Cubic-bezier easing functions
- **Gradient Animations**: Moving color overlays
- **Particle Effects**: Floating background elements
- **Scale Animations**: Card lifting and scaling effects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ishan Chakraborty**
- QA Engineer & Data Scientist
- Automation Expert & Gaming Content Creator
- [LinkedIn](https://www.linkedin.com/in/ishan-chakraborty-0085571a1/)
- [GitHub](https://github.com/Ishan96Dev)
- [YouTube](https://youtube.com/@ishangaming96)

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Google Fonts for beautiful typography
- Open source community for inspiration

---

**Built with ❤️ using Streamlit & Python**
