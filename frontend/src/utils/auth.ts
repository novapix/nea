import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

type JwtPayload = {
  exp: number;
  [key: string]: any;
};

export const isTokenValid = (token: string | null): boolean => {
  if (!token) return false;
  try {
    const decoded = jwtDecode<JwtPayload>(token);
    return decoded.exp * 1000 > Date.now();
  } catch {
    return false;
  }
};

export const getCurrentUserRole = (): string | null => {
  const token = localStorage.getItem('accessToken');
  if (!token || !isTokenValid(token)) return null;
  
  try {
    const decoded = jwtDecode<JwtPayload>(token);
    return decoded.role || null;
  } catch {
    return null;
  }
};

export const authRequest = async (config: {
  url: string;
  method: 'get' | 'post' | 'put' | 'delete' | 'patch';
  data?: any;
  headers?: Record<string, string>;
}) => {
  let accessToken = localStorage.getItem('accessToken');
  const refreshToken = localStorage.getItem('refreshToken');

  // Validate tokens before making request
  if (!accessToken || !refreshToken || !isTokenValid(refreshToken)) {
    redirectToLogin();
    throw new Error('Authentication required');
  }

  // Refresh token if expired
  if (!isTokenValid(accessToken)) {
    try {
      accessToken = await refreshAccessToken();
      if (!accessToken) throw new Error('Token refresh failed');
    } catch (error) {
      redirectToLogin();
      throw error;
    }
  }

  try {
    // First attempt with current token
    return await axios({
      ...config,
      headers: {
        ...config.headers,
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    });
  } catch (error: any) {
    // If unauthorized, try to refresh token
    if (error.response?.status === 401) {
      try {
        const newAccessToken = await refreshAccessToken();
        if (!newAccessToken) {
          throw new Error('Session expired');
        }
        
        // Retry with new token
        return await axios({
          ...config,
          headers: {
            ...config.headers,
            'Authorization': `Bearer ${newAccessToken}`,
            'Content-Type': 'application/json'
          }
        });
      } catch (refreshError) {
        // If refresh fails, redirect to login
        redirectToLogin();
        throw new Error('Session expired');
      }
    }
    
    throw error;
  }
};

export const refreshAccessToken = async (): Promise<string | null> => {
  try {
    const refreshToken = localStorage.getItem('refreshToken');
    if (!refreshToken) {
      redirectToLogin();
      return null;
    }

    const response = await axios.post('/api/token/refresh/', {
      refresh: refreshToken
    });

    const newAccessToken = response.data.access;
    localStorage.setItem('accessToken', newAccessToken);
    return newAccessToken;
  } catch (error) {
    console.error('Failed to refresh token:', error);
    redirectToLogin();
    return null;
  }
};

const redirectToLogin = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  window.location.href = '/login';
};

export const isAuthenticated = () => {
  return !!localStorage.getItem('accessToken');
};

export const getAccessToken = () => {
  return localStorage.getItem('accessToken');
    };
