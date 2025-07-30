import React from 'react';

const OrganizationDashboard = () => {
  return (
    <div className="container mt-5">
      <div className="card">
        <div className="card-header">
          <h2>Organization Dashboard</h2>
        </div>
        <div className="card-body">
          <p>Welcome to your organization dashboard. Here you can manage your organization details, view donations, and post stories.</p>
          {/* Add more organization-specific content here */}
        </div>
      </div>
    </div>
  );
};

export default OrganizationDashboard;