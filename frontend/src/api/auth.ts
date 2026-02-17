import { useMutation } from '@tanstack/react-query'
import { apiClient } from './client'

interface LoginRequest {
  username: string
  password: string
}

interface LoginResponse {
  access_token: string
  refresh_token: string
  token_type: string
}

interface UserProfile {
  id: string
  username: string
  email: string
  full_name_en: string
  full_name_ar: string
  role: string
  is_active: boolean
  is_ldap_user: boolean
}

export const useLogin = () => {
  return useMutation({
    mutationFn: async (credentials: LoginRequest) => {
      const response = await apiClient.post<LoginResponse>('/auth/login', credentials)
      return response.data
    },
  })
}

export const useGetProfile = () => {
  return useMutation({
    mutationFn: async () => {
      const response = await apiClient.get<UserProfile>('/auth/me')
      return response.data
    },
  })
}
