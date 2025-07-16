import { Routes, Route, Navigate, BrowserRouter } from 'react-router-dom'
import { Login, Home, Dashboard } from '@/pages'
import './App.css'

function App() {
  const isAuthenticated = !!localStorage.getItem('access_token');
  console.log('App render - isAuthenticated:', isAuthenticated);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route 
          path="/login" 
          element={isAuthenticated ? (
            <>
              {console.log('Redirecting to dashboard from login')}
              <Navigate to="/dashboard" />
            </>
          ) : <Login />} 
        />
        <Route 
          path="/dashboard" 
          element={isAuthenticated ? (
            <Dashboard />
          ) : (
            <>
              {console.log('Redirecting to login from dashboard')}
              <Navigate to="/login" />
            </>
          )} 
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App
