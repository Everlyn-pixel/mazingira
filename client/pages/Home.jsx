import React from 'react';

const Home = () => {
  return (
    <div className="container mt-5">
      <div className="jumbotron bg-light p-5 rounded-lg m-3">
        <h1 className="display-4">Welcome to Mazingira</h1>
        <p className="lead">Donate to environmental preservation organizations and help combat environmental degradation.</p>
        <hr className="my-4" />
        <img src="https://via.placeholder.com/800x400?text=Environmental+Preservation" className="img-fluid mb-4" alt="Environmental Preservation" />
        <p>Join us in making a difference for our planet.</p>
      </div>
    </div>
  );
};

export default Home;
