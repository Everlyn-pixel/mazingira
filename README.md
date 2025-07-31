# mazingira
# 🌍 Mazingira - Environmental Donation Platform

**Mazingira** is a full-stack donation platform designed to support environmental preservation organizations through regular and one-time donations. The platform connects donors with vetted organizations and simplifies the donation process, encouraging sustainable contributions to help combat environmental degradation.

## 🧠 Problem Statement

Environmental degradation is the deterioration of the Earth’s natural environment through the excessive consumption of resources such as air, water, and soil, the destruction of ecosystems, and the loss of wildlife. This leads to consequences that threaten the survival of humanity. Despite the urgency, there are currently limited resources available to fight this problem.

## 💡 Solution

Mazingira offers a digital platform where:
- Donors can set up one-time or recurring (e.g. monthly) donations
- Organizations can showcase their impact and receive funds
- Administrators manage platform integrity and organization approvals

The goal is to automate and simplify the donation process to support the sustainability and growth of environmental conservation efforts.

---

## 👥 Team

**Full Stack Application**
- **Frontend**: React.js + Redux Toolkit
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Testing**: Jest (frontend), Minitests (backend)

---

## 👤 Users & Roles

### Donor
- Browse available environmental organizations
- Register and log into the platform
- Choose organizations to support
- Make one-time or recurring donations
- Choose to donate anonymously
- Receive monthly donation reminders
- Read stories about donation impact
- Use third-party payment gateways like PayPal/Stripe

### Organization
- Apply to be listed on the platform
- Once approved, manage their profile and details
- View all donations (anonymous & non-anonymous)
- View total donations received
- Create and publish stories about beneficiaries
- Manage beneficiary details and inventory distributed

### Administrator
- Review and approve/reject organization applications
- Manage (delete) organizations
- Ensure platform compliance and content quality

---

## 📌 Features

- Authentication & authorization
- Organization application and approval flow
- Donation options (one-time & recurring)
- Anonymous donation support
- Beneficiary storytelling system
- Monthly donation reminders
- Admin dashboard

---

## 🛠️ Tech Stack

| Tech            | Description                      |
|-----------------|----------------------------------|
| React.js        | Frontend framework               |
| Redux Toolkit   | State management                 |
| Python Flask    | Backend API framework            |
| PostgreSQL      | Relational database              |
| Jest            | Frontend testing framework       |
| Minitests       | Backend testing                  |
| Figma           | UI/UX wireframes (mobile-first)  |

---

### Frontend
```bash
cd client
npm install
npm run dev
vercel link 
https://mazingira-jfiv.vercel.app/