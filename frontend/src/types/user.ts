export const UserRole = {
  SUPERADMIN: 'superadmin',
  BRANCH_ADMIN: 'branch_admin',
  METER_READER: 'meter_reader',
  CUSTOMER: 'customer'
} as const

export type UserRole = typeof UserRole[keyof typeof UserRole]

export interface User {
  id: number
  username: string
  role: UserRole
}
