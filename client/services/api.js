import axios from 'axios';

// Hardcoded backend API base URL for production testing
const API = axios.create({
  baseURL: 'https://mazingira-1.onrender.com/api',
});

API.interceptors.request.use((req) => {
  if (localStorage.getItem('profile')) {
    req.headers.Authorization = `Bearer ${JSON.parse(localStorage.getItem('profile')).token}`;
  }
  return req;
});

export default API;
