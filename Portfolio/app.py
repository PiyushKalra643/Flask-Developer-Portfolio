from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Portfolio data extracted from your resume
portfolio_data = {
    "name": "Piyush Kalra",
    "tagline": "Enthusiastic Web Developer with a knack for crafting intuitive and efficient web solutions.",
    "email": "piyushkalra150@gmail.com",
    "linkedin": "https://linkedin.com/in/piyush-kalra-6618a5296",
    "phone": "+91 9643182250",
    "about": "As a passionate and detail-oriented web developer, I am always eager to learn and adapt to new technologies. I have strong organizational and time-management skills, and I thrive both independently and as a team member. My goal is to build user-friendly and efficient web applications that solve real-world problems.",
    "skills": ["C", "C++", "Java", "HTML5", "CSS3", "JavaScript", "React", "Python", "Flask", "MongoDB", "Git", "Figma"],
    "projects": [
        {
            "title": "Figma Travel App Design",
            "description": "Created wireframes, user personas, journey maps, and high-fidelity prototypes to visualize and iterate on user flows. Implemented responsive design elements for optimal performance across iOS and Android platforms.",
            "link": "#" # Placeholder link - replace with a link to your project
        },
        {
            "title": "Spotify Clone",
            "description": "Developed a full-stack web application replicating core Spotify features. Utilized programming languages like HTML, CSS, and JavaScript to build a scalable platform for music streaming.",
            "link": "#" # Placeholder link - replace with a link to your project
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Technology",
            "institution": "Manav Rachna University",
            "years": "2022-2026",
            "gpa": "5.86 CGPA"
        },
        {
            "degree": "Diploma",
            "institution": "Government Polytechnic Manesar",
            "years": "2020-2023",
            "gpa": "66%"
        }
    ],
    "internship": {
        "title": "Front-End Developer Intern",
        "company": "MotionCut",
        "date": "July - August, 2024",
        "description": "Designed and developed user-friendly webpages with a focus on cross-browser compatibility and responsive design."
    }
}

# The single-page portfolio route
@app.route('/')
def portfolio():
    # Renders the index.html template and passes all the data to it
    return render_template('index.html', data=portfolio_data)

# Run the app
if __name__ == '__main__':
    # debug=True allows for automatic reloading on code changes
    app.run(debug=True)


