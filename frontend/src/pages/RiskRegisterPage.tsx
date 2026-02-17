import { useTranslation } from 'react-i18next'
import { useRisks } from '../api/risks'

export default function RiskRegisterPage() {
  const { t } = useTranslation()
  const { data: risks, isLoading } = useRisks()

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">{t('risks.title')}</h1>
        <button className="rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90">
          {t('risks.addRisk')}
        </button>
      </div>

      <div className="rounded-lg border bg-card">
        {isLoading ? (
          <div className="p-6 text-center text-muted-foreground">
            {t('common.loading')}
          </div>
        ) : risks && risks.length > 0 ? (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="border-b">
                <tr>
                  <th className="px-6 py-3 text-start text-sm font-medium">
                    {t('risks.riskId')}
                  </th>
                  <th className="px-6 py-3 text-start text-sm font-medium">
                    {t('risks.title_label')}
                  </th>
                  <th className="px-6 py-3 text-start text-sm font-medium">
                    {t('risks.riskLevel')}
                  </th>
                  <th className="px-6 py-3 text-start text-sm font-medium">
                    {t('risks.status')}
                  </th>
                </tr>
              </thead>
              <tbody>
                {risks.map((risk) => (
                  <tr key={risk.id} className="border-b">
                    <td className="px-6 py-4 text-sm">{risk.risk_id}</td>
                    <td className="px-6 py-4 text-sm">{risk.title_en}</td>
                    <td className="px-6 py-4 text-sm">{risk.risk_level}</td>
                    <td className="px-6 py-4 text-sm">{risk.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="p-6 text-center text-muted-foreground">
            No risks found
          </div>
        )}
      </div>
    </div>
  )
}
