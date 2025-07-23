import { RotateCw } from 'lucide-react';

export default function LoadingSpinner() {
  return (
    <div className="flex justify-center items-center p-8">
      <RotateCw className="h-8 w-8 animate-spin" />
    </div>
  );
}
