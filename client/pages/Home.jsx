import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Import the new CSS file

const Home = () => {
  const [showDonorForm, setShowDonorForm] = useState(false);
  const [showOrgForm, setShowOrgForm] = useState(false);

  const handleDonorSubmit = (e) => {
    e.preventDefault();
    alert('Donor submitted!');
    setShowDonorForm(false);
  };

  const handleOrgSubmit = (e) => {
    e.preventDefault();
    alert('Organization application submitted!');
    setShowOrgForm(false);
  };

  return (
    <div className="container mt-5 text-center">
      <div className="bg-light p-5 rounded-lg">
        <h1 className="display-5 text-success">Welcome to Mazingira - Your Environmental Donation Platform</h1>
        <p className="lead mt-3 mb-4">
          Support organizations working to protect our planet. Set up donations, track your impact, and build a sustainable future.
        </p>
        <div className="mb-4">
          <button className="btn btn-success mx-2">Explore Organizations</button>
          <button className="btn btn-outline-success mx-2" onClick={() => setShowDonorForm(true)}>Become a Donor</button>
        </div>

        <div className="row">
          <div className="col-md-4 mb-3">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title text-success">For Donors</h5>
                <p className="card-text">Easily support environmental causes and track your impact over time.</p>
                <button className="btn btn-info" onClick={() => setShowDonorForm(true)}>Join as Donor</button>
              </div>
            </div>
          </div>

          <div className="col-md-4 mb-3">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title text-success">For Organizations</h5>
                <p className="card-text">Apply to receive donations and connect with supporters worldwide.</p>
                <button className="btn btn-success" onClick={() => setShowOrgForm(true)}>Apply as Organization</button>
              </div>
            </div>
          </div>

          <div className="col-md-4 mb-3">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title text-success">For Administrators</h5>
                <p className="card-text">Manage platform data, approve organizations, and oversee donations.</p>
                <Link to="/login" className="btn btn-warning text-white">Admin Login</Link>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Donor Modal */}
      {showDonorForm && (
        <div className="modal-backdrop-custom">
          <div className="modal-content-custom">
            <div className="modal-header-custom">
              <h5>Donor Signup</h5>
            </div>
            <form onSubmit={handleDonorSubmit}>
              <input type="text" placeholder="Name" className="form-control mb-2" required />
              <input type="email" placeholder="Email" className="form-control mb-3" required />
              <button className="btn btn-success w-100 mb-2" type="submit">Submit</button>
              <button className="btn btn-secondary w-100" onClick={() => setShowDonorForm(false)}>Cancel</button>
            </form>
          </div>
        </div>
      )}

      {/* Organization Modal */}
      {showOrgForm && (
        <div className="modal-backdrop-custom">
          <div className="modal-content-custom">
            <div className="modal-header-custom">
              <h5>Organization Application</h5>
            </div>
            <form onSubmit={handleOrgSubmit}>
              <input type="text" placeholder="Organization Name" className="form-control mb-2" required />
              <textarea placeholder="Why should we approve you?" className="form-control mb-3" rows="3" required />
              <button className="btn btn-success w-100 mb-2" type="submit">Submit</button>
              <button className="btn btn-secondary w-100" onClick={() => setShowOrgForm(false)}>Cancel</button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;

