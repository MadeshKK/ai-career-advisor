course_map = {
    # 🛠️ Engineering
    'dealing with computers': [
        {"name": "B.Tech in Computer Science", "description": "Learn programming, software development, and system design."},
        {"name": "BCA", "description": "Focuses on application development and basic coding."}
    ],
    'construction': [
        {"name": "B.Tech in Civil Engineering", "description": "Focuses on infrastructure, buildings, and structural design."},
        {"name": "Diploma in Construction Management", "description": "Practical course for managing construction projects."}
    ],
    'electronics': [
        {"name": "B.Tech in Electronics & Communication", "description": "Learn circuit design, embedded systems, and communication tech."},
        {"name": "Diploma in Embedded Systems", "description": "Hands-on training in microcontrollers and IoT devices."}
    ],

    # 🩺 Medical
    'helping people': [
        {"name": "MBBS", "description": "Comprehensive medical training to become a doctor."},
        {"name": "Bachelor of Physiotherapy", "description": "Focuses on rehabilitation and physical therapy."}
    ],
    'lab work': [
        {"name": "B.Sc in Medical Laboratory Technology", "description": "Training in diagnostic lab procedures and equipment."},
        {"name": "Diploma in Clinical Pathology", "description": "Specialized study of lab-based disease diagnosis."}
    ],
    'surgery': [
        {"name": "MS in General Surgery", "description": "Postgraduate surgical training for medical graduates."},
        {"name": "BDS", "description": "Bachelor's in Dental Surgery for oral healthcare careers."}
    ],

    # 💼 Business
    'marketing': [
        {"name": "BBA in Marketing", "description": "Learn branding, consumer behavior, and digital marketing."},
        {"name": "MBA in Marketing", "description": "Advanced strategies in market research and campaign planning."}
    ],
    'finance': [
        {"name": "B.Com in Finance", "description": "Basics of accounting, taxation, and financial analysis."},
        {"name": "MBA in Finance", "description": "Corporate finance, investment banking, and risk management."}
    ],
    'entrepreneurship': [
        {"name": "BBA in Entrepreneurship", "description": "Startup fundamentals, innovation, and business planning."},
        {"name": "PG Diploma in Entrepreneurship", "description": "Practical exposure to launching and scaling ventures."}
    ]
}
course_detail_map = {
    # 🛠️ Engineering

    'b.tech in computer science': {
        "name": "B.Tech in Computer Science",
        "description": "A 4-year engineering program focused on software development, algorithms, system architecture, and emerging technologies like AI and cybersecurity.",
        "syllabus": ["Data Structures", "Operating Systems", "Machine Learning", "Computer Networks", "Database Systems"],
        "career_paths": ["Software Engineer", "AI Developer", "Cybersecurity Analyst", "Cloud Architect"],
        "colleges": ["IIT Bombay", "IIIT Hyderabad", "NIT Surathkal"],
        "prep_tips": "Master programming languages like Python and Java. Build projects and contribute to open-source. Practice problem-solving on platforms like LeetCode or HackerRank.",
        

        "roadmap":{
       "career_path": "Full Stack Developer",
       "milestones": [
       {"stage": "Master DSA & OOP", "duration": "4 months"},
       {"stage": "Learn MERN stack", "duration": "3 months"},
       {"stage": "Build portfolio projects", "duration": "2 months"},
       {"stage": "Internship & job prep", "duration": "2 months"}
        ],
      "required_skills": ["JavaScript", "React", "Node.js", "MongoDB", "Git"],
      "certifications": ["Coursera Full Stack", "Scaler Academy", "Google Cloud Dev"],
      "learning_resources": ["GeeksforGeeks", "freeCodeCamp", "YouTube - CodeWithHarry"],
      "market_outlook": "Strong demand in startups and MNCs. Avg salary ₹6–12 LPA."
      }
    },

        'bca':{
    "name": "Bachelor of Computer Applications",
    "description": "Focuses on software development and coding fundamentals.",
    "syllabus": ["Data Structures", "Web Development", "Database Management"],
    "career_paths": ["Software Developer", "App Developer", "QA Analyst"],
    "colleges": ["Christ University", "Symbiosis", "Amity"],
    "prep_tips": "Practice coding daily. Learn basic algorithms and build small projects.",
    
    "roadmap": {
        "career_path": "Software Developer",
        "milestones": [
            {"stage": "Learn Python & Web Dev", "duration": "3 months"},
            {"stage": "Build 3 mini projects", "duration": "2 months"},
            {"stage": "Internship in tech company", "duration": "2 months"},
            {"stage": "Apply for full-time roles", "duration": "1 month"}
        ],
        "required_skills": ["Python", "HTML/CSS/JS", "Git", "SQL"],
        "certifications": ["Google IT Support", "NPTEL Web Development", "Hackerrank Python"],
        "learning_resources": ["freeCodeCamp", "GeeksforGeeks", "Coursera", "YouTube - Apna College"],
        "market_outlook": "High demand for full-stack developers. Avg salary ₹4–8 LPA. Remote jobs growing."
        }
    },

  
    'b.tech in civil engineering': {
        "name": "B.Tech in Civil Engineering",
        "description": "A 4-year program that teaches structural design, construction techniques, and environmental engineering.",
        "syllabus": ["Structural Engineering", "Fluid Mechanics", "Construction Materials", "Surveying", "Transportation Engineering"],
        "career_paths": ["Site Engineer", "Project Manager", "Urban Planner", "Structural Consultant"],
        "colleges": ["IIT Delhi", "NIT Trichy", "BITS Pilani"],
        "prep_tips": "Strengthen your math and physics fundamentals. Learn CAD tools like AutoCAD and STAAD Pro. Stay updated on sustainable construction practices.",

        "roadmap":{
  "career_path": "Structural Engineer",
  "milestones": [
    {"stage": "Learn AutoCAD & STAAD Pro", "duration": "3 months"},
    {"stage": "Understand building codes", "duration": "2 months"},
    {"stage": "Intern on-site projects", "duration": "3 months"},
    {"stage": "Prepare for GATE or private jobs", "duration": "2 months"}
  ],
  "required_skills": ["AutoCAD", "STAAD Pro", "Surveying", "Project Management"],
  "certifications": ["NPTEL Civil Design", "IS Codes Training", "PMI CAPM"],
  "learning_resources": ["Skill-Lync", "Coursera", "YouTube - Civil Guruji"],
  "market_outlook": "Steady demand in infrastructure. Avg salary ₹3–6 LPA."
}
    },

    'diploma in construction management': {
        "name": "Diploma in Construction Management",
        "description": "A practical course focused on managing construction projects, budgeting, and site operations.",
        "syllabus": ["Project Planning", "Construction Safety", "Materials Management", "Site Supervision"],
        "career_paths": ["Construction Supervisor", "Project Coordinator", "Quantity Surveyor"],
        "colleges": ["NICMAR Pune", "RICS School of Built Environment", "CEPT University"],
        "prep_tips": "Develop leadership and organizational skills. Learn project management tools like MS Project or Primavera. Understand basic legal and safety regulations.",

        "roadmap":{
  "career_path": "Construction Project Manager",
  "milestones": [
    {"stage": "Learn MS Project & budgeting", "duration": "2 months"},
    {"stage": "Understand site safety & labor laws", "duration": "2 months"},
    {"stage": "Intern with contractors", "duration": "3 months"},
    {"stage": "Apply for site supervisor roles", "duration": "1 month"}
  ],
  "required_skills": ["Project Planning", "Budgeting", "Site Supervision", "Safety Protocols"],
  "certifications": ["NICMAR CM Diploma", "OSHA Safety", "Primavera P6"],
  "learning_resources": ["RICS India", "YouTube - Civil Simplified", "Coursera"],
  "market_outlook": "Growing demand in urban development. Avg salary ₹3–5 LPA."
}
    },

    'b.tech in electronics & communication': {
        "name": "B.Tech in Electronics & Communication",
        "description": "A 4-year engineering course focused on electronic circuits, communication systems, and embedded technologies.",
        "syllabus": ["Analog Circuits", "Digital Signal Processing", "Microcontrollers", "Wireless Communication", "VLSI Design"],
        "career_paths": ["Embedded Systems Engineer", "Telecom Specialist", "IoT Developer", "Electronics Design Engineer"],
        "colleges": ["IIT Kharagpur", "NIT Warangal", "VIT Vellore"],
        "prep_tips": "Practice circuit design and simulation. Build IoT projects using Arduino or Raspberry Pi. Learn C/C++ and MATLAB for embedded systems.",

        "roadmap":{
  "career_path": "Embedded Systems Engineer",
  "milestones": [
    {"stage": "Learn C/C++ & microcontrollers", "duration": "3 months"},
    {"stage": "Build IoT projects", "duration": "2 months"},
    {"stage": "Intern in hardware labs", "duration": "3 months"},
    {"stage": "Apply for embedded roles", "duration": "2 months"}
  ],
  "required_skills": ["C/C++", "Arduino", "PCB Design", "RTOS"],
  "certifications": ["CDAC Embedded Systems", "NPTEL IoT", "Coursera Microcontrollers"],
  "learning_resources": ["YouTube - Pantech ProLabs", "Hackster.io", "MIT OpenCourseWare"],
  "market_outlook": "High demand in IoT and automotive. Avg salary ₹5–9 LPA."
}
    },

    'diploma in embedded systems': {
        "name": "Diploma in Embedded Systems",
        "description": "A hands-on course that teaches microcontroller programming, real-time systems, and hardware-software integration.",
        "syllabus": ["Embedded C", "RTOS Concepts", "Sensor Integration", "PCB Design"],
        "career_paths": ["Firmware Developer", "Hardware Engineer", "Automation Specialist"],
        "colleges": ["CDAC Pune", "NSIT Delhi", "SRM University"],
        "prep_tips": "Work on real-time projects. Learn debugging tools and protocols like UART, SPI, and I2C. Understand electronics fundamentals deeply.",

        "roadmap":{
  "career_path": "Embedded Technician",
  "milestones": [
    {"stage": "Learn microcontroller basics", "duration": "2 months"},
    {"stage": "Build simple sensor-based projects", "duration": "2 months"},
    {"stage": "Intern in electronics lab", "duration": "2 months"},
    {"stage": "Apply for technician roles", "duration": "1 month"}
  ],
  "required_skills": ["Embedded C", "Sensor Integration", "PCB Assembly", "Debugging"],
  "certifications": ["CDAC Technician Track", "PCB Design Workshop", "IoT Bootcamp"],
  "learning_resources": ["YouTube - TechieNest", "Pantech Solutions", "Coursera"],
  "market_outlook": "Growing demand in smart devices and automation. Avg salary ₹2.5–4.5 LPA."
}
    },

    # 🩺 Medical

    'mbbs': {
        "name": "MBBS",
        "description": "A 5.5-year undergraduate program that trains students to become licensed medical doctors. Includes clinical rotations, anatomy, pharmacology, and surgery.",
        "syllabus": ["Human Anatomy", "Physiology", "Pathology", "Pharmacology", "General Medicine", "Surgery"],
        "career_paths": ["General Physician", "Surgeon", "Pediatrician", "Medical Officer"],
        "colleges": ["AIIMS Delhi", "CMC Vellore", "JIPMER Puducherry"],
        "prep_tips": "Focus on NEET preparation. Build strong foundations in biology and chemistry. Practice clinical case studies and stay updated on medical ethics.",
       
       "roadmap": {
  "career_path": "General Physician",
  "milestones": [
    {"stage": "Complete MBBS + internship", "duration": "5.5 years"},
    {"stage": "Prepare for NEET PG", "duration": "6 months"},
    {"stage": "Choose specialization", "duration": "3 years"},
    {"stage": "Apply for hospital roles", "duration": "1 month"}
  ],
  "required_skills": ["Clinical Diagnosis", "Patient Care", "Pharmacology", "Medical Ethics"],
  "certifications": ["NEET PG", "AIIMS Residency", "FMGE (for abroad practice)"],
  "learning_resources": ["Prepladder", "Marrow", "YouTube - Dr. Najeeb"],
  "market_outlook": "High demand in public and private hospitals. Avg salary ₹8–15 LPA."
}
    },

    'bachelor of physiotherapy': {
        "name": "Bachelor of Physiotherapy",
        "description": "A 4-year course plus 6-month internship that trains students in physical rehabilitation, exercise therapy, and treating musculoskeletal and neurological conditions.",
        "syllabus": ["Anatomy", "Biomechanics", "Exercise Therapy", "Electrotherapy", "Orthopaedics", "Neurology"],
        "career_paths": ["Physiotherapist", "Rehabilitation Specialist", "Sports Injury Therapist"],
        "colleges": ["Manipal University", "Jamia Hamdard", "BFUHS Faridkot"],
        "prep_tips": "Develop strong knowledge of human anatomy. Practice hands-on therapy techniques. Stay fit and learn patient communication skills.",

        "roadmap":{
  "career_path": "Physiotherapist",
  "milestones": [
    {"stage": "Learn anatomy & therapy techniques", "duration": "6 months"},
    {"stage": "Intern in rehab centers", "duration": "3 months"},
    {"stage": "Get certified in sports therapy", "duration": "2 months"},
    {"stage": "Apply for hospital or clinic roles", "duration": "1 month"}
  ],
  "required_skills": ["Exercise Therapy", "Electrotherapy", "Patient Communication"],
  "certifications": ["AIAP Certification", "Sports Physio Diploma", "CPR & First Aid"],
  "learning_resources": ["Physiopedia", "YouTube - PhysioTutors", "Coursera"],
  "market_outlook": "Growing demand in sports and rehab. Avg salary ₹3–6 LPA."
}
    },

    'b.sc in medical laboratory technology': {
        "name": "B.Sc in Medical Laboratory Technology",
        "description": "A 3-year course focused on diagnostic testing, lab equipment handling, and disease detection through biological samples.",
        "syllabus": ["Clinical Biochemistry", "Microbiology", "Hematology", "Pathology", "Lab Management"],
        "career_paths": ["Lab Technician", "Clinical Analyst", "Pathology Assistant"],
        "colleges": ["St. John's Medical College", "BFUHS Faridkot", "SRM Institute of Science and Technology"],
        "prep_tips": "Learn lab safety protocols. Understand sample processing and diagnostic tools. Stay detail-oriented and precise in documentation.",
        "roadmap":{
  "career_path": "Lab Technician",
  "milestones": [
    {"stage": "Learn lab protocols & equipment", "duration": "3 months"},
    {"stage": "Intern in diagnostic labs", "duration": "2 months"},
    {"stage": "Get certified in pathology", "duration": "1 month"},
    {"stage": "Apply for hospital labs", "duration": "1 month"}
  ],
  "required_skills": ["Sample Analysis", "Lab Safety", "Biochemistry"],
  "certifications": ["MLT Certification", "NABL Lab Training", "Clinical Pathology Diploma"],
  "learning_resources": ["YouTube - LabTech", "MedlinePlus", "Coursera"],
  "market_outlook": "Essential role in diagnostics. Avg salary ₹2.5–5 LPA."
}
    },

    'diploma in clinical pathology': {
        "name": "Diploma in Clinical Pathology",
        "description": "A 2-year diploma course that trains students in analyzing tissue, blood, and body fluids to diagnose diseases.",
        "syllabus": ["Histopathology", "Cytology", "Clinical Biochemistry", "Lab Techniques"],
        "career_paths": ["Pathology Technician", "Lab Assistant", "Diagnostic Consultant"],
        "colleges": ["Kasturba Medical College", "BFUHS Faridkot", "Apollo Institute of Medical Sciences"],
        "prep_tips": "Focus on microscope work and sample analysis. Learn to interpret lab results accurately. Stay updated on diagnostic technologies.",

       "roadmap": {
  "career_path": "Pathology Technician",
  "milestones": [
    {"stage": "Learn histopathology & cytology", "duration": "3 months"},
    {"stage": "Hands-on lab training", "duration": "2 months"},
    {"stage": "Intern in diagnostic centers", "duration": "2 months"},
    {"stage": "Apply for technician roles", "duration": "1 month"}
  ],
  "required_skills": ["Microscopy", "Sample Preparation", "Lab Reporting", "Quality Control"],
  "certifications": ["Diploma in Pathology", "Lab Safety Training", "Clinical Biochemistry Workshop"],
  "learning_resources": ["YouTube - PathoLab", "Coursera - Clinical Lab Science", "NPTEL"],
  "market_outlook": "Growing need for skilled lab technicians. Avg salary ₹2–4.5 LPA."
}
    },

    'ms in general surgery': {
        "name": "MS in General Surgery",
        "description": "A 3-year postgraduate program for MBBS graduates, focusing on surgical techniques, patient care, and emergency procedures.",
        "syllabus": ["Surgical Anatomy", "Operative Techniques", "Trauma Surgery", "Postoperative Care"],
        "career_paths": ["General Surgeon", "Trauma Specialist", "Surgical Consultant"],
        "colleges": ["AIIMS Delhi", "PGIMER Chandigarh", "KGMU Lucknow"],
        "prep_tips": "Gain hands-on experience during MBBS. Practice suturing and surgical simulations. Stay calm under pressure and improve decision-making.",

        "roadmap": {
  "career_path": "Surgeon",
  "milestones": [
    {"stage": "Complete MBBS + MS", "duration": "8.5 years"},
    {"stage": "Practice surgical techniques", "duration": "1 year"},
    {"stage": "Join hospital or private practice", "duration": "1 month"}
  ],
  "required_skills": ["Surgical Anatomy", "Operative Techniques", "Emergency Care", "Decision Making"],
  "certifications": ["NEET PG", "MCI Registration", "Advanced Trauma Life Support"],
  "learning_resources": ["Surgical Mindset", "YouTube - Dr. Najeeb", "Marrow", "Coursera - Surgery Essentials"],
  "market_outlook": "High demand in hospitals and trauma centers. Avg salary ₹12–25 LPA."
}
    },

    'bds': {
        "name": "Bachelor of Dental Surgery",
        "description": "A 5-year undergraduate program that trains students in oral health, dental procedures, and maxillofacial surgery.",
        "syllabus": ["Dental Anatomy", "Oral Pathology", "Prosthodontics", "Orthodontics", "Oral Surgery"],
        "career_paths": ["Dentist", "Orthodontist", "Oral Surgeon"],
        "colleges": ["Maulana Azad Dental College", "Manipal College of Dental Sciences", "Government Dental College Mumbai"],
        "prep_tips": "Practice dental models and procedures. Learn patient interaction and hygiene protocols. Stay updated on cosmetic and restorative techniques.",

        "roadmap": {
  "career_path": "Dentist",
  "milestones": [
    {"stage": "Complete BDS + internship", "duration": "5 years"},
    {"stage": "Set up clinic or join hospital", "duration": "2 months"},
    {"stage": "Specialize in orthodontics or surgery", "duration": "2 years"}
  ],
  "required_skills": ["Dental Anatomy", "Oral Surgery", "Patient Handling", "Sterilization Protocols"],
  "certifications": ["DCI Registration", "Laser Dentistry", "Cosmetic Dentistry"],
  "learning_resources": ["DentalTown", "YouTube - Dental Mastery", "Coursera - Oral Health"],
  "market_outlook": "Growing demand in urban clinics and cosmetic dentistry. Avg salary ₹4–10 LPA."
}
    },

    # 📊 Marketing

    'bba in marketing': {
        "name": "BBA in Marketing",
        "description": "A 3-year undergraduate program focused on branding, consumer behavior, digital marketing, and sales strategies.",
        "syllabus": [
            "Principles of Management", "Business Communication", "Marketing Concepts",
            "Sales & Distribution Management", "Advertising & Public Relations",
            "Digital Marketing", "Market Research"
        ],
        "career_paths": ["Marketing Executive", "Brand Manager", "Digital Marketer", "Sales Strategist"],
        "colleges": ["NMIMS Mumbai", "Christ University", "Symbiosis Pune"],
        "prep_tips": "Stay updated on marketing trends. Learn tools like Google Ads, Canva, and HubSpot. Practice writing ad copy and analyzing consumer data.",

        "roadmap": {
  "career_path": "Digital Marketer",
  "milestones": [
    {"stage": "Learn SEO, SEM, and analytics", "duration": "3 months"},
    {"stage": "Run mock campaigns", "duration": "2 months"},
    {"stage": "Intern in marketing agency", "duration": "2 months"},
    {"stage": "Apply for entry-level roles", "duration": "1 month"}
  ],
  "required_skills": ["SEO", "Google Ads", "Social Media Strategy", "Analytics"],
  "certifications": ["Google Digital Garage", "HubSpot Academy", "Meta Blueprint"],
  "learning_resources": ["YouTube - Marketing Masterclass", "freeCodeCamp", "Coursera - Digital Marketing"],
  "market_outlook": "High demand across startups and e-commerce. Avg salary ₹4–8 LPA. Remote roles growing rapidly."
}
    },

    'mba in marketing': {
        "name": "MBA in Marketing",
        "description": "A 2-year postgraduate program that dives deep into strategic marketing, consumer analytics, and campaign management.",
        "syllabus": [
            "Strategic Marketing", "Consumer Behavior", "Marketing Analytics",
            "International Marketing", "Brand Management", "Retail Marketing"
        ],
        "career_paths": ["Marketing Manager", "Product Manager", "Market Analyst", "CMO"],
        "colleges": ["IIM Ahmedabad", "FMS Delhi", "SPJIMR Mumbai"],
        "prep_tips": "Build a portfolio of marketing campaigns. Learn data tools like Excel, Tableau, and Google Analytics. Practice case studies and pitch decks.",

        "roadmap": {
  "career_path": "Marketing Manager",
  "milestones": [
    {"stage": "Master strategic marketing & branding", "duration": "3 months"},
    {"stage": "Lead mock campaigns or case studies", "duration": "2 months"},
    {"stage": "Intern with FMCG or tech firms", "duration": "3 months"},
    {"stage": "Apply for mid-level roles", "duration": "1 month"}
  ],
  "required_skills": ["Brand Strategy", "Consumer Behavior", "Campaign Management", "Marketing Analytics"],
  "certifications": ["IIM Marketing Bootcamp", "Google Analytics", "LinkedIn Marketing Labs"],
  "learning_resources": ["Harvard Business Review", "YouTube - Think School", "Coursera - Strategic Marketing"],
  "market_outlook": "Strong demand in FMCG, tech, and consulting. Avg salary ₹8–15 LPA."
}
    },

    # 💰 Finance

    'b.com in finance': {
        "name": "B.Com in Finance",
        "description": "A 3-year undergraduate course covering accounting, taxation, financial systems, and investment basics.",
        "syllabus": [
            "Financial Accounting", "Business Economics", "Corporate Finance",
            "Taxation", "Banking & Insurance", "Investment Analysis"
        ],
        "career_paths": ["Accountant", "Financial Analyst", "Tax Consultant", "Banking Officer"],
        "colleges": ["Shri Ram College of Commerce", "Loyola College", "St. Xavier's Mumbai"],
        "prep_tips": "Master Excel and financial formulas. Stay updated on stock markets and RBI policies. Practice budgeting and financial reporting.",

        "roadmap": {
  "career_path": "Financial Analyst",
  "milestones": [
    {"stage": "Learn accounting & Excel modeling", "duration": "3 months"},
    {"stage": "Practice financial statement analysis", "duration": "2 months"},
    {"stage": "Intern in banks or fintech firms", "duration": "3 months"},
    {"stage": "Apply for analyst roles", "duration": "1 month"}
  ],
  "required_skills": ["Accounting", "Excel", "Financial Modeling", "Taxation"],
  "certifications": ["NISM Certification", "Tally ERP", "Coursera - Financial Markets"],
  "learning_resources": ["YouTube - CA Rachana Ranade", "Investopedia", "NPTEL - Finance"],
  "market_outlook": "Steady demand in banking and finance. Avg salary ₹3–6 LPA. Government exam eligibility included."
}
    },

    'mba in finance': {
        "name": "MBA in Finance",
        "description": "A 2-year postgraduate program focused on corporate finance, investment banking, and financial risk management.",
        "syllabus": [
            "Corporate Finance", "Investment Banking", "Financial Modeling",
            "Risk Management", "Mergers & Acquisitions", "Portfolio Management"
        ],
        "career_paths": ["Finance Manager", "Investment Banker", "Risk Analyst", "CFO"],
        "colleges": ["IIM Bangalore", "XLRI Jamshedpur", "ISB Hyderabad"],
        "prep_tips": "Learn financial modeling in Excel. Understand valuation techniques. Follow global financial news and practice case-based analysis.",

        "roadmap": {
  "career_path": "Investment Banker",
  "milestones": [
    {"stage": "Master valuation & M&A concepts", "duration": "3 months"},
    {"stage": "Build financial models", "duration": "2 months"},
    {"stage": "Intern with investment firms", "duration": "3 months"},
    {"stage": "Apply for analyst or associate roles", "duration": "1 month"}
  ],
  "required_skills": ["Valuation", "M&A", "Excel Modeling", "Risk Management"],
  "certifications": ["CFA Level 1", "Wall Street Prep", "Coursera - Investment Banking"],
  "learning_resources": ["YouTube - Finance with Sharan", "Corporate Finance Institute", "Harvard Online"],
  "market_outlook": "High-paying roles in finance hubs. Avg salary ₹10–20 LPA. Competitive but rewarding."
}
    },

    # 🚀 Entrepreneurship

    'bba in entrepreneurship': {
        "name": "BBA in Entrepreneurship",
        "description": "A 3-year undergraduate program that teaches startup fundamentals, business planning, innovation, and venture creation.",
        "syllabus": [
            "Entrepreneurship Development", "Business Planning", "Startup Finance",
            "Innovation Management", "Legal Aspects of Business", "Digital Strategy"
        ],
        "career_paths": ["Startup Founder", "Business Consultant", "Innovation Strategist"],
        "colleges": ["IIT Bombay (SOM)", "EDII Ahmedabad", "Ashoka University"],
        "prep_tips": "Work on a real startup idea. Learn lean startup methodology. Network with founders and attend pitch events or hackathons.",

        "roadmap": {
  "career_path": "Startup Founder",
  "milestones": [
    {"stage": "Learn lean startup & business model canvas", "duration": "2 months"},
    {"stage": "Build MVP and validate idea", "duration": "3 months"},
    {"stage": "Pitch to incubators or angel investors", "duration": "2 months"},
    {"stage": "Launch and scale product", "duration": "Ongoing"}
  ],
  "required_skills": ["Business Planning", "Pitching", "Digital Strategy", "Leadership"],
  "certifications": ["Startup India Learning Program", "Y Combinator Startup School", "Coursera - Entrepreneurship"],
  "learning_resources": ["YouTube - Backstage with Millionaires", "Harvard i-lab", "LinkedIn Learning"],
  "market_outlook": "High risk, high reward. Growing startup ecosystem in India. Funding opportunities expanding."
}
    },

    'pg diploma in entrepreneurship': {
        "name": "PG Diploma in Entrepreneurship",
        "description": "A 1-year practical program for aspiring entrepreneurs, focusing on venture creation, funding, and scaling strategies.",
        "syllabus": [
            "Startup Ecosystem", "Business Model Canvas", "Fundraising & Pitching",
            "Growth Hacking", "Leadership & Team Building", "Exit Strategies"
        ],
        "career_paths": ["Startup Founder", "Incubator Manager", "Venture Analyst"],
        "colleges": ["IIM Kozhikode", "NEN India", "EDC at IIM Calcutta"],
        "prep_tips": "Build a pitch deck. Learn from case studies of successful startups. Join incubators or startup accelerators for mentorship.",
        "roadmap": {
  "career_path": "Innovation Consultant / Founder",
  "milestones": [
    {"stage": "Refine business idea & market research", "duration": "2 months"},
    {"stage": "Build pitch deck & financial plan", "duration": "2 months"},
    {"stage": "Join incubator or accelerator", "duration": "3 months"},
    {"stage": "Launch product or service", "duration": "Ongoing"}
  ],
  "required_skills": ["Market Research", "Pitching", "Startup Finance", "Growth Hacking"],
  "certifications": ["IIM Kozhikode EDP", "NEN India", "Coursera - Innovation & Entrepreneurship"],
  "learning_resources": ["YouTube - Startup Stories", "MIT OpenCourseWare", "Entrepreneur.com"],
  "market_outlook": "Strong support from government and VCs. Avg salary varies; equity potential high."
}
    }
}