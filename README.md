# Coronavirus Diagnosis and Reporting System

![My Video](your_video_url)

The Coronavirus Diagnosis and Reporting System is a web application that allows users to perform symptom-based diagnosis for coronavirus and report their diagnosis results. It provides tools for tracking and visualizing diagnosis and symptom reports over time.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Images](#sample-images)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication:** Users can create accounts, log in, and manage their profiles.

- **Symptom-Based Diagnosis:** Users can select symptoms, describe their condition, and receive a diagnosis based on selected symptoms.

- **Diagnosis Reporting:** Users can report their diagnosis results along with additional information.

- **Diagnosis Tracking:** The system tracks and visualizes the number of diagnosis reports over time.

- **Symptom Tracking:** The system tracks and visualizes the number of symptom reports over time.

- **Live Reports:** Interactive charts for tracking and comparing diagnosis and symptom reports.

- **Profile Management:** Users can manage their profiles and change passwords.

- **Responsive Design:** The application is designed to work on various devices and screen sizes.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/coronavirus-diagnosis-system.git

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Configure the application by setting environment variables in a `.env` file. You can use the provided `.env.example` file as a template.
6. Run migrations:

   ```bash
   python manage.py migrate
   ```
7. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```
8. Run the development server:

   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`.

## Usage

1. Register an account or log in if you already have one.
2. Take a diagnosis: Select symptoms and provide additional details for a diagnosis.
3. Report a diagnosis: Optionally, you can report a diagnosis along with a description.
4. View your diagnosis and symptom reports on your profile.
5. Explore live reports to track and visualize the number of reports over time.

## Sample Images

![Sample Image 1](sample_image_1_link)
![Sample Image 2](sample_image_2_link)
![Sample Image 3](sample_image_3_link)

## Documentation

For detailed information on how to use and configure the application, please follow  this README file accordingly

## Contributing

We welcome contributions from the community. If you would like to contribute to the project, please follow our [Contributing Guidelines](link_to_contributing_guidelines).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or assistance, please contact us at: lchinecherem2018@gmail.com
