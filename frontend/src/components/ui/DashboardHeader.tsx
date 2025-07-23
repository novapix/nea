import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { useAuth } from '@/hooks/useAuth';

type DashboardHeaderProps = {
  title: string;
  description: string;
};

export default function DashboardHeader({ title, description }: DashboardHeaderProps) {
  const { user, avatarUrl, logout } = useAuth();
  
  return (
    <Card className="flex justify-between items-center p-6 rounded-lg">
      <div>
        <h1 className="text-4xl font-bold tracking-tight">{title}</h1>
        <p className="text-muted-foreground">{description}</p>
      </div>
      
      {user && (
        <div className="flex items-center gap-4">
          <div className="text-right">
            <p className="text-sm text-muted-foreground">Welcome back,</p>
            <p className="font-medium">{user.name}</p>
          </div>
          {avatarUrl ? (
            <img 
              src={avatarUrl} 
              alt="User Avatar"
              className="h-10 w-10 rounded-full object-cover"
            />
          ) : (
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-primary text-primary-foreground">
              <span className="text-sm font-medium">{user.name?.charAt(0) || 'U'}</span>
            </div>
          )}
          <Button 
            variant="destructive" 
            size="sm"
            onClick={() => {
              logout();
              window.location.href = '/login';
            }}
          >
            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
            </svg>
            Logout
          </Button>
        </div>
      )}
    </Card>
  );
}
