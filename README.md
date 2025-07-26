# FestiveVibe - Celebrating Telugu Festivals 🎉

A comprehensive, modern Streamlit web application showcasing the rich cultural heritage and festivals of Andhra Pradesh and Telangana. Built with love for Telugu culture and traditions.

## 🌟 Features

### Core Features
- **🏠 Homepage**: Welcoming interface with festival countdown and quick stats
- **🎊 Festival Explorer**: Browse 40+ Telugu festivals with detailed information
- **📝 Submit Traditions**: Share your local festival traditions and customs
- **🌐 Bilingual Support**: Full support for English and Telugu languages
- **📱 Responsive Design**: Mobile-friendly interface with modern UI

### New Advanced Features
- **📅 Festival Calendar**: Visual calendar view showing festivals by month and date
- **⏰ Festival Reminders**: Set personal reminders for upcoming festivals
- **📸 Photo Gallery**: Upload and share festival photos with community
- **🧠 Festival Quiz**: Interactive quiz to test your knowledge of Telugu festivals
- **🗺️ Map of Celebrations**: Visual representation of festival distribution across states
- **📖 Festival Stories**: Share personal experiences, poems, and articles about festivals
- **🖼️ Downloadable Posters**: Access festival posters and greeting cards
- **🌙 Dark/Light Mode**: Toggle between dark and light themes
- **⚙️ Admin Panel**: Manage submissions, gallery, and view analytics
- **🎯 Countdown Timer**: Real-time countdown to next major festival

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FestiveVibe
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28.0+
- Pandas 2.0.0+
- Pillow 10.0.0+
- Plotly 5.15.0+
- streamlit-option-menu 0.3.6+

## 🎯 Usage

### Navigation
The application features an intuitive sidebar navigation with the following sections:

1. **🏠 Home**: Welcome page with festival countdown and overview
2. **🎊 Festival Explorer**: Browse and search festivals by region
3. **📅 Calendar**: Monthly calendar view of festivals
4. **⏰ Reminders**: Set and manage festival reminders
5. **📸 Gallery**: Upload and view festival photos
6. **🧠 Quiz**: Test your festival knowledge
7. **🗺️ Map**: Visual festival distribution across states
8. **📖 Stories**: Share and read festival experiences
9. **🖼️ Posters**: Download festival posters and cards
10. **⚙️ Admin**: Manage content (password: admin123)
11. **📝 Submit Tradition**: Share your traditions

### Language Support
- Toggle between English and Telugu using the language buttons in the sidebar
- All content, including festival names, descriptions, and UI elements, are available in both languages

### Theme Options
- Switch between light and dark themes using the theme toggle in the sidebar
- Dark mode provides a comfortable viewing experience in low-light conditions

## 🎨 Festival Information

Each festival includes comprehensive details:
- **Name**: In both English and Telugu
- **Date**: When the festival is celebrated
- **Description**: Cultural significance and meaning
- **Rituals**: Traditional practices and ceremonies
- **Special Foods**: Traditional dishes prepared during the festival
- **Traditional Attire**: Clothing and accessories worn
- **Dances & Events**: Cultural performances and activities
- **Community Events**: Social gatherings and celebrations

## 📊 Admin Features

Access the admin panel with password `admin123` to:
- **Review Submissions**: Approve or reject user-submitted traditions
- **Manage Gallery**: Remove inappropriate photos
- **View Analytics**: Track user engagement and quiz performance
- **Content Moderation**: Ensure quality and appropriateness of content

## 🎮 Interactive Features

### Quiz System
- Multiple-choice questions about Telugu festivals
- Score tracking and performance analytics
- Bilingual question support
- Immediate feedback and results

### Reminder System
- Set personal reminders for upcoming festivals
- Add custom notes to reminders
- Manage and delete existing reminders
- Date-based notification system

### Gallery System
- Upload festival photos with titles and descriptions
- Search and filter photos
- Like and interact with community photos
- User attribution and timestamps

### Story Sharing
- Share personal festival experiences
- Submit poems and articles
- Filter stories by type and festival
- Community interaction with likes

## 🗺️ Festival Distribution

The application includes a comprehensive map showing:
- Festival popularity across Andhra Pradesh and Telangana
- Regional variations in celebrations
- Interactive state information
- Visual data representation using charts

## 📱 Mobile Responsiveness

The application is fully responsive and optimized for:
- Mobile phones and tablets
- Desktop computers
- Various screen sizes and orientations
- Touch-friendly interface elements

## 🔧 Customization

### Adding New Festivals
Festivals can be easily added by modifying the `get_festival_data()` function in `app.py`:

```python
"New Festival": {
    "telugu_name": "న్యూ ఫెస్టివల్",
    "date": "Month-Day",
    "description": "English description",
    "telugu_description": "తెలుగు వివరణ",
    "regions": ["AP", "Telangana"],
    "rituals": ["Ritual 1", "Ritual 2"],
    "foods": ["Food 1", "Food 2"],
    "attire": ["Attire 1", "Attire 2"],
    "dances": ["Dance 1", "Dance 2"],
    "events": ["Event 1", "Event 2"]
}
```

### Styling
Customize the appearance by modifying the CSS in the `load_css()` function:
- Color schemes
- Typography
- Layout spacing
- Component styling

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment
The application can be deployed on:
- **Streamlit Cloud**: Direct deployment from GitHub
- **Heroku**: Using the provided requirements.txt
- **AWS/GCP**: Container-based deployment
- **Vercel**: Static deployment with Streamlit

## 📈 Analytics

The admin panel provides insights into:
- Total user submissions
- Gallery photo uploads
- Story contributions
- Quiz participation rates
- Average quiz scores
- User engagement metrics

## 🔒 Security Features

- Admin authentication system
- Content moderation capabilities
- User input validation
- Secure file upload handling
- Session state management

## 🌟 Future Enhancements

Planned features for upcoming versions:
- User authentication and profiles
- Advanced search and filtering
- Festival event calendar integration
- Social media sharing
- Email notifications for reminders
- Advanced analytics dashboard
- Multi-language support expansion
- Festival video content
- Community forums
- Festival merchandise store

## 🤝 Contributing

We welcome contributions to enhance FestiveVibe:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Contribution Areas
- New festival additions
- UI/UX improvements
- Feature enhancements
- Bug fixes
- Documentation updates
- Translation improvements

## 📞 Contact & Support

- **Email**: contact@festivevibe.com
- **LinkedIn**: [Your Profile]
- **WhatsApp**: Available for support
- **Instagram**: Follow for updates

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Telugu community for cultural insights
- Contributors and beta testers
- Open source community for tools and libraries
- Cultural experts for festival information validation

---

**FestiveVibe** - Celebrating the rich cultural heritage of Andhra Pradesh and Telangana, one festival at a time! 🎉 