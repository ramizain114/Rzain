import { useQuery } from '@tanstack/react-query'
import { apiClient } from './client'

export interface DashboardSummary {
  total_controls: number
  implemented_controls: number
  compliance_percentage: number
  total_risks: number
  open_risks: number
  critical_risks: number
  total_audits: number
  active_audits: number
  open_findings: number
}

export const useDashboardSummary = () => {
  return useQuery({
    queryKey: ['dashboard-summary'],
    queryFn: async () => {
      const response = await apiClient.get<DashboardSummary>('/dashboard/summary')
      return response.data
    },
  })
}
