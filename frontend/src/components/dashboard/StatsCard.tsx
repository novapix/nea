import { ArrowTrendingUpIcon, ArrowTrendingDownIcon } from '@heroicons/react/24/outline';
import { cn } from '@/lib/utils';

type StatsCardProps = {
  title: string;
  value: string | number;
  change?: number;
  icon: React.ReactNode;
  className?: string;
};

export default function StatsCard({ 
  title, 
  value, 
  change = 0, 
  icon, 
  className = '' 
}: StatsCardProps) {
  const isPositive = change >= 0;

  return (
    <div className={cn(
      'bg-white dark:bg-gray-800 rounded-xl shadow-md dark:shadow-gray-700/50 p-6 transition-all hover:shadow-lg',
      className
    )}>
      <div className="flex justify-between items-start">
        <div>
          <p className="text-sm font-medium text-gray-500 dark:text-gray-400">{title}</p>
          <p className="text-2xl font-bold text-gray-800 dark:text-white mt-1">{value}</p>
        </div>
        <div className="p-3 rounded-lg bg-blue-100 dark:bg-blue-900/50 text-blue-600 dark:text-blue-300">
          {icon}
        </div>
      </div>

      {change !== 0 && (
        <div className="flex items-center mt-4 text-sm">
          {isPositive ? (
            <ArrowTrendingUpIcon className="w-4 h-4 text-green-500 mr-1" />
          ) : (
            <ArrowTrendingDownIcon className="w-4 h-4 text-red-500 mr-1" />
          )}
          <span className={isPositive ? 'text-green-600 dark:text-green-400' : 'text-red-600 dark:text-red-400'}>
            {Math.abs(change)}% {isPositive ? 'increase' : 'decrease'}
          </span>
          <span className="text-gray-500 dark:text-gray-400 ml-1">vs last period</span>
        </div>
      )}
    </div>
  );
}
