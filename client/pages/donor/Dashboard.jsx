import React from 'react';

const DonorDashboard = () => {
  return (
    <div className="container mt-5">
      <div className="card">
        <div className="card-header">
          <h2>Donor Dashboard</h2>
        </div>
        <div className="card-body">
          <p>Welcome to your donor dashboard. Here you can manage your donations and view beneficiary stories.</p>
          {/* Add more donor-specific content here */}
        </div>
      </div>
    </div>
  );
};

export default DonorDashboard;