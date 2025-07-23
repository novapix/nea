import { useState } from 'react';
import axios from 'axios';

type PasswordResetFormProps = {
  darkMode?: boolean;
};

export default function PasswordResetForm({ darkMode = false }: PasswordResetFormProps) {
  const [email, setEmail] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    
    try {
      await axios.post('/api/auth/password/reset/', { email });
      setSuccess(true);
    } catch (err: unknown) {
      if (axios.isAxiosError(err)) {
        setError(err.response?.data?.message || 'Failed to send reset link');
      } else {
        setError('An unexpected error occurred');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={`max-w-md w-full mx-auto ${darkMode ? 'bg-gray-800/80 backdrop-blur-sm' : 'bg-white/90 backdrop-blur-sm'} rounded-2xl shadow-xl overflow-hidden border ${darkMode ? 'border-gray-700' : 'border-gray-200'} transition-all duration-300 hover:shadow-2xl`}>
      <div className="p-8">
        <div className="text-center mb-8">
          <h2 className={`text-2xl font-bold ${darkMode ? 'text-white' : 'text-gray-800'} mb-2`}>
            Reset Password
          </h2>
          <p className={`text-sm ${darkMode ? 'text-gray-400' : 'text-gray-600'}`}>
            Enter your email to receive a secure reset link
          </p>
        </div>
        
        {success && (
          <div className="mb-6 p-4 bg-green-100/80 dark:bg-green-900/30 text-green-700 dark:text-green-300 rounded-lg transition-all duration-200">
            Password reset link sent! Check your email.
          </div>
        )}
        
        {error && (
          <div className="mb-6 p-4 bg-red-100/80 dark:bg-red-900/30 text-red-700 dark:text-red-300 rounded-lg transition-all duration-200">
            {error}
          </div>
        )}
        
        {!success && (
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-2">
              <label className={`block text-sm font-medium ${darkMode ? 'text-gray-300' : 'text-gray-700'} transition-colors duration-200`}>
                Email Address
              </label>
              <div className="relative">
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className={`w-full px-4 py-3 text-sm rounded-lg transition-all duration-200 ${darkMode ? 'bg-gray-700/50 border-gray-600 focus:ring-indigo-500 focus:border-indigo-500 text-gray-200' : 'bg-white border-gray-300 focus:ring-indigo-300 focus:border-indigo-300 text-gray-900'} border focus:ring-2 focus:ring-opacity-50`}
                  required
                  disabled={isLoading}
                />
                <span className={`absolute right-3 top-1/2 transform -translate-y-1/2 text-xs ${darkMode ? 'text-gray-400' : 'text-gray-500'} transition-colors duration-200`}>
                  {email.length}/254
                </span>
              </div>
            </div>
            
            <button
              type="submit"
              disabled={isLoading}
              className={`w-full py-3 px-4 rounded-xl transition-all duration-300 ${darkMode ? 'bg-indigo-600 hover:bg-indigo-700' : 'bg-indigo-600 hover:bg-indigo-700'} text-white font-medium flex justify-center items-center gap-2 ${isLoading ? 'opacity-90' : 'hover:shadow-md'} transform hover:-translate-y-0.5`}
            >
              {isLoading ? (
                <>
                  <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Sending...
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clipRule="evenodd" />
                  </svg>
                  Send Reset Link
                </>
              )}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
