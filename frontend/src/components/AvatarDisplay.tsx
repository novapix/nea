import { useAuth } from '@/context/AuthContext';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

export function AvatarDisplay() {
  const { user } = useAuth();
  
  return (
    <Avatar className="h-10 w-10">
      {user?.avatar ? (
        <AvatarImage 
          src={user.avatar} 
          alt={`${user.name}'s avatar`}
        />
      ) : (
        <AvatarFallback>
          {user?.name?.charAt(0) || user?.email?.charAt(0) || 'U'}
        </AvatarFallback>
      )}
    </Avatar>
  );
}
