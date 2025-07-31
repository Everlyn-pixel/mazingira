import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from '../store/store.js';
import './Buttons.css';
import Header from '../components/layout/Header';
import Footer from '../components/layout/Footer';
import Home from '../pages/Home';
import Login from '../pages/auth/Login';
import Register from '../pages/auth/Register';
import OrganizationList from '../pages/donor/OrganizationList';
import OrganizationDetails from '../pages/donor/OrganizationDetails';
import Donation from '../pages/donor/Donation';
import DonorDashboard from '../pages/donor/Dashboard';
import OrganizationDashboard from '../pages/organization/Dashboard';
import AdminDashboard from '../pages/admin/Dashboard';
import BeneficiaryStories from '../pages/donor/BeneficiaryStories';
import PrivateRoute from '../components/common/PrivateRoute';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/organizations" element={<OrganizationList />} />
            <Route path="/organizations/:id" element={<OrganizationDetails />} />
            <Route path="/donate/:id" element={<Donation />} />
            <Route path="/beneficiaries/:beneficiaryId/stories" element={<BeneficiaryStories />} />
            <Route
              path="/donor/dashboard"
              element={
                <PrivateRoute>
                  <DonorDashboard />
                </PrivateRoute>
              }
            />
            <Route
              path="/organization/dashboard"
              element={
                <PrivateRoute>
                  <OrganizationDashboard />
                </PrivateRoute>
              }
            />
            <Route
              path="/admin/dashboard"
              element={
                <PrivateRoute>
                  <AdminDashboard />
                </PrivateRoute>
              }
            />
          </Routes>
        </main>
        <Footer />
      </Router>
    </Provider>
  );
}

export default App;
