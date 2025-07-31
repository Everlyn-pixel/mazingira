import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import API from '../../services/api';

const Donation = () => {
  const { id } = useParams();
  const [amount, setAmount] = useState(0);
  const [isRecurring, setIsRecurring] = useState(false);
  const [isAnonymous, setIsAnonymous] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.post(`/donate/${id}`, { amount, isRecurring, isAnonymous });
      alert('Donation successful!');
    } catch (error) {
      console.error(error);
      alert('Donation failed.');
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">Donate to Organization {id}</div>
            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="amountInput" className="form-label">Amount</label>
                  <input
                    type="number"
                    className="form-control"
                    id="amountInput"
                    placeholder="Enter amount"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                  />
                </div>
                <div className="mb-3 form-check">
                  <input
                    type="checkbox"
                    className="form-check-input"
                    id="recurringCheck"
                    checked={isRecurring}
                    onChange={(e) => setIsRecurring(e.target.checked)}
                  />
                  <label className="form-check-label" htmlFor="recurringCheck">Make this a recurring donation</label>
                </div>
                <div className="mb-3 form-check">
                  <input
                    type="checkbox"
                    className="form-check-input"
                    id="anonymousCheck"
                    checked={isAnonymous}
                    onChange={(e) => setIsAnonymous(e.target.checked)}
                  />
                  <label className="form-check-label" htmlFor="anonymousCheck">Donate anonymously</label>
                </div>
                <button type="submit" className="btn-custom btn-custom-success">Donate</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Donation;