import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { Plus } from 'lucide-react'
import { useRisks } from '../api/risks'
import { getRiskLevelColor, getRiskLevelTextColor } from '../lib/utils'
import RiskMatrix from '../components/risks/RiskMatrix'
import RiskHeatmap from '../components/risks/RiskHeatmap'
import RiskForm from '../components/risks/RiskForm'

export default function RiskRegisterPage() {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'
  const { data: risks, isLoading, refetch } = useRisks()
  const [showForm, setShowForm] = useState(false)
  const [view, setView] = useState<'table' | 'matrix' | 'heatmap'>('table')

  const handleFormSuccess = () => {
    setShowForm(false)
    refetch()
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">{t('risks.title')}</h1>
        <div className="flex gap-2">
          <div className="flex rounded-lg border bg-background">
            <button
              onClick={() => setView('table')}
              className={`px-3 py-2 text-sm font-medium rounded-s-lg transition-colors ${
                view === 'table' ? 'bg-primary text-primary-foreground' : 'hover:bg-accent'
              }`}
            >
              {isArabic ? 'جدول' : 'Table'}
            </button>
            <button
              onClick={() => setView('matrix')}
              className={`px-3 py-2 text-sm font-medium transition-colors ${
                view === 'matrix' ? 'bg-primary text-primary-foreground' : 'hover:bg-accent'
              }`}
            >
              {isArabic ? 'مصفوفة' : 'Matrix'}
            </button>
            <button
              onClick={() => setView('heatmap')}
              className={`px-3 py-2 text-sm font-medium rounded-e-lg transition-colors ${
                view === 'heatmap' ? 'bg-primary text-primary-foreground' : 'hover:bg-accent'
              }`}
            >
              {isArabic ? 'خريطة حرارية' : 'Heatmap'}
            </button>
          </div>
          <button
            onClick={() => setShowForm(true)}
            className="flex items-center gap-2 rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90"
          >
            <Plus className="h-4 w-4" />
            {t('risks.addRisk')}
          </button>
        </div>
      </div>

      {/* Risk Form Modal */}
      {showForm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="w-full max-w-4xl rounded-lg border bg-card p-6 shadow-lg max-h-[90vh] overflow-y-auto">
            <h2 className="text-xl font-semibold mb-4">{t('risks.addRisk')}</h2>
            <RiskForm onSuccess={handleFormSuccess} onCancel={() => setShowForm(false)} />
          </div>
        </div>
      )}

      {/* View content */}
      {view === 'matrix' && risks && <RiskMatrix risks={risks} />}
      
      {view === 'heatmap' && risks && <RiskHeatmap risks={risks} />}

      {view === 'table' && (
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
                      {t('risks.impact')}
                    </th>
                    <th className="px-6 py-3 text-start text-sm font-medium">
                      {t('risks.likelihood')}
                    </th>
                    <th className="px-6 py-3 text-start text-sm font-medium">
                      {isArabic ? 'الدرجة' : 'Score'}
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
                    <tr key={risk.id} className="border-b hover:bg-accent/50">
                      <td className="px-6 py-4 text-sm font-medium">{risk.risk_id}</td>
                      <td className="px-6 py-4 text-sm">
                        {isArabic ? risk.title_ar : risk.title_en}
                      </td>
                      <td className="px-6 py-4 text-sm">{risk.impact_score}/5</td>
                      <td className="px-6 py-4 text-sm">{risk.likelihood_score}/5</td>
                      <td className="px-6 py-4 text-sm font-bold">{risk.risk_score}</td>
                      <td className="px-6 py-4 text-sm">
                        <span className={`inline-flex items-center rounded-full px-2 py-1 text-xs font-medium ${getRiskLevelColor(risk.risk_level)} text-white`}>
                          {risk.risk_level}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm">{risk.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="p-6 text-center text-muted-foreground">
              {isArabic ? 'لم يتم العثور على مخاطر' : 'No risks found'}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
