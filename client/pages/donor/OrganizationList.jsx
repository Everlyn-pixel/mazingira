import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import API from '../../services/api';

const OrganizationList = () => {
  const [organizations, setOrganizations] = useState([]);

  useEffect(() => {
    const fetchOrganizations = async () => {
      try {
        const { data } = await API.get('/organizations');
        setOrganizations(data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchOrganizations();
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="mb-4 text-center">Organizations</h2>
      <div className="row">
        {organizations.map((org) => (
          <div key={org.id} className="col-md-4 mb-4">
            <div className="card h-100">
              <img src={`https://via.placeholder.com/300x200?text=Org+${org.id}`} className="card-img-top" alt={org.name} />
              <div className="card-body d-flex flex-column">
                <h5 className="card-title">{org.name}</h5>
                <p className="card-text">{org.description ? org.description.substring(0, 100) + '...' : 'No description available.'}</p>
                <Link to={`/organizations/${org.id}`} className="btn-custom btn-custom-primary mt-auto">View Details</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default OrganizationList;
