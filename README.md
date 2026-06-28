The project aims to develop a web-based real estate property listing platform that allows users to browse available properties through structured and user-friendly pages. The system will display property listings with images, descriptions, prices, locations, and other relevant details. Users will be able to search and view properties and contact agents directly through inquiry forms. The platform will support different user roles, including administrators, agents, and customers, to ensure efficient property management and communication.


# REAL ESTATE PROPERTY LISTING WEBSITE – TEAM ROLES AND RESPONSIBILITIES

To ensure that our project is developed efficiently and consistently, each team member should focus on the responsibilities assigned below. Please adhere to your role and communicate with the group if you need to add features or make significant changes.

## 1. Frontend Developer

**Primary responsibility:** Design and build the user interface.

### Tasks:

* Design all website pages using HTML, CSS, and JavaScript.
* Create:

  * Home page
  * Property listing page
  * Property details page
  * Login page
  * Registration page
  * Agent dashboard page
  * Admin dashboard page
  * Contact/inquiry forms
* Create navigation bars, footers, buttons, cards, and layouts.
* Ensure the website is responsive on desktop and mobile devices.
* Integrate frontend templates with backend data provided by the backend developer.

---

## 2. Backend Developer

**Primary responsibility:** Build the application's business logic and authentication system.

### Tasks:

* Create and configure the Django project.
* Create the custom User model.
* Implement:

  * User registration
  * Login/logout
  * Role-based access control (Admin, Agent, Customer)
* Develop property CRUD operations:

  * Create property
  * View property
  * Update property
  * Delete property
* Implement inquiry submission and management.
* Create dashboards for Admin and Agent users.
* Implement permissions and security.
* Connect all components of the system.

---

## 3. Database Developer

**Primary responsibility:** Design and manage the database structure.

### Tasks:

* Design the database schema.
* Create and maintain models for:

  * User
  * Property
  * PropertyImage
  * Inquiry
* Define relationships between models.
* Create migrations.
* Ensure data integrity and normalization.
* Assist in database optimization and testing.

### Example relationships:

User (Agent)
↓
Property
↓
PropertyImage

Property
↓
Inquiry

---

## 4. Search and Filter Developer

**Primary responsibility:** Implement property searching and filtering functionality.

### Tasks:

* Develop property search features.
* Implement filters such as:

  * Property location
  * Property type
  * Price range
  * Number of bedrooms
  * Availability status
* Create search forms.
* Ensure search results display correctly.
* Optimize search performance.

Example:

* Search: "Nairobi apartments"
* Filter:

  * Price: KES 2M–5M
  * Bedrooms: 3
  * Type: Apartment

---

## 5. Image Upload Developer

**Primary responsibility:** Manage property image uploads and display.

### Tasks:

* Implement image upload functionality for agents.
* Configure Django media settings.
* Create the PropertyImage model.
* Allow multiple images per property.
* Validate uploaded image formats.
* Store images in the media directory.
* Display uploaded images on:

  * Property listing pages
  * Property detail pages
* Handle image deletion and updates.

Example:
Property
├── Image 1
├── Image 2
└── Image 3

---

## Team Rule

* Follow the agreed project scope.
* Inform the group before introducing new features.
* Push code regularly to GitHub.
* Communicate any challenges early to avoid delays.

NB -Ensure you install all the requirements from the requirements.txt file in the virtual environment before writing any code.  ( pip install -r requirements.txt)
