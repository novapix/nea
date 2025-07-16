import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  SuperadminDashboard,
  BranchAdminDashboard,
  MeterReaderDashboard,
  CustomerDashboard
} from './dashboards'
import { UserRole } from '@/types/user'

export default function Dashboard() {
  const navigate = useNavigate()
  const [userRole, setUserRole] = useState<UserRole | null>(null)

  useEffect(() => {
    // In a real app, you would decode the JWT token to get the user role
    // For now, we'll use a mock implementation
    const token = localStorage.getItem('access_token')
    if (!token) {
      navigate('/login')
      return
    }
    
    // Mock - replace with actual JWT decoding
    setUserRole(UserRole.SUPERADMIN)
  }, [navigate])

  if (!userRole) return <div>Loading...</div>

  switch (userRole) {
    case UserRole.SUPERADMIN:
      return <SuperadminDashboard />
    case UserRole.BRANCH_ADMIN:
      return <BranchAdminDashboard />
    case UserRole.METER_READER:
      return <MeterReaderDashboard />
    case UserRole.CUSTOMER:
      return <CustomerDashboard />
    default:
      return <div>Unauthorized</div>
  }
}
