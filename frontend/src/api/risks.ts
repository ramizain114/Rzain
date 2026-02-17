import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { apiClient } from './client'

export interface Risk {
  id: string
  risk_id: string
  title_en: string
  title_ar: string
  impact_score: number
  likelihood_score: number
  risk_score: number
  risk_level: string
  status: string
}

export const useRisks = () => {
  return useQuery({
    queryKey: ['risks'],
    queryFn: async () => {
      const response = await apiClient.get<Risk[]>('/risks')
      return response.data
    },
  })
}

export const useCreateRisk = () => {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (riskData: Partial<Risk>) => {
      const response = await apiClient.post('/risks', riskData)
      return response.data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['risks'] })
    },
  })
}
