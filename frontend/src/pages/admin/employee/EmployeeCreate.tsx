import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { useBranches } from '@/hooks/useBranches';
import axios from 'axios';
import { toast } from 'react-hot-toast';

type EmployeeFormData = {
  name: string;
  email: string;
  contact_no: string;
  employee_code: string;
  address: string;
  citizenship_no: string;
  branch_id: number;
};

export default function EmployeeCreate() {
  const { register, handleSubmit, formState: { errors }, setError } = useForm<EmployeeFormData>();
  const navigate = useNavigate();
  const { theme } = useTheme();
  const { branches } = useBranches();
  const { user } = useAuth();
  
  const onSubmit = async (data: EmployeeFormData) => {
    try {
      const response = await axios.post('/api/employees/create/', data);
      toast.success('Employee created successfully!');
      navigate('/admin/employees');
    } catch (error) {
      if (axios.isAxiosError(error)) {
        if (error.response?.status === 401) {
          toast.error('Session expired. Please login again.');
          return;
        }
        
        const errorData = error.response?.data;
        if (errorData?.errors) {
          Object.entries(errorData.errors).forEach(([field, message]) => {
            const errorMessage = Array.isArray(message) 
              ? message.join(' ') 
              : typeof message === 'string' 
                ? message 
                : '';
            setError(field as keyof EmployeeFormData, {
              type: 'manual',
              message: errorMessage
            });
          });
        } else {
          toast.error(errorData?.detail || 'Failed to create employee');
        }
      } else {
        toast.error('An unexpected error occurred');
      }
    }
  };

  return (
    <div className={`p-6 ${theme === 'dark' ? 'bg-gray-900' : 'bg-white'} min-h-screen`}>
      <div className="max-w-4xl mx-auto">
        <h1 className={`text-2xl font-bold mb-8 ${theme === 'dark' ? 'text-white' : 'text-gray-800'}`}>
          Create New Employee
        </h1>
        
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Name */}
            <div>
              <Label htmlFor="name" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Full Name
              </Label>
              <Input
                id="name"
                {...register('name', { required: 'Name is required' })}
                className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
              />
              {errors.name && <p className="mt-1 text-sm text-red-500">{errors.name.message}</p>}
            </div>
            
            {/* Email */}
            <div>
              <Label htmlFor="email" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Email
              </Label>
              <Input
                id="email"
                type="email"
                {...register('email', { 
                  required: 'Email is required',
                  pattern: { value: /^\S+@\S+\.\S+$/, message: 'Enter a valid email' }
                })}
                className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
              />
              {errors.email && <p className="mt-1 text-sm text-red-500">{errors.email.message}</p>}
            </div>
            
            {/* Contact Number */}
            <div>
              <Label htmlFor="contact_no" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Contact Number
              </Label>
              <Input
                id="contact_no"
                {...register('contact_no', { required: 'Contact number is required' })}
                className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
              />
              {errors.contact_no && <p className="mt-1 text-sm text-red-500">{errors.contact_no.message}</p>}
            </div>
            
            {/* Employee Code */}
            <div>
              <Label htmlFor="employee_code" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Employee Code
              </Label>
              <Input
                id="employee_code"
                {...register('employee_code', { required: 'Employee code is required' })}
                className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
              />
              {errors.employee_code && <p className="mt-1 text-sm text-red-500">{errors.employee_code.message}</p>}
            </div>
            
            {/* Branch */}
            <div>
              <Label htmlFor="branch_id" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Branch
              </Label>
              <Select
                name="branch_id"
                defaultValue=""
                onValueChange={(value) => {}}
              >
                <SelectTrigger className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}>
                  <SelectValue placeholder="Select branch" />
                </SelectTrigger>
                <SelectContent className={theme === 'dark' ? 'bg-gray-800 border-gray-700' : ''}>
                  {branches.map((branch) => (
                    <SelectItem key={branch.id} value={branch.id.toString()}>
                      {branch.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            
            {/* Citizenship Number */}
            <div>
              <Label htmlFor="citizenship_no" className={theme === 'dark' ? 'text-gray-300' : ''}>
                Citizenship Number
              </Label>
              <Input
                id="citizenship_no"
                {...register('citizenship_no', { required: 'Citizenship number is required' })}
                className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
              />
              {errors.citizenship_no && <p className="mt-1 text-sm text-red-500">{errors.citizenship_no.message}</p>}
            </div>
          </div>
          
          {/* Address */}
          <div>
            <Label htmlFor="address" className={theme === 'dark' ? 'text-gray-300' : ''}>
              Address
            </Label>
            <Input
              id="address"
              {...register('address', { required: 'Address is required' })}
              className={`mt-1 ${theme === 'dark' ? 'bg-gray-800 border-gray-700 text-white' : ''}`}
            />
            {errors.address && <p className="mt-1 text-sm text-red-500">{errors.address.message}</p>}
          </div>
          
          <div className="flex justify-end gap-4 pt-4">
            <Button 
              type="button" 
              variant="outline"
              onClick={() => navigate(-1)}
              className={theme === 'dark' ? 'border-gray-700 hover:bg-gray-800' : ''}
            >
              Cancel
            </Button>
            <Button type="submit">
              Create Employee
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
}
