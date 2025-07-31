import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { login } from '../../store/slices/authSlice';
import API from '../../services/api';

const Register = () => {
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const dispatch = useDispatch();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await API.post('/auth/register', formData);
      dispatch(login(data));
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header text-center">Register</div>
            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="nameInput" className="form-label">Name</label>
                  <input type="text" className="form-control" id="nameInput" name="name" placeholder="Enter your name" onChange={handleChange} />
                </div>
                <div className="mb-3">
                  <label htmlFor="emailInput" className="form-label">Email address</label>
                  <input type="email" className="form-control" id="emailInput" name="email" placeholder="Enter email" onChange={handleChange} />
                </div>
                <div className="mb-3">
                  <label htmlFor="passwordInput" className="form-label">Password</label>
                  <input type="password" className="form-control" id="passwordInput" name="password" placeholder="Password" onChange={handleChange} />
                </div>
                <button type="submit" className="btn-custom btn-custom-primary w-100">Register</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;