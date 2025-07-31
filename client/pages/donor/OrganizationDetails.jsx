import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import API from '../../services/api';

const OrganizationDetails = () => {
  const { id } = useParams();
  const [organization, setOrganization] = useState(null);

  useEffect(() => {
    const fetchOrganization = async () => {
      try {
        const { data } = await API.get(`/organizations/${id}`);
        setOrganization(data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchOrganization();
  }, [id]);

  if (!organization) {
    return <div className="container mt-5">Loading...</div>;
  }

  return (
    <div className="container mt-5">
      <div className="card mb-3">
        <img src={`https://via.placeholder.com/800x400?text=Organization+${organization.id}+Details`} className="card-img-top" alt={organization.name} />
        <div className="card-body">
          <h2 className="card-title">{organization.name}</h2>
          <p className="card-text">{organization.description}</p>
          <Link to={`/donate/${id}`} className="btn-custom btn-custom-primary">Donate Now</Link>
        </div>
      </div>
    </div>
  );
};

export default OrganizationDetails;
