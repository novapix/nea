import { useState } from 'react';
import { Input } from '@/components/ui/input';
import { useAuth } from '@/context/AuthContext';
import axios from 'axios';
import type { AuthUser } from '@/context/AuthContext';

export function AvatarUpload() {
  const { user, setUser } = useAuth();
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file || !user) return;

    setIsUploading(true);
    setError('');
    
    try {
      const formData = new FormData();
      formData.append('image', file);
      
      const response = await axios.post<{image: string}>('/api/api/avatar/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      
      // Update user context with new avatar
      if (user) {
        setUser({
          ...user,
          avatar: response.data.image
        } as AuthUser);
      }
    } catch (err) {
      setError('Failed to upload avatar');
      console.error(err);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="flex flex-col gap-2">
      <Input 
        type="file" 
        accept="image/jpeg,image/png"
        onChange={handleFileChange}
        disabled={isUploading}
      />
      {error && <p className="text-red-500 text-sm">{error}</p>}
    </div>
  );
}
